
input = document.getElementById("input");
button = document.getElementById("button");

button.addEventListener("click", function() {
    let number = parseInt(input.value);
    if (number % 2 === 0) {
        alert("le nombre est pair");
    } else {
        alert("le nombre est impair");
    }
});