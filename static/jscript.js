//alert("hello world!!!!!")
/*I left the code in below, however I wasn't able to get any of it to work, instead I placed the code within <script> tags on the individual pages to show how it worked, 
but I realise it all should be contained within this file.*/

/*
fetch("static/students.json", {cache: "no-store"})
.then(results => results.json())
.then(data => {  
document.querySelector("#fname").value = data.FirstName
document.querySelector("#lname").value = data.LastName
document.querySelector("#dob").value = data.DOB
document.querySelector("#country").value = data.Country
document.querySelector("#mobile").value = data.Mobile
document.querySelector("#email").value = data.Email
document.querySelector("#course").value = data.Course})


this functionality was designed to dispaly the current date in the DOB text box
var date = new Date();
var year = date.getFullYear();
var month= date.getMonth() +1;
var today = date.getDate();
var datePattern = today + '-' + month + '-' + year;
document.getElementById("dob").value = datePattern;
*/

/*
function checkExists(){
    email = document.getElementById("email").value
    fetch("/checkExists?email=" + email).then(data=>{if(data.exists)
        {document.getElementById("emailexists").innerHTML="Email Exists"}
        else{document.getElementById("emailexists").innerHTML=""}
    })

}

//this code is used to today's date to the DOB field; however the code doesn't fire and therefore, a null value remains in the date field. It has been replaced by a static date.
let date = new Date();
let year = date.getFullYear();
let month= date.getMonth() +1;
let todayDate = string(date.getDate()).padStart(2,'0');
let datePattern = year +'-'+ month + '-' + todayDate;
document.getElementById('dob').value = datePattern;

//this functionality checks the values in the student form and if any are missing it flags them.
$("#form").submit( function(event) {
        
    var found_error = false;
    var error_amount = 0;
    var fname = $("#fname").val();
    if(fname == ""){
        $("input#fname").css("border-color", "#ff3333");
        found_error = true;
        error_amount += 1;
    }
    var lname = $("#lname").val();
    if(lname == ""){
        $("input#lname").css("border-color", "#ff3333");
        found_error = true;
        error_amount += 1;
    }
    var dob = $("#dob").val();
    if(dob == ""){
        $("input#dob").css("border-color", "#ff3333");
        found_error = true;
        error_amount += 1;
    }
    var country = $("#country").val();
    if(country == ""){
        $("input#country").css("border-color", "#ff3333");
        found_error = true;
        error_amount += 1;
    }
    var mobile = $("#mobile").val();
    if(mobile == ""){
        $("input#mobile").css("border-color", "#ff3333");
        found_error = true;
        error_amount += 1;
    }
    var email = $("#email").val();
    if(email == ""){
        $("input#email").css("border-color", "#ff3333");
        found_error = true;
        error_amount += 1;
    }
    var course = $("#course").val();
    if(course == ""){
        $("input#course").css("border-color", "#ff3333");
        found_error = true;
        error_amount += 1;
    }
//if any errors are found this is highlighted on the page and the page is prevented from being submitted
    if (found_error == true){
        $("span#error-count").text(error_amount);
        $("p#error-list").css("display", "block");
        event.preventDefault();
    
    }})
    */