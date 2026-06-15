async function loadDashboard(){

    const response = await fetch("/dashboard");

    const data = await response.json();

    document.getElementById("total-problems").innerText =
        data.total_solved_problems;

    document.getElementById("pending-revisions").innerText =
        data.pending_revisions;
}

loadDashboard();