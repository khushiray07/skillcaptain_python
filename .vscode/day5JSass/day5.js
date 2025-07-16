let password = document.getElementById("password");
let confirmPassword = document.getElementById("confirmPassword");
let submit= document.getElementById("contactForm");
let status = document.getElementById("status");

submit.addEventListener("submit", function(e){
    e.preventDefault();
    if (password.value === confirmPassword.value) {
        status.innerText = "Passwords match!";
        status.style.color = "green";


    } else {
        status.innerText = "Passwords do not match!";
        status.style.color = "red";
    }


})
    