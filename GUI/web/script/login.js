
function lg(){
  name=document.getElementById("nametext").value;
  uname=document.getElementById("unametext").value;
  pwd=document.getElementById("passtext").value;
  console.log(name);
  eel.login(name,uname,pwd)(setImage);
}
function setImage(){
  window.location = "main.html";
}







function validate(){
  name=document.getElementById("nametext").value;
  uname=document.getElementById("unametext").value;
  pwd=document.getElementById("passtext").value;
  if((name.length == 0) && (uname.length == 0) && (pwd.length == 0)){
    return False;
  }else{
    return True;
  }
}
// When user enter query in text box and hits enter
console.log(name);
name.addEventListener("keyup", function(event) {

  if (event.keyCode === 13) {
    event.preventDefault();
    ButtonClicked = false;
    status=validate();
    if(status == True){
      lg();
    }else{
      alert("Details Incomplete");
    }
  }
});

uname.addEventListener("keyup", function(event) {

  if (event.keyCode === 13) {
    event.preventDefault();
    ButtonClicked = false;
    status=validate();
    if(status == True){
      lg();
    }else{
      alert("Details Incomplete");
    }
  }
});
pwd.addEventListener("keyup", function(event) {

  if (event.keyCode === 13) {
    event.preventDefault();
    ButtonClicked = false;
    status=validate();
    if(status == True){
      lg();
    }else{
      alert("Details Incomplete");
    }
  }
});
