from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(title="Box Cricket Bhilwara")

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Box Cricket Bhilwara - Book Your Slot</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #fff;
            min-height: 100vh;
        }
        header {
            background: rgba(0,0,0,0.4);
            padding: 16px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #00e676;
        }
        header h1 { font-size: 1.8rem; color: #00e676; letter-spacing: 1px; }
        header p { font-size: 0.9rem; color: #b0bec5; }
        nav a {
            color: #fff;
            text-decoration: none;
            margin-left: 24px;
            font-size: 0.95rem;
            transition: color 0.2s;
        }
        nav a:hover { color: #00e676; }

        .hero {
            text-align: center;
            padding: 80px 20px 40px;
        }
        .hero h2 { font-size: 3rem; font-weight: 700; }
        .hero h2 span { color: #00e676; }
        .hero p {
            margin-top: 16px;
            font-size: 1.1rem;
            color: #b0bec5;
            max-width: 560px;
            margin-left: auto;
            margin-right: auto;
        }
        .hero .cta {
            display: inline-block;
            margin-top: 32px;
            padding: 14px 40px;
            background: #00e676;
            color: #000;
            font-weight: 700;
            border-radius: 30px;
            text-decoration: none;
            font-size: 1rem;
            transition: background 0.2s;
        }
        .hero .cta:hover { background: #69f0ae; }

        .features {
            display: flex;
            justify-content: center;
            gap: 24px;
            padding: 48px 40px;
            flex-wrap: wrap;
        }
        .card {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 28px 24px;
            width: 220px;
            text-align: center;
            transition: transform 0.2s;
        }
        .card:hover { transform: translateY(-6px); }
        .card .icon { font-size: 2.4rem; margin-bottom: 12px; }
        .card h3 { font-size: 1rem; margin-bottom: 8px; }
        .card p { font-size: 0.85rem; color: #b0bec5; }

        .booking-section {
            max-width: 600px;
            margin: 0 auto 60px;
            padding: 0 20px;
        }
        .booking-section h2 {
            text-align: center;
            font-size: 1.8rem;
            margin-bottom: 28px;
        }
        .booking-section h2 span { color: #00e676; }
        form {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 32px;
        }
        .form-group { margin-bottom: 20px; }
        label { display: block; font-size: 0.9rem; color: #b0bec5; margin-bottom: 6px; }
        input, select {
            width: 100%;
            padding: 12px 16px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 8px;
            color: #fff;
            font-size: 0.95rem;
            outline: none;
            transition: border 0.2s;
        }
        input:focus, select:focus { border-color: #00e676; }
        select option { background: #203a43; }
        .submit-btn {
            width: 100%;
            padding: 14px;
            background: #00e676;
            color: #000;
            font-weight: 700;
            font-size: 1rem;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            transition: background 0.2s;
            margin-top: 8px;
        }
        .submit-btn:hover { background: #69f0ae; }

        .slots {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            padding: 0 40px 60px;
        }
        .slots h2 {
            width: 100%;
            text-align: center;
            font-size: 1.5rem;
            margin-bottom: 20px;
        }
        .slots h2 span { color: #00e676; }
        .slot-badge {
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }
        .available { background: rgba(0,230,118,0.15); border: 1px solid #00e676; color: #00e676; }
        .booked    { background: rgba(244,67,54,0.15);  border: 1px solid #f44336;  color: #f44336; }

        footer {
            text-align: center;
            padding: 24px;
            background: rgba(0,0,0,0.3);
            font-size: 0.85rem;
            color: #607d8b;
        }
    </style>
</head>
<body>

<header>
    <div>
        <h1>🏏 Box Cricket Bhilwara</h1>
        <p>Bhilwara, Rajasthan — India's Sport Hub</p>
    </div>
    <nav>
        <a href="#book">Book Slot</a>
        <a href="#slots">Availability</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<section class="hero">
    <h2>Play. <span>Book.</span> Win.</h2>
    <p>Reserve your box cricket slot in Bhilwara — floodlit turf, professional pitches, and instant confirmation.</p>
    <a href="#book" class="cta">Book a Slot Now</a>
</section>

<section class="features">
    <div class="card"><div class="icon">🌟</div><h3>Floodlit Turf</h3><p>Play day or night on our premium synthetic turf.</p></div>
    <div class="card"><div class="icon">⚡</div><h3>Instant Booking</h3><p>Confirm your slot in under 60 seconds online.</p></div>
    <div class="card"><div class="icon">👥</div><h3>Team Events</h3><p>Tournaments & corporate events available.</p></div>
    <div class="card"><div class="icon">📍</div><h3>Central Location</h3><p>Easily accessible from all parts of Bhilwara.</p></div>
</section>

<section class="slots" id="slots">
    <h2>Today's <span>Slot Availability</span></h2>
    <span class="slot-badge available">6:00 AM – 7:00 AM</span>
    <span class="slot-badge booked">7:00 AM – 8:00 AM</span>
    <span class="slot-badge available">8:00 AM – 9:00 AM</span>
    <span class="slot-badge booked">5:00 PM – 6:00 PM</span>
    <span class="slot-badge available">6:00 PM – 7:00 PM</span>
    <span class="slot-badge available">7:00 PM – 8:00 PM</span>
    <span class="slot-badge booked">8:00 PM – 9:00 PM</span>
    <span class="slot-badge available">9:00 PM – 10:00 PM</span>
</section>

<section class="booking-section" id="book">
    <h2>Book Your <span>Slot</span></h2>
    <form action="/book" method="post">
        <div class="form-group">
            <label>Full Name</label>
            <input type="text" name="name" placeholder="e.g. Rahul Sharma" required>
        </div>
        <div class="form-group">
            <label>Phone Number</label>
            <input type="tel" name="phone" placeholder="+91 9XXXXXXXXX" required>
        </div>
        <div class="form-group">
            <label>Date</label>
            <input type="date" name="date" required>
        </div>
        <div class="form-group">
            <label>Time Slot</label>
            <select name="slot" required>
                <option value="">Select a slot</option>
                <option>6:00 AM – 7:00 AM</option>
                <option>8:00 AM – 9:00 AM</option>
                <option>6:00 PM – 7:00 PM</option>
                <option>7:00 PM – 8:00 PM</option>
                <option>9:00 PM – 10:00 PM</option>
            </select>
        </div>
        <div class="form-group">
            <label>Number of Players</label>
            <select name="players" required>
                <option value="">Select</option>
                <option>6 players</option>
                <option>8 players</option>
                <option>10 players</option>
                <option>12 players</option>
            </select>
        </div>
        <button type="submit" class="submit-btn">Confirm Booking ✅</button>
    </form>
</section>

<footer id="contact">
    📍 Bhilwara, Rajasthan &nbsp;|&nbsp; 📞 +91 98XXX XXXXX &nbsp;|&nbsp; ✉ bookings@boxcricketbhilwara.in
    <br><br>© 2026 Box Cricket Bhilwara. All rights reserved.
</footer>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def homepage():
    return HTML_PAGE


class Booking(BaseModel):
    name: str
    phone: str
    date: str
    slot: str
    players: str


bookings: list[Booking] = []


@app.post("/book", response_class=HTMLResponse)
async def book_slot(
    name: str = Form(...),
    phone: str = Form(...),
    date: str = Form(...),
    slot: str = Form(...),
    players: str = Form(...),
):
    booking = Booking(name=name, phone=phone, date=date, slot=slot, players=players)
    bookings.append(booking)
    return f"""
    <html><body style="font-family:sans-serif;background:#0f2027;color:#fff;text-align:center;padding:80px">
    <h1 style="color:#00e676">Booking Confirmed! 🏏</h1>
    <p style="margin-top:16px">Thanks <strong>{name}</strong>, your slot <strong>{slot}</strong> on <strong>{date}</strong> for {players} is confirmed.</p>
    <p style="color:#b0bec5;margin-top:8px">We'll send details to {phone}.</p>
    <a href="/" style="display:inline-block;margin-top:32px;padding:12px 32px;background:#00e676;color:#000;border-radius:24px;text-decoration:none;font-weight:700">← Back to Home</a>
    </body></html>
    """


@app.get("/bookings")
async def list_bookings():
    return {"total": len(bookings), "bookings": bookings}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
