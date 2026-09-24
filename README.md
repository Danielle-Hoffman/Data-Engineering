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

    1. open the files and make sure you install the requirements txt 

    2. Once thats done make sure you have live server installed or like anthing that'll allow you to view it in port 5000 

    3. run it and bam! you can now view the project