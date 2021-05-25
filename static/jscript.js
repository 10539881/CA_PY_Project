function close_flash_message(){
    document.alertmessage.style.display='none';
    return false;  
}
alert("Hello")
var select = document.getElementById("select"),
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
    alert("hello")
    var today = new Date();
    document.getElementById("date").value = today.getFullYear() + '-' + ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
}
    