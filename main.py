from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def homepage():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Home</title></head>
    <body>
        <h1>Welcome to FastAPI</h1>
        <p>Your API is up and running.</p>
    </body>
    </html>
    """
