function generateTable() {
    let numProcesses = parseInt(document.getElementById("num_processes").value);
    let numResources = parseInt(document.getElementById("num_resources").value);
    let tablesDiv = document.getElementById("tables");
    tablesDiv.innerHTML = '';

    let availableTable = `<h3>Available Resources</h3><table><tr><th></th>`;
    for (let j = 0; j < numResources; j++) {
        availableTable += `<th><strong>Resource ${j + 1} ↓</strong></th>`;
    }
    availableTable += `</tr><tr><td><strong>Available</strong></td>`;
    for (let j = 0; j < numResources; j++) {
        availableTable += `<td><input type="number" id="available_${j}" value="0"></td>`;
    }
    availableTable += `</tr></table>`;
    tablesDiv.innerHTML += availableTable;

    let maxNeedTable = `<h3>Max Need</h3><table><tr><th></th>`;
    for (let j = 0; j < numResources; j++) {
        maxNeedTable += `<th><strong>Resource ${j + 1} ↓</strong></th>`;
    }
    maxNeedTable += `</tr>`;
    for (let i = 0; i < numProcesses; i++) {
        maxNeedTable += `<tr><td><strong>Process ${i + 1} →</strong></td>`;
        for (let j = 0; j < numResources; j++) {
            maxNeedTable += `<td><input type="number" id="max_${i}_${j}" value="0"></td>`;
        }
        maxNeedTable += `</tr>`;
    }
    maxNeedTable += `</table>`;
    tablesDiv.innerHTML += maxNeedTable;

    let allocatedTable = `<h3>Allocated</h3><table><tr><th></th>`;
    for (let j = 0; j < numResources; j++) {
        allocatedTable += `<th><strong>Resource ${j + 1} ↓</strong></th>`;
    }
    allocatedTable += `</tr>`;
    for (let i = 0; i < numProcesses; i++) {
        allocatedTable += `<tr><td><strong>Process ${i + 1} →</strong></td>`;
        for (let j = 0; j < numResources; j++) {
            allocatedTable += `<td><input type="number" id="alloc_${i}_${j}" value="0"></td>`;
        }
        allocatedTable += `</tr>`;
    }
    allocatedTable += `</table>`;
    tablesDiv.innerHTML += allocatedTable;
}

function checkSafety() {
    let numProcesses = parseInt(document.getElementById("num_processes").value);
    let numResources = parseInt(document.getElementById("num_resources").value);

    let available = [];
    for (let j = 0; j < numResources; j++) {
        available.push(parseInt(document.getElementById(`available_${j}`).value));
    }

    let maxNeed = [];
    let allocated = [];

    for (let i = 0; i < numProcesses; i++) {
        let maxRow = [];
        let allocRow = [];
        for (let j = 0; j < numResources; j++) {
            maxRow.push(parseInt(document.getElementById(`max_${i}_${j}`).value));
            allocRow.push(parseInt(document.getElementById(`alloc_${i}_${j}`).value));
        }
        maxNeed.push(maxRow);
        allocated.push(allocRow);
    }

    fetch("/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ available, max_need: maxNeed, allocated })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.safe ? `Safe Sequence: ${data.sequence.join(" → ")}` : "Unsafe State!";
    });
}