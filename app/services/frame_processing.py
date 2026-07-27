"""Frame processing service.

Handles the transient lifecycle of an uploaded image file:
writes it to a short-lived temporary path, passes that path to
the provided pose adapter, and removes the file before returning.

Keeping this logic in the service layer means the route stays
responsible only for HTTP concerns (reading the request, returning
JSON), while all file-I/O coordination lives here.
"""

from __future__ import annotations

import logging
import tempfile
import time
from pathlib import Path
from typing import Protocol

from app.services.pose_tracking import PoseResult

logger = logging.getLogger(__name__)


class PoseAdapter(Protocol):
    """Minimal structural type that any pose adapter must satisfy."""

    def estimate(self, image_path: str | Path) -> PoseResult: ...


def process_frame(file: object, pose_adapter: PoseAdapter) -> PoseResult:
    """Save *file* to a temporary path, run *pose_adapter*, then delete the file.

    ``file`` is expected to be a Werkzeug ``FileStorage`` object
    (or any object with a ``filename`` attribute and a ``save`` method),
    so this function never imports Flask directly.

    The temporary file is deleted in a ``finally`` block regardless of
    whether the adapter raises an exception, so uploaded bytes are never
    retained on disk beyond a single request.

    Parameters
    ----------
    file:
        The uploaded file object. Must expose ``.filename`` (str) and
        ``.save(path)`` (saves bytes to *path*).
    pose_adapter:
        Any object with an ``estimate(image_path) -> PoseResult`` method.

    Returns
    -------
    PoseResult
        The result returned by ``pose_adapter.estimate``.
    """
    original_filename: str = getattr(file, "filename", "") or ""
    extension = (
        original_filename.rsplit(".", 1)[-1].lower()
        if "." in original_filename
        else "tmp"
    )
    suffix = f".{extension}"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_path = Path(temp_file.name)

    started = time.perf_counter()
    try:
        save_started = time.perf_counter()
        file.save(temp_path)  # type: ignore[union-attr]
        save_seconds = time.perf_counter() - save_started
        inference_started = time.perf_counter()
        result = pose_adapter.estimate(temp_path)
        logger.info(
            "frame_processing save_seconds=%.4f adapter_seconds=%.4f "
            "total_seconds=%.4f",
            save_seconds,
            time.perf_counter() - inference_started,
            time.perf_counter() - started,
        )
        return result
    finally:
        if temp_path.exists():
            temp_path.unlink()
