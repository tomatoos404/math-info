let div1 = document.createElement("div");
div1.textContent = "tp 2 en cours";
document.body.appendChild(div1);

let normbre1 = document.getElementById("number");
let normbre2 = document.getElementById("number2");
let lasomme = document.querySelector(".lasomme");
document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
    let somme = parseFloat(normbre1.value) + parseFloat(normbre2.value);
    lasomme.textContent = "La somme est : " + somme;
});
