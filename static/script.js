

async function fetchEvents() {
    try {
        const res = await fetch('/events');
        const events = await res.json();

        const ul = document.getElementById('eventList');
        ul.innerHTML = ""; 

        events.forEach(event => {
            const li = document.createElement('li');
            const date = new Date(event.timestamp).toUTCString();
            let message = "";

            switch (event.action_type) {
                case "push":
                    message = `${event.author} pushed to ${event.to_branch} on ${date}`;
                    break;
                case "pull_request":
                    message = `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch} on ${date}`;
                    break;
                case "merge":
                    message = `${event.author} merged branch ${event.from_branch} to ${event.to_branch} on ${date}`;
                    break;
                default:
                    message = "Unknown event";
            }

            li.textContent = message;
            ul.appendChild(li);
        });

    } catch (error) {
        console.error("Error fetching events:", error);
    }
}


fetchEvents();


setInterval(fetchEvents, 15000);

