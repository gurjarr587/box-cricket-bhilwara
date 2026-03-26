from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def homepage():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Analog Clock</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background: radial-gradient(ellipse at center, #1a1a3e 0%, #0a0a1a 100%);
                font-family: 'Courier New', monospace;
            }
            .clock-wrapper {
                position: relative;
                width: 320px;
                height: 320px;
            }
            .clock-face {
                width: 320px;
                height: 320px;
                border-radius: 50%;
                background: radial-gradient(circle at 30% 30%, #2a2a5a, #0d0d2b);
                border: 4px solid transparent;
                background-clip: padding-box;
                box-shadow:
                    0 0 0 4px #7b2ff7,
                    0 0 0 8px #f72ff7,
                    0 0 40px rgba(123, 47, 247, 0.6),
                    0 0 80px rgba(247, 47, 247, 0.3),
                    inset 0 0 40px rgba(0,0,0,0.5);
                position: relative;
            }
            /* Hour markers */
            .marker {
                position: absolute;
                left: 50%;
                top: 50%;
                transform-origin: 0 0;
            }
            .marker span {
                display: block;
                position: absolute;
                border-radius: 2px;
            }
            .marker.hour span {
                width: 3px;
                height: 18px;
                margin-left: -1.5px;
                margin-top: -148px;
                background: linear-gradient(to bottom, #ff6ec7, #7b2ff7);
                box-shadow: 0 0 6px #ff6ec7;
            }
            .marker.minute span {
                width: 2px;
                height: 10px;
                margin-left: -1px;
                margin-top: -148px;
                background: #3a3a6a;
            }
            /* Hands */
            .hand {
                position: absolute;
                left: 50%;
                top: 50%;
                transform-origin: 50% 100%;
                border-radius: 4px;
            }
            #hour-hand {
                width: 8px;
                height: 90px;
                margin-left: -4px;
                margin-top: -90px;
                background: linear-gradient(to top, #ff6ec7, #c040fb);
                box-shadow: 0 0 12px #ff6ec7, 0 0 24px rgba(255,110,199,0.5);
                border-radius: 4px 4px 2px 2px;
            }
            #minute-hand {
                width: 5px;
                height: 125px;
                margin-left: -2.5px;
                margin-top: -125px;
                background: linear-gradient(to top, #40e0ff, #0080ff);
                box-shadow: 0 0 12px #40e0ff, 0 0 24px rgba(64,224,255,0.5);
                border-radius: 4px 4px 2px 2px;
            }
            #second-hand {
                width: 2px;
                height: 145px;
                margin-left: -1px;
                margin-top: -145px;
                background: linear-gradient(to top, #ff4040, #ffaa00);
                box-shadow: 0 0 8px #ff4040, 0 0 16px rgba(255,64,64,0.6);
                border-radius: 2px;
            }
            /* Counter-weight tail for second hand */
            #second-tail {
                width: 2px;
                height: 30px;
                margin-left: -1px;
                margin-top: 0px;
                background: linear-gradient(to bottom, #ffaa00, transparent);
                border-radius: 2px;
                position: absolute;
                left: 50%;
                top: 50%;
                transform-origin: 50% 0%;
            }
            /* Center dot */
            .center-dot {
                position: absolute;
                left: 50%;
                top: 50%;
                width: 14px;
                height: 14px;
                margin-left: -7px;
                margin-top: -7px;
                border-radius: 50%;
                background: radial-gradient(circle, #ffffff, #ff6ec7);
                box-shadow: 0 0 10px #ff6ec7, 0 0 20px rgba(255,110,199,0.8);
                z-index: 10;
            }
            /* Digital time below */
            #digital {
                margin-top: 30px;
                font-size: 2rem;
                letter-spacing: 0.15em;
                background: linear-gradient(90deg, #ff6ec7, #40e0ff, #7b2ff7, #ffaa00);
                background-size: 300% 100%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: rainbow 4s linear infinite;
            }
            #date-display {
                margin-top: 10px;
                font-size: 0.9rem;
                color: #6666aa;
                letter-spacing: 0.2em;
            }
            @keyframes rainbow {
                0%   { background-position: 0% 50%; }
                100% { background-position: 300% 50%; }
            }

            /* Cricket scorecards */
            .cricket-section {
                width: 100%;
                max-width: 800px;
                margin-top: 50px;
                padding: 0 20px 40px;
            }
            .cricket-title {
                text-align: center;
                font-size: 1.2rem;
                letter-spacing: 0.3em;
                color: #ff6ec7;
                text-shadow: 0 0 10px rgba(255,110,199,0.5);
                margin-bottom: 20px;
                text-transform: uppercase;
            }
            .scorecard {
                background: linear-gradient(135deg, #12122a, #1a1a3e);
                border: 1px solid #2a2a5a;
                border-left: 3px solid #7b2ff7;
                border-radius: 10px;
                padding: 16px 20px;
                margin-bottom: 16px;
                box-shadow: 0 0 20px rgba(123,47,247,0.15);
            }
            .match-status {
                font-size: 0.7rem;
                letter-spacing: 0.2em;
                text-transform: uppercase;
                margin-bottom: 10px;
            }
            .status-live   { color: #ff4040; text-shadow: 0 0 8px #ff4040; }
            .status-result { color: #40e0ff; }
            .status-upcoming { color: #ffaa00; }
            .teams {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 10px;
            }
            .team {
                flex: 1;
            }
            .team-name {
                font-size: 1rem;
                font-weight: bold;
                color: #e0e0ff;
                margin-bottom: 4px;
            }
            .team-score {
                font-size: 1.4rem;
                background: linear-gradient(90deg, #ff6ec7, #40e0ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: bold;
            }
            .team-overs {
                font-size: 0.75rem;
                color: #5555aa;
                margin-top: 2px;
            }
            .vs {
                color: #3a3a6a;
                font-size: 0.9rem;
                padding: 0 8px;
            }
            .match-info {
                margin-top: 10px;
                font-size: 0.75rem;
                color: #4a4a8a;
                border-top: 1px solid #1e1e42;
                padding-top: 8px;
            }
            .match-result {
                margin-top: 6px;
                font-size: 0.8rem;
                color: #40e0ff;
            }
            .api-note {
                text-align: center;
                font-size: 0.75rem;
                color: #3a3a6a;
                margin-top: 20px;
                letter-spacing: 0.1em;
            }
            .api-note a {
                color: #7b2ff7;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="clock-wrapper">
            <div class="clock-face" id="clock-face"></div>
            <div class="hand" id="hour-hand"></div>
            <div class="hand" id="minute-hand"></div>
            <div class="hand" id="second-hand"></div>
            <div id="second-tail"></div>
            <div class="center-dot"></div>
        </div>
        <div id="digital">--:--:--</div>
        <div id="date-display"></div>

        <!-- Cricket Scorecards -->
        <div class="cricket-section">
            <div class="cricket-title">Today's Cricket</div>

            <!-- Match 1 - LIVE -->
            <div class="scorecard">
                <div class="match-status status-live">&#9679; Live · IPL 2025 · Match 42</div>
                <div class="teams">
                    <div class="team">
                        <div class="team-name">Mumbai Indians</div>
                        <div class="team-score">187/4</div>
                        <div class="team-overs">20.0 ov</div>
                    </div>
                    <div class="vs">vs</div>
                    <div class="team" style="text-align:right">
                        <div class="team-name">Chennai Super Kings</div>
                        <div class="team-score">142/6</div>
                        <div class="team-overs">16.3 ov</div>
                    </div>
                </div>
                <div class="match-result">CSK need 46 runs in 21 balls</div>
                <div class="match-info">Wankhede Stadium, Mumbai</div>
            </div>

            <!-- Match 2 - Result -->
            <div class="scorecard">
                <div class="match-status status-result">&#10003; Result · Test Series · Day 4</div>
                <div class="teams">
                    <div class="team">
                        <div class="team-name">India</div>
                        <div class="team-score">412 & 210/3</div>
                        <div class="team-overs">dec</div>
                    </div>
                    <div class="vs">vs</div>
                    <div class="team" style="text-align:right">
                        <div class="team-name">England</div>
                        <div class="team-score">289</div>
                        <div class="team-overs">87.4 ov</div>
                    </div>
                </div>
                <div class="match-result">India won by an innings and 45 runs</div>
                <div class="match-info">M.A. Chidambaram Stadium, Chennai</div>
            </div>

            <!-- Match 3 - Upcoming -->
            <div class="scorecard">
                <div class="match-status status-upcoming">&#9679; Upcoming · ODI Series · Match 2</div>
                <div class="teams">
                    <div class="team">
                        <div class="team-name">Australia</div>
                        <div class="team-score">-- / --</div>
                        <div class="team-overs">yet to bat</div>
                    </div>
                    <div class="vs">vs</div>
                    <div class="team" style="text-align:right">
                        <div class="team-name">South Africa</div>
                        <div class="team-score">-- / --</div>
                        <div class="team-overs">yet to bat</div>
                    </div>
                </div>
                <div class="match-info">Starts at 14:30 IST · Sydney Cricket Ground</div>
            </div>

            <!-- Match 4 - LIVE -->
            <div class="scorecard">
                <div class="match-status status-live">&#9679; Live · T20 World Cup · Semi-Final</div>
                <div class="teams">
                    <div class="team">
                        <div class="team-name">Pakistan</div>
                        <div class="team-score">156/8</div>
                        <div class="team-overs">20.0 ov</div>
                    </div>
                    <div class="vs">vs</div>
                    <div class="team" style="text-align:right">
                        <div class="team-name">New Zealand</div>
                        <div class="team-score">98/3</div>
                        <div class="team-overs">13.2 ov</div>
                    </div>
                </div>
                <div class="match-result">NZ need 59 runs in 40 balls</div>
                <div class="match-info">Dubai International Stadium</div>
            </div>

            <div class="api-note">
                Placeholder data &mdash; connect a live API key at
                <a href="https://cricketdata.org" target="_blank">cricketdata.org</a> for real scores
            </div>
        </div>

        <script>
            // Build tick markers
            const face = document.getElementById('clock-face');
            for (let i = 0; i < 60; i++) {
                const m = document.createElement('div');
                m.className = 'marker ' + (i % 5 === 0 ? 'hour' : 'minute');
                m.style.transform = 'rotate(' + (i * 6) + 'deg)';
                m.innerHTML = '<span></span>';
                face.appendChild(m);
            }

            function setRotation(el, deg) {
                el.style.transform = 'rotate(' + deg + 'deg)';
            }

            function update() {
                const now = new Date();
                const s = now.getSeconds() + now.getMilliseconds() / 1000;
                const m = now.getMinutes() + s / 60;
                const h = (now.getHours() % 12) + m / 60;

                setRotation(document.getElementById('second-hand'), s * 6);
                document.getElementById('second-tail').style.transform =
                    'rotate(' + (s * 6 + 180) + 'deg)';
                setRotation(document.getElementById('minute-hand'), m * 6);
                setRotation(document.getElementById('hour-hand'), h * 30);

                document.getElementById('digital').textContent =
                    now.toLocaleTimeString('en-US', { hour12: false });
                document.getElementById('date-display').textContent =
                    now.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
            }

            update();
            setInterval(update, 50);
        </script>
    </body>
    </html>
    """
