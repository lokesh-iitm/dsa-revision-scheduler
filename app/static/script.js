async function loadDashboard(){

    const response = await fetch("/dashboard");

    const data = await response.json();

    document.getElementById("total-problems").innerText =
        data.total_solved_problems;

    document.getElementById("pending-revisions").innerText =
        data.pending_revisions;
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