# MovePal

MovePal is an AI-powered movement analysis and exercise tracking platform. It leverages computer vision and landmark estimation to evaluate physical movement form in real-time, calculate scores, and provide immediate feedback and session summaries to users.

---

## Key Features

* **Real-time Pose Tracking:** Uses computer vision (MediaPipe) to track key body landmarks across video frames.
* **Movement Rule Evaluation:** Calculates joint angles and checks form against pre-defined movement rules.
* **Live Feedback Engine:** Provides instantaneous visual/audio feedback to help users correct their posture and technique.
* **Scoring & Performance Metrics:** Evaluates rep quality, consistency, and overall form score.
* **Session Summaries:** Generates post-workout reports and analytics.

---

## Tech Stack

* **Backend:** Python (FastAPI / Flask)
* **Computer Vision:** MediaPipe, OpenCV, NumPy
* **Data & Storage:** JSON-based landmark fixtures & session stores
* **Frontend:** HTML5, CSS3, JavaScript / Jinja2 Templates

---

## Project Structure

```text
movepal/
├── app/
│   ├── routes/
│   │   ├── api.py            # REST API endpoints for pose data & scoring
│   │   └── pages.py          # Frontend view routes
│   ├── services/
│   │   ├── pose_tracking.py  # MediaPipe landmark extraction logic
│   │   ├── movement_rules.py # Angle calculations & pose verification
│   │   ├── scoring.py        # Performance scoring algorithms
│   │   ├── feedback.py       # Real-time feedback generator
│   │   └── session_summary.py# Summary & analytics aggregator
│   └── templates/            # HTML templates
├── data/
│   └── landmarks/            # Landmark JSON test fixtures
├── backlog/                  # Task documentation & project backlog
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## Installation & Local Setup

### Prerequisites
* Python 3.9+
* pip package manager
* Git

### 1. Clone the Repository
```bash
git clone https://github.com/your-org/movepal.git
cd movepal
```

### 2. Create and Activate a Virtual Environment
* **Linux/macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app/main.py
```
> Access the application in your browser at `http://localhost:8000` (or `[http://127.0.0.1:5000](http://127.0.0.1:5000)`).

---

## Testing & Data Fixtures

To run unit tests or evaluate landmark fixtures:

```bash
pytest
```

Mock landmark data for testing movement rules can be found in `data/landmarks/`.

---

## Contributing Workflow

We follow a feature-branch / Pull Request workflow:

1. Create a feature branch off `master`:
   ```bash
   git checkout -b feature/task-9-implementation
   ```
2. Commit your changes with clear messages.
3. Keep your branch updated with `master`:
   ```bash
   git fetch origin
   git merge origin/master
   ```
4. Push your branch and open a Pull Request (PR) for review.

---

## License

This project is developed for internal team use / educational purposes.
