# Data-Engineering
This repository holds my data engineering elective project.
WTC-DXKWTBAT


## Main idea 
For this project I was thinking about myself as a consumer. I do youtube on the side and I make gaming videos and the one issue I came across as a youtuber is never knowing what is actually trending vs what I think is trending because of the algorithm I built off of my interests. 

The main idea for this project is a web app that shows me what is trending on youtube and twitch in real time based off of what category of content I do, such as in this case Gaming. The data is not affected by the algorithm or your personal likes and dislikes. This app enables users to see the data and make a decision of weather to follow trends, see rising trends and jump on during its peak or revisit past trends.

It's something I will use and do actually use. 


## 📂 Project Architecture
```text
stream-pulse/
├── .env                 # Local API keys and DB credentials
├── DESIGN.md            # System architecture and Mermaid ERD
├── requirements.txt     # Python backend dependencies
├── db/
│   └── schema.sql       # PostgreSQL DDL and analytical views
├── ingestion/
│   └── fetcher.py       # API polling and database insertion script
├── backend/
│   ├── main.py          # FastAPI application routes
│   └── database.py      # PostgreSQL connection pooling
└── frontend/
    ├── index.html       # Dashboard layout
    ├── style.css        # UI styling
    └── app.js           # API fetching and DOM manipulation



    ##How do I run this?
    Okay so I need you to listen cause its still in development. Okay! so: 

    1. Setup Environment & Dependencies
Open your terminal in the project root and isolate your Python environment:

Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
2. Configure API Keys
Create a .env file in the root directory and add your Twitch credentials:

Ini, TOML
TWITCH_CLIENT_ID=your_client_id_here
TWITCH_APP_SECRET=your_app_secret_here
3. Initialize Database & Fetch Data
Build the local SQLite database and populate it with a live batch of Twitch data:

Bash
# Build the tables and views
sqlite3 lobbystats.db < db/schema.sql

# Ingest live streams (filters out non-gaming IRL categories)
python ingestion/fetcher.py
4. Start the Backend API
Keep your virtual environment active and start the FastAPI server:

Bash
uvicorn backend.main:app --reload
The API is now listening on http://127.0.0.1:8000.

5. Launch the Frontend Dashboard
With the backend running, open the frontend/index.html file. You can do this by right-clicking the file in VS Code and selecting Open with Live Server (which typically hosts on port 5500), or by simply double-clicking the HTML file in your Mac Finder to open it natively in Chrome.