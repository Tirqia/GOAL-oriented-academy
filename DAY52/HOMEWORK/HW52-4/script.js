function colorChanger() {
    document.getElementById("myParagraph").style.color = "green";
    document.getElementById("Header").style.color = "red";
}

document.getElementById("myButton").addEventListener("click", colorChanger);