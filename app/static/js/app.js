function calculate() {
    const a = document.getElementById("a").value;
    const b = document.getElementById("b").value;
    const operation = document.getElementById("operation").value;

    fetch("/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ a, b, operation })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText =
            data.result !== undefined ? "Result: " + data.result : data.error;
    });
}
