function myFunction1() {
    var x = document.getElementById("password");
    if (x.type == "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function myFunction2() {
    var x = document.getElementById("repeatpassword");
    if (x.type == "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function validateForm() {
    var x = document.forms["myForm"]["firstname"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
}