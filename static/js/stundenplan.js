document.getElementById("loadSchedule").addEventListener("click", () => {
    const className = document.getElementById("class").value;
    const year = document.getElementById("year").value;
    const week = document.getElementById("week").value;

    fetch(`/api/schedule?class=${className}&year=${year}&week=${week}`)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById("scheduleTable").querySelector("tbody");
            tableBody.innerHTML = ""; // Tabelle leeren

            data.forEach(entry => {
                const row = document.createElement("tr");
                row.innerHTML = `<td>${entry.time}</td><td>${entry.subject}</td>`;
                tableBody.appendChild(row);
            });
        });
});