"""Static asset presence checks, OS-portable via pathlib."""

from pathlib import Path


def test_static_assets_exist():
    static_dir = Path(__file__).parents[2] / "app" / "static"
    assert (static_dir / "css" / "app.css").is_file()
    assert (static_dir / "js" / "app.js").is_file()
