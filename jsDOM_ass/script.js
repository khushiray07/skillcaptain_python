const button = document.getElementById("changeTextButton");

const paragraph = document.getElementById("myParagraph");

button.addEventListener("click", function() {
  paragraph.textContent = "The message has been changed!";
});
