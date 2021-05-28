

function close_flash_message(){ //function to close button created by the flash messages.
    document.alertmessage.style.display='none';
    return false;  
}

//this is used by the update.html form in order to hide the form when it's not required.
document.getElementById("showhide").style.display = "none";

var select = document.getElementById("country"),
var arr = ["Afghanistan","Australia","Bangladesh","Belgium", "Brazil",'Burkina Faso','Burundi','Cambodia','Canada','Chad','Chile','China','Christmas Island','Cocos (Keeling) Islands','Colombia','Comoros','Congo','Cook Islands','Costa Rica','Croatia','Cuba','Cyprus','Czechia','Denmark','Djibouti','Dominica','Dominican Republic','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Falkland Islands (Malvinas)','Faroe Islands','Fiji','Finland','France','French Guiana','French Polynesia','French Southern Territories','Gabon','Gambia','Georgia','Germany','Ghana','Gibraltar','Greece','Greenland','Grenada','Guadeloupe','Guam','Guatemala','Guernsey','Guinea','Guinea-bissau','Guyana','Haiti','Heard Island and Mcdonald Islands','Holy See (Vatican City State)','Honduras','Hong Kong','Hungary','Iceland','India','Indonesia','Iran Islamic Republic of','Iraq','Ireland','Isle of Man','Israel','Italy','Jamaica','Japan','Jersey','Jordan','Kazakhstan','Kenya','Kiribati','Korea','Kuwait','Kyrgyzstan','Latvia','Lebanon','Lesotho','Liberia','Libyan Arab Jamahiriya','Liechtenstein','Lithuania','Luxembourg','Macao','Macedonia The Former Yugoslav Republic of','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Martinique','Mauritania','Mauritius','Mayotte','Mexico','Micronesia Federated States of','Moldova Republic of','Monaco','Mongolia','Montenegro','Montserrat','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','Netherlands Antilles','New Caledonia','New Zealand','Nicaragua','Niger','Nigeria','Niue','Norfolk Island','Northern Mariana Islands','Norway','Oman','Pakistan','Palau','Palestinian Territory Occupied','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Pitcairn','Poland','Portugal','Puerto Rico','Qatar','Reunion','Romania','Russian Federation','Rwanda','Saint Helena','Saint Kitts and Nevis','Saint Lucia','Saint Pierre and Miquelon','Saint Vincent and The Grenadines','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Georgia and The South Sandwich Islands','Spain','Sri Lanka','Sudan','Suriname','Svalbard and Jan Mayen','Swaziland','Sweden','Switzerland','Syrian Arab Republic','Taiwan Province of China','Tajikistan','Tanzania United Republic of','Thailand','Timor-leste','Togo','Tokelau','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Turks and Caicos Islands','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','United States Minor Outlying Islands','Uruguay','Uzbekistan','Vanuatu','Venezuela','Viet Nam','Virgin Islands British','Virgin Islands U.S.','Wallis and Futuna','Western Sahara','Yemen','Zambia','Zimbabwe'];

for(var i = 0; i < arr.length; i++)
{
var option = document.createElement("option"),
txt = document.createTextNode(arr[i]);
option.appendChild(txt);
option.setAttribute("value", arr[i]);
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
