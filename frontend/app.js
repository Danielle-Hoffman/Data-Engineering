const API_BASE = "http://127.0.0.1:8000/api";
const container = document.getElementById("dashboard-container");
const btnOpps = document.getElementById("btn-opportunities");
const btnStreams = document.getElementById("btn-streams");

async function loadOpportunities() {
    container.innerHTML = "<p>Calculating market opportunities...</p>";
    btnOpps.classList.add("active");
    btnStreams.classList.remove("active");
    
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

async function loadStreams() {
    container.innerHTML = "<p>Scanning live streams...</p>";
    btnStreams.classList.add("active");
    btnOpps.classList.remove("active");
    
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

// Attach event listeners to the navigation buttons
btnOpps.addEventListener("click", loadOpportunities);
btnStreams.addEventListener("click", loadStreams);

// Automatically load the developer opportunities view when the page opens
loadOpportunities();