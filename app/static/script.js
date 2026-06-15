async function loadDashboard(){

    const response = await fetch("/dashboard");

    const data = await response.json();

    document.getElementById("total-problems").innerText =
        data.total_solved_problems;

    document.getElementById("pending-revisions").innerText =
        data.pending_revisions;
}
async function loadProblems(){

    const response =
        await fetch("/problems");

    let data =
        await response.json();

    const search =
        document
        .getElementById("search-box")
        .value
        .toLowerCase();

    const topic =
        document
        .getElementById("topic-filter")
        .value;

    const difficulty =
        document
        .getElementById("difficulty-filter")
        .value;

    data = data.filter(problem => {

        const matchesSearch =
            problem[1]
            .toLowerCase()
            .includes(search);

        const matchesTopic =
            topic === ""
            || problem[2] === topic;

        const matchesDifficulty =
            difficulty === ""
            || problem[3] === difficulty;

        return (
            matchesSearch
            && matchesTopic
            && matchesDifficulty
        );
    });

    const tbody =
        document.querySelector(
            "#problems-table tbody"
        );

    tbody.innerHTML = "";

    data.forEach(problem => {

        tbody.innerHTML += `
           <tr>
    <td>${problem[0]}</td>
    <td>${problem[1]}</td>
    <td>${problem[2]}</td>
    <td>${problem[3]}</td>
    <td>${problem[4]}</td>
    <td>
        <button onclick="deleteProblem(${problem[0]})">
            Delete
        </button>
    </td>
</tr>
        `;
    });

    loadTopics(data);
}
async function deleteProblem(id){

    const response =
        await fetch(
            `/problem/${id}`,
            {
                method: "DELETE"
            }
        );

    const data =
        await response.json();

    alert(data.message);

    loadDashboard();
    loadProblems();
    loadUpcomingRevisions();
}
function loadTopics(data){

    const select =
        document.getElementById(
            "topic-filter"
        );

    const current =
        select.value;

    select.innerHTML =
        '<option value="">All Topics</option>';

    const topics =
        [...new Set(
            data.map(
                p => p[2]
            )
        )];

    topics.forEach(topic => {

        select.innerHTML += `
            <option value="${topic}">
                ${topic}
            </option>
        `;
    });

    select.value = current;
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
    document.getElementById("title").value = "";
    document.getElementById("topic").value = "";
    document.getElementById("difficulty").value = "";

    loadDashboard();
loadProblems();
loadUpcomingRevisions();
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
document
.getElementById("search-box")
.addEventListener(
    "input",
    loadProblems
);

document
.getElementById("topic-filter")
.addEventListener(
    "change",
    loadProblems
);

document
.getElementById("difficulty-filter")
.addEventListener(
    "change",
    loadProblems
);
loadDashboard();
loadProblems();
loadUpcomingRevisions();
