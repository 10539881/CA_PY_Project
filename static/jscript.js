
fetch("http://127.0.0.1:5000/static/students.json")
    .then(results => results.json())
        .then(data => {
            document.querySelector("#fname").value = data.FirstName
            document.querySelector("#lname").value = data.LastName
            document.querySelector("#dob").value = data.DOB
            document.querySelector("#country").value = data.Country
            document.querySelector("#mobile").value = data.Mobile
            document.querySelector("#email").value = data.Email
            document.querySelector("#course").value = data.Course})


function checkExists(){
    email = document.getElementById("email").value
    fetch("/checkExists?email=" + email).then(data=>{if(data.exists)
        {document.getElementById("emailexists").innerHTML="Email Exists"}
        else{document.getElementById("emailexists").innerHTML=""}
    })

}


    

