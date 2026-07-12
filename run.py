"""Development entry point for MovePal."""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=False)
