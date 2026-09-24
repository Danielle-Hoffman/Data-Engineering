const API_BASE = "http://127.0.0.1:8000/api";
const container = document.getElementById("dashboard-container");
const btnOpps = document.getElementById("btn-opportunities");
const btnSuggestions = document.getElementById("btn-suggestions");
const btnStreams = document.getElementById("btn-streams");
const btnAbout = document.getElementById("btn-about");

async function loadOpportunities() {
    container.innerHTML = "<p>Calculating market opportunities...</p>";
    btnOpps.classList.add("active");
    btnSuggestions.classList.remove("active");
    btnStreams.classList.remove("active");
    btnAbout.classList.remove("active");
    
    try {
        const res = await fetch(`${API_BASE}/opportunities`);
        const data = await res.json();
        
        container.innerHTML = data.map(item => `
            <div class="card">
                <h3>${item.category_name}</h3>
                <p>Genre Category: ${item.genre_type}</p>
                <p>Active Broadcasters: ${item.active_streams}</p>
                <p>Total Viewership: ${item.total_viewers}</p>
                <div class="metric">Opp Score: ${item.opportunity_score}</div>
            </div>
        `).join("");
    } catch (error) {
        container.innerHTML = `<p>Error connecting to database. Is FastAPI running?</p>`;
    }
}

async function loadSuggestions() {
    container.innerHTML = "<p>Running recommendation algorithm...</p>";
    btnSuggestions.classList.add("active");
    btnOpps.classList.remove("active");
    btnStreams.classList.remove("active");
    btnAbout.classList.remove("active");
    
    try {
        const res = await fetch(`${API_BASE}/suggestions`);
        const data = await res.json();
        
        container.innerHTML = data.map(item => `
            <div class="card" style="border-left: 4px solid var(--accent);">
                <h3>${item.category_name}</h3>
                <p><strong>Why play this?</strong> High viewer ratio.</p>
                <p>Current Viewers: ${item.total_viewers.toLocaleString()}</p>
                <p>Competing Streams: ${item.active_streams}</p>
                <div class="metric">Score: ${item.opportunity_score}</div>
            </div>
        `).join("");
    } catch (error) {
        container.innerHTML = `<p>Error connecting to database. Is FastAPI running?</p>`;
    }
}

async function loadStreams() {
    container.innerHTML = "<p>Scanning live streams...</p>";
    btnStreams.classList.add("active");
    btnOpps.classList.remove("active");
    btnSuggestions.classList.remove("active");
    btnAbout.classList.remove("active");
    
    try {
        const res = await fetch(`${API_BASE}/streams`);
        const data = await res.json();
        
        container.innerHTML = data.map(item => `
            <div class="card">
                <img src="${item.thumbnail_url}" alt="Stream Thumbnail">
                <h4>${item.stream_title}</h4>
                <p>${item.broadcaster_name} • ${item.category_name}</p>
                <div class="metric">👁 ${item.viewer_count.toLocaleString()}</div>
            </div>
        `).join("");
    } catch (error) {
        container.innerHTML = `<p>Error connecting to database. Is FastAPI running?</p>`;
    }
}

function loadAbout() {
    btnAbout.classList.add("active");
    btnOpps.classList.remove("active");
    btnSuggestions.classList.remove("active");
    btnStreams.classList.remove("active");
    
    container.innerHTML = `
        <div class="card" style="grid-column: 1 / -1; max-width: 800px;">
            <h2 style="margin-top: 0; color: var(--accent);">Understanding the Opportunity Score</h2>
            <p>Mathematically, the Opportunity Score represents the <strong>average number of viewers per active stream</strong> for that specific game.</p>
            <p>Strategically, it is an indicator of <strong>supply and demand</strong>. It tells a creator exactly where the gaps in the market are.</p>
            <hr style="border: 1px solid var(--bg-color); margin: 20px 0;">
            <h3 style="color: #4ade80;">📈 A High Score (High Opportunity)</h3>
            <p>Indicates there is a massive, active audience hungry for this game, but very few creators are actually broadcasting it. If you stream this game, your chances of discovery are incredibly high because the viewers are forced to condense into the few channels available. You aren't fighting an algorithm; you are just filling a void.</p>
            <h3 style="color: #f87171; margin-top: 25px;">📉 A Low Score (High Saturation)</h3>
            <p>Indicates that the audience is spread incredibly thin across too many broadcasters. A game like <em>Fortnite</em> might have 100,000 total viewers, but if there are 10,000 people streaming it, the average viewers-per-stream is abysmal. Your stream would be buried at the very bottom of the directory with almost zero chance of organic discovery.</p>
        </div>
    `;
}

// Attach event listeners to the navigation buttons
btnOpps.addEventListener("click", loadOpportunities);
btnSuggestions.addEventListener("click", loadSuggestions);
btnStreams.addEventListener("click", loadStreams);
btnAbout.addEventListener("click", loadAbout);

// Automatically load the developer opportunities view when the page opens
loadOpportunities();