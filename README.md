# Data-Engineering
This repository holds my data engineering elective project.
WTC-DXKWTBAT

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