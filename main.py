from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1>Docker Website Running 🚀</h1>
            <p>Fully isolated environment</p>
        </body>
    </html>
    """
