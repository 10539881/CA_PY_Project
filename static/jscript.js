

function close_flash_message(){
    document.alertmessage.style.display='none';
    return false;  
}

//this is used by the update.html form in order to hide the form when it's not required.
document.getElementById("showhide").style.display = "none";

var select = document.getElementById("country"),
arr = ["html","css","java","javascript","php","c++","node.js","ASP","JSP","SQL"];

for(var i = 0; i < arr.length; i++)
{
var option = document.createElement("option"),
txt = document.createTextNode(arr[i]);
option.appendChild(txt);
option.setAttribute("value",arr[i]);
select.insertBefore(option,select.lastChild);
}   

createEditableSelect(document.forms[0].myText);

function getDate(){
    var today = new Date();
    document.getElementById("date").value = today.getFullYear() + '-' + ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
}


function checkExists(){
    email = document.getElementById("email").value
    fetch("/checkExists?email=" + email).then(data=>{if(data.exists)
        {document.getElementById("emailexists").innerHTML="Email Exists"}
        else{document.getElementById("emailexists").innerHTML=""}
    })

}

function findStudent(){
    findemail=document.getElementById("findemail").value;
    fetch("/find/student?findemail=")

}

function fillInForm(){
    fetch("/templates/students.json")
        .then(results => results.json())
            .then(data => {document.querySelector("#fname").innerText = data.FirstName})
    }

//this functionality checks the values in the student form and if any are missing it flags them.
/*
$("#student").submit( function(event) {
		
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
    
    }

*/
