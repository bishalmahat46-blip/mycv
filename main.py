from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
INDEX = Path(__file__).parent / "index.html"

@app.get("/", response_class=HTMLResponse)
def home():
    return INDEX.read_text(encoding="utf-8")
