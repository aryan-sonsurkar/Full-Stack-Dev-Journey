let rankElement = document.getElementById("rank");
let levelElement = document.getElementById("num_level");
let button = document.getElementById("levelBtn");

let level = 1;
button.addEventListener(
    "click",
    function() {
        console.log("Button Clicked!");
        level += 1;
        levelElement.textContent = `LEVEL: ${level}`;
        if (level >= 10) {
            rankElement.textContent = "S-RANK HUNTER";
        }
    }
);