const list = document.getElementById("fruitList");

list.addEventListener("click", function(event) {

  if (event.target && event.target.tagName === "LI") {
    console.log("You clicked:", event.target.textContent);
  }
});
