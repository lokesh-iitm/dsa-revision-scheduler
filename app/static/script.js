async function loadDashboard(){

    const response = await fetch("/dashboard");

    const data = await response.json();

    document.getElementById("total-problems").innerText =
        data.total_solved_problems;

    document.getElementById("pending-revisions").innerText =
        data.pending_revisions;
}
async function loadProblems(){

    const response = await fetch("/problems");

    const data = await response.json();

    const tbody =
        document.querySelector("#problems-table tbody");

    tbody.innerHTML = "";

    data.forEach(problem => {

        tbody.innerHTML += `
            <tr>
                <td>${problem[0]}</td>
                <td>${problem[1]}</td>
                <td>${problem[2]}</td>
                <td>${problem[3]}</td>
                <td>${problem[4]}</td>
            </tr>
        `;
    });
}

loadDashboard();
document
.getElementById("problem-form")
.addEventListener("submit", async function(e){

    e.preventDefault();

    const problem = {

        title:
            document.getElementById("title").value,

        topic:
            document.getElementById("topic").value,

        difficulty:
            document.getElementById("difficulty").value
    };

    const response = await fetch(
        "/problem",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(problem)
        }
    );

    const data = await response.json();

    alert(data.message);

    loadDashboard();
});
loadDashboard();
loadProblems();
async function loadUpcomingRevisions(){

    const response =
        await fetch("/revisions/upcoming");

    const data = await response.json();

    const tbody =
        document.querySelector("#revisions-table tbody");

    tbody.innerHTML = "";

    data.forEach(revision => {

        tbody.innerHTML += `
            <tr>
                <td>${revision[0]}</td>
                <td>${revision[1]}</td>
                <td>${revision[2]}</td>
                <td>${revision[3]}</td>
            </tr>
        `;
    });
}
loadDashboard();
loadProblems();
loadUpcomingRevisions();