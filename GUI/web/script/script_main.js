
var lastSentMessage = "";
var lastRecievedMessage = 1;
var ButtonClicked = false;

var action_email_reciever_flag=false;
var action_email_subject_flag=false;
var action_email_message_flag=false;
var action_email_confirm_flag=false;
var email_reciever=""
var email_subject=""
var email_message=""

var notes_insert_flag=false;
var notes_remove_flag=false;
var notes_message="";
var notes_position=0;

var action_file_organizer_flag=false;
var action_file_organizer_index=0;

var python_module_forward=false;

var DEFAULT_TIME_DELAY = 3000;
//keypress enter for messages
var input = document.getElementById("textarea");
var rec_icon = document.getElementById("rec");
var chatbx=document.getElementById("chat-window");
var loader_icon=document.getElementById("loadingGif");


// This is for saying Hello First Name
addname()
function addname(){
  eel.get_name()(backvalue)
}
function backvalue(r){
  var putname = document.getElementById("put_name");
  console.log(r);
  putname.innerHTML += "Hello "+r;
  showLoading();

  // After 3 seconds call the createNewMessage function
  setTimeout(function() {
    eel.voice_output("How can I help you?");
    createNewMessage("How can I help you?");
  }, 800);
}

// When user enter query in text box and hits enter
input.addEventListener("keyup", function(event) {

  if (event.keyCode === 13) {
    event.preventDefault();
    ButtonClicked = false;
    if(action_email_reciever_flag == true){
      action_email_reciever_flag=false;
      action_email_subject_flag=true;
      email_reciever=input.value;
      user_query(input.value);//user reply
      createNewMessage("What is the subject ? ");//chatbot reply
      eel.voice_output("What is the subject ? ");//chatbot voice
    }else if (action_email_subject_flag == true) {
      action_email_subject_flag=false;
      action_email_message_flag=true;
      email_subject=input.value;
      user_query(input.value);
      createNewMessage("What is the Message ? ");
      eel.voice_output("What is the Message ? ");
    }else if (action_email_message_flag == true) {
      action_email_message_flag=false;
      action_email_confirm_flag=true;
      email_message=input.value;
      user_query(input.value);
      createNewMessage("Is this the message you want to send");
      eel.voice_output("Is this the message you want to send");
      createNewMessage("To : "+email_reciever);
      createNewMessage("Subject : "+email_subject);
      createNewMessage("Message: "+email_message);
      createNewMessage("yes/no ?");
    }else if (action_email_confirm_flag == true) {
      action_email_confirm_flag=false;
      user_confirm = input.value.trim();
      user_query(user_confirm);
      console.log(user_confirm+":output ");
      if(user_confirm === "yes"){
        console.log("starting to send mail");
        eel.send_email(email_reciever,email_subject,email_message)
      }else{
        console.log("cancel send mail");
        eel.voice_output("Email Cancelled ");
      }

    }else if (notes_insert_flag == true) {
      notes_insert_flag=false;
      notes_message=input.value;
      user_query(input.value);
      insert_notes(notes_message);
    }else if (notes_remove_flag == true) {
      notes_remove_flag=false;
      notes_position=input.value;
      user_query(input.value);
      remove_note(notes_position);
    }else if(action_file_organizer_flag==true){
      action_file_organizer_flag=false;
      console.log('sadasd')
      action_file_organizer_index=input.value;
      console.log(action_file_organizer_index)
      eel.file_organize(action_file_organizer_index);

    }else if (python_module_forward == true) {
      console.log(input.value.trim() == 'deactivate')
      if(input.value.trim() === 'deactivate'){
        user_query(input.value);
        eel.python_deactivate()(deactivated)
      }else{

        user_query(input.value);
        eel.request_python_module(input.value)(python_response)}
    }else{
      send(input.value);
    }


    input.rows=1;
    input.value = "";

  }
});

//This is for Recording icon


rec_icon.addEventListener("click",function(event){

  console.log(rec_icon);
  rec_icon.src="Images/microphoneoff.png";
  console.log(rec_icon);
  requestAnimationFrame(() => {
      setTimeout(voice_get, 0, rec_icon);
  });



});
function voice_get(){
  eel.voice_input()(callBack)
}
function callBack(result){
  //rec_icon.src="Images/microphone.png"
  console.log(result);
  if(action_email_reciever_flag == true){
    action_email_reciever_flag=false;
    action_email_subject_flag=true;
    email_reciever=result;
    user_query(result);
    createNewMessage("What is the subject ? ");
    eel.voice_output("What is the subject ? ");
  }else if (action_email_subject_flag == true) {
    action_email_subject_flag=false;
    action_email_message_flag=true;
    email_subject=result;
    user_query(result);
    createNewMessage("What is the Message ? ");
    eel.voice_output("What is the Message ? ");
  }else if (action_email_message_flag == true) {
    action_email_message_flag=false;
    action_email_confirm_flag=true;
    email_message=result;
    user_query(result);
    createNewMessage("Is this the message you want to send");
    eel.voice_output("Is this the message you want to send");
    createNewMessage("To : "+email_reciever);
    createNewMessage("Subject : "+email_subject);
    createNewMessage("Message: "+email_message);
    createNewMessage("yes/no ?");
  }else if (action_email_confirm_flag == true) {
    action_email_confirm_flag=false;
    user_confirm = result;
    user_query(user_confirm);
    console.log(user_confirm+":output ");
    if(user_confirm === "yes"){
      console.log("starting to send mail");
      eel.send_email(email_reciever,email_subject,email_message)
    }else{
      console.log("cancel send mail");
      eel.voice_output("Email Cancelled ");
    }

  }else if (notes_insert_flag == true) {
    notes_insert_flag=false;
    notes_message=result;
    user_query(result);
    insert_notes(notes_message);
  }else if (notes_remove_flag == true) {
    notes_remove_flag=false;
    notes_position=result;
    user_query(result);
    remove_note(notes_position);
  }else if (python_module_forward == true) {
    if(result.trim() === 'deactivate'){
      user_query(result);
      eel.python_deactivate()(deactivated)
    }
    else{
      user_query(result);
      eel.request_python_module(result)(python_response)
      showLoading();
    }

  }else{
    if(result=='None'){
        voice_get();
    }else{
      send(result);
      //rec_icon.src="Images/microphone.png"
    }
  }
}

function python_response(response){
  showLoading();
  setTimeout(function() {
    hideLoading();
    createNewbreaklineMessage(response)
  }, 500);


}

function user_query(text){
  var div_temp = document.createElement('div');
  div_temp.classList.add("chat");
  div_temp.classList.add("self");
  var p = document.createElement("p");
  p.classList.add("chat-message");                // Create a <h1> element
  var t = document.createTextNode(text);
  p.appendChild(t);
  div_temp.appendChild(p);


  chatbx.appendChild(div_temp);
}

//This is for getting the response from the chabot
function send(text) {

  user_query(text);

	// Create a div with the text that the user typed in

	// Find the last message in the chatlogs
	var $sentMessage =document.querySelectorAll(".chat:last-child");


	// Check to see if that message is visible
	checkVisibility($sentMessage);

	// update the last message sent variable to be stored in the database and store in database
	lastSentMessage = text;
	storeMessageToDB();


	// AJAX post request, sends the users text to API.AI and
	// calls the method newReceivedMessage with the response from API.AI
  eel.response_get(text)(resp);


}
async function resp(result){
  showLoading();
  if(result.split("#")[0] == 'weather_result_output'){
    console.log('Got weather');
    degree=result.split("#")[1];
    desp_main=result.split("#")[4];
    loc=result.split("#")[3];
    console.log(degree);
    console.log(desp_main);
    console.log(loc);
    setTimeout(function() {
      hideLoading();
      weathercard(degree,desp_main,loc);
    }, 1000);


  }else if (result.split("#")[0] == 'image_search_output'){
    console.log('Got image');
    imglinks=result.split("#");
    setTimeout(function() {
      hideLoading();
      imagecard(imglinks[1],imglinks[2],imglinks[3],imglinks[4]);
    }, 1000);


  }else if (result.split("#")[0] == 'email_send_flag'){
    console.log('Got mail');
    createNewMessage("Who do you want to send the Email ? ");
    eel.voice_output("Who do you want to send the Email ? ");
    action_email_reciever_flag=true

  }else if (result.split("#")[0] == 'notes_insert_output'){
    console.log('add note');
    createNewMessage("What do you want to note ? ");
    eel.voice_output("What do you want to note ? ");
    notes_insert_flag=true


  }else if (result.split("#")[0] == 'notes_remove_output'){
    console.log('remove note');
    createNewMessage("Which note do you want to remove ? ");
    eel.voice_output("Which note do you want to remove ? ");
    notes_remove_flag=true


  }else if (result.split("#")[0] == 'notes_show_output'){
    console.log('Got notes');
    show_notes();


  }else if (result.split("#")[0] == 'youtube_show_output'){
    console.log('Openning Youtube');
    hideLoading();


  }else if (result.split("#")[0] == 'python_mode_activate'){
    console.log('Python mode started');
    eel.python_activate()(activated)



  }else if (result.split("#")[0] == 'show_news_output'){
    console.log('showing news');
    setTimeout(function() {
      eel.news_get()(news);
    }, 1000);


  }else if (result.split("#")[0] == 'volume_up'){
    console.log('volume up');
    eel.volumeup();
    hideLoading();


  }else if (result.split("#")[0] == 'volume_down'){
    console.log('volume down');
    eel.volumedown();
    hideLoading();


  }
  else if (result.split("#")[0] == 'volume_max'){
    console.log('volume max');
    eel.volumemax();
    hideLoading();


  }
  else if (result.split("#")[0] == 'notepad_write_module'){
    console.log('note_writer');
    eel.note_writer();
    hideLoading();


  }else if (result.split("#")[0] == 'volume_mute'){
    console.log('volume mute');
    eel.volumemute();
    hideLoading();


  }else if (result.split("#")[0] == 'show_covid_stat'){
    console.log('showing covid stats');
    setTimeout(function() {
      hideLoading();
      eel.put_covid_total_stats()(cov_data);
      eel.put_covid_state_stats()(cov_data);
    }, 2000);


  }else if(result.split("#")[0] == 'File_organiser'){
    setTimeout(function() {
      hideLoading();
      createNewMessage("Select the folder in which you want to organize ");
      eel.voice_output("Select the folder in which you want to organize");

      createNewMessage("1. Documents")
      createNewMessage("2. Downloads")
      createNewMessage("3. Desktop")
      createNewMessage("4. test")

      action_file_organizer_flag=true;

    }, DEFAULT_TIME_DELAY);
  }else if(result.split("#")[0] == 'features'){
    setTimeout(function() {
      createNewbreaklineMessage(result.split("#")[1]);
      eel.voice_output("My features are")
    }, 1000);
  }else{
    console.log(result);
    // After 3 seconds call the createNewMessage function
    setTimeout(function() {
      createNewMessage(result);
      eel.voice_output(result)
    }, 1500);

  }

}
function doactioncheck() {
  return new Promise((resolve,reject) => {
    console.log("doing action variable check");
    if(actionreturn == "") {//we want it to match
        setTimeout(doactioncheck, 50);//wait 50 millisecnds then recheck
        return;
    }
  });

}

function activated(result){
  python_module_forward=true;
  hideLoading();
}

function deactivated(result){
  python_module_forward=false;
  hideLoading();
}
//news card
function news(output){
  output=output.split('#');
  div_main=document.createElement('div');
  div_main.classList.add("chat");
  div_main.classList.add("friend");
  div_main.classList.add("news_container");

  div_header=document.createElement('div');
  div_header.classList.add("news_header");
  elem_header=document.createElement('h2');
  headertext=document.createTextNode("Latest News");
  elem_header.appendChild(headertext);
  div_header.appendChild(elem_header);
  div_main.appendChild(div_header);


  output.forEach(function(content){
    content=content.split('||');
    title=content[0];
    link=content[1];
    anchor=document.createElement('A');
    anchor.href=link;
    text=document.createTextNode(title);
    anchor.appendChild(text);
    div_main.appendChild(anchor);
  });
  hideLoading();
  chatbx.appendChild(div_main);


}

// covid data

//news card
function cov_data(output){
  output=output.split('#');
  div_main=document.createElement('div');
  div_main.classList.add("chat");
  div_main.classList.add("friend");
  div_main.classList.add("covid_container");

  div_header=document.createElement('div');
  div_header.classList.add("covid_header");
  elem_header=document.createElement('h2');
  headertext=document.createTextNode(output[0]);
  elem_header.appendChild(headertext);
  div_header.appendChild(elem_header);
  div_main.appendChild(div_header);

  div_body=document.createElement('div');

  div_body_c1=document.createElement('div');
  div_body_c1.classList.add("stats_div_recov");
  div_body_c1.classList.add("stats");
  text1=document.createElement("p");
  text_value1=document.createTextNode("Recovered");
  h1=document.createElement("h1");
  h_value1=document.createTextNode(output[1]);

  div_body_c2=document.createElement('div');
  div_body_c2.classList.add("stats_div_confirm");
  div_body_c2.classList.add("stats");
  text2=document.createElement("p");
  text_value2=document.createTextNode("Confirmed");
  h2=document.createElement("h1");
  h_value2=document.createTextNode(output[2]);

  div_body_c3=document.createElement('div');
  div_body_c3.classList.add("stats_div_death");
  div_body_c3.classList.add("stats");
  text3=document.createElement("p");
  text_value3=document.createTextNode("Deaths");
  h3=document.createElement("h1");
  h_value3=document.createTextNode(output[3]);

  h1.appendChild(h_value1);
  text1.appendChild(text_value1);
  div_body_c1.appendChild(text1);
  div_body_c1.appendChild(h1);

  h2.appendChild(h_value2);
  text2.appendChild(text_value2);
  div_body_c2.appendChild(text2);
  div_body_c2.appendChild(h2);

  h3.appendChild(h_value3);
  text3.appendChild(text_value3);
  div_body_c3.appendChild(text3);
  div_body_c3.appendChild(h3);

  div_body.appendChild(div_body_c1);
  div_body.appendChild(div_body_c2);
  div_body.appendChild(div_body_c3);

  div_main.appendChild(div_body);


  chatbx.appendChild(div_main);


}

//weather card

function weathercard(temp,desp,loc){
  div_main=document.createElement('div');
  div_main.classList.add("chat");
  div_main.classList.add("friend");

  weatherbox_div=document.createElement('div')
  div_main.classList.add("weatherbox");

  icon = new Image();
  if((desp == 'Rain')||(desp == 'Drizzle')) {
    icon.src = "Images/rainy.gif";
    div_main.classList.add("rain");
  }else if (desp == 'Thunderstorm') {
    icon.src = "Images/thunderstorm.gif";
    div_main.classList.add("thunder");
  }else if (desp == 'Clear') {
    icon.src = "Images/sunny.gif";
    div_main.classList.add("sun");
  }else if (desp == 'Clouds') {
    icon.src = "Images/cloudy.gif";
    div_main.classList.add("cloud");
  }



  weatherchild_1=document.createElement('div');
  weatherchild_1.classList.add("weatherchild");

  weather_gif=document.createElement('div');
  weather_gif.classList.add("weathergif");


  temperature=document.createElement('div');
  temperature.classList.add("temp_div");
  value_span = document.createElement("SPAN");
  value = document.createTextNode(temp);
  value_span.classList.add("temper");
  degree_span=document.createElement("SPAN");
  degree=document.createTextNode("\u2103");

  weatherchild_2=document.createElement('div');
  weatherchild_2.classList.add("weatherchild");

  weather_climate=document.createElement('div');
  weather_climate.classList.add("weather_climate");
  text1=document.createElement("p");
  text_value1=document.createTextNode("now in");
  text2=document.createElement("p");
  text_value2=document.createTextNode(loc);
  text3=document.createElement("p");
  text3.classList.add("loc");
  text_value3=document.createTextNode(desp);

  text3.appendChild(text_value3);
  text2.appendChild(text_value2);
  text1.appendChild(text_value1);
  weather_climate.appendChild(text1);
  weather_climate.appendChild(text2);
  weather_climate.appendChild(text3);
  weatherchild_2.appendChild(weather_climate);

  value_span.appendChild(value);
  degree_span.appendChild(degree);
  temperature.appendChild(value_span);
  temperature.appendChild(degree_span);
  weather_gif.appendChild(icon);
  weatherchild_1.appendChild(weather_gif);
  weatherchild_1.appendChild(temperature);

  weatherbox_div.appendChild(weatherchild_1);
  weatherbox_div.appendChild(weatherchild_2);

  div_main.appendChild(weatherbox_div);
  console.log(div_main);

  chatbx.appendChild(div_main);

}


// image card
function imagecard(link1,link2,link3,link4){
  div_main=document.createElement('div');
  div_main.classList.add("chat");
  div_main.classList.add("friend");
  div_main.classList.add("images_container");

  img_div1=document.createElement('div');
  img_div1.classList.add("divSquare");
  img1 = new Image();
  img1.src=link1;


  img_div2=document.createElement('div');
  img_div2.classList.add("divSquare");
  img2 = new Image();
  img2.src=link2;

  div_mid=document.createElement('div');
  div_mid.style.clear='both';

  img_div3=document.createElement('div');
  img_div3.classList.add("divSquare");
  img3 = new Image();
  img3.src=link3;

  img_div4=document.createElement('div');
  img_div4.classList.add("divSquare");
  img4 = new Image();
  img4.src=link4;

  img_div1.appendChild(img1);
  img_div2.appendChild(img2);
  img_div3.appendChild(img3);
  img_div4.appendChild(img4);

  div_main.appendChild(img_div1);
  div_main.appendChild(img_div2);
  div_main.appendChild(div_mid);
  div_main.appendChild(img_div3);
  div_main.appendChild(img_div4);

  chatbx.appendChild(div_main);


}

//Notes
function insert_notes(message){
  eel.notes_insert(message)
  hideLoading();
}
function remove_note(position){
  eel.remove_notes(position)
  hideLoading();
}
function show_notes(){
  eel.print_notes()(note_output)
  hideLoading();
}
function note_output(result){
  console.log(result);
  if(result != "none"){
    notes=result.split("#");

    div_main=document.createElement('div');
    div_main.classList.add("chat");
    div_main.classList.add("friend");
    div_main.classList.add("note_container");

    div_header=document.createElement('div');
    div_header.classList.add("notes_header");
    elem_header=document.createElement('h2');
    headertext=document.createTextNode("Notes");
    elem_header.appendChild(headertext);
    div_header.appendChild(elem_header);
    div_main.appendChild(div_header);

    ord_list=document.createElement('ol');

    notes.forEach(function(note){

      list_elem=document.createElement('li');
      list_elem.innerHTML=note;
      ord_list.appendChild(list_elem);
      br=document.createElement('br');
      ord_list.appendChild(br);
    });
    div_main.appendChild(ord_list);
    showLoading();
    setTimeout(function() {
      hideLoading();
      chatbx.appendChild(div_main);
    }, 3000);

  }


}







// Method to create a new div showing the text from API.AI
function createNewMessage(message) {

	// Hide the typing indicator


  var div_temp = document.createElement('div');
  div_temp.classList.add("chat");
  div_temp.classList.add("friend");
  var img_div = document.createElement("div");
  img_div.classList.add("user-photo");
  var img = new Image();
  img.src = "Images/ana.JPG";
  img_div.appendChild(img);
  div_temp.appendChild(img_div);
  var p = document.createElement("p");
  p.classList.add("chat-message");                // Create a <h1> element
  var t = document.createTextNode(message);
  p.appendChild(t);
  div_temp.appendChild(p);

  hideLoading();

  chatbx.appendChild(div_temp);



	// Find the last message in the chatlogs
  var $sentMessage = document.querySelectorAll(".chat:last-child");

  // Check to see if that message is visible
  checkVisibility($sentMessage);
}
function createNewbreaklineMessage(message) {

	// Hide the typing indicator


  var div_temp = document.createElement('div');
  div_temp.classList.add("chat");
  div_temp.classList.add("friend");
  var img_div = document.createElement("div");
  img_div.classList.add("user-photo");
  var img = new Image();
  img.src = "Images/ana.JPG";
  img_div.appendChild(img);
  div_temp.appendChild(img_div);
  var p = document.createElement("p");
  p.classList.add("chat-message");                // Create a <h1> element
  //var t = document.createTextNode(message);
  //p.appendChild(t);
  p.innerHTML=message;
  div_temp.appendChild(p);

  hideLoading();

  chatbx.appendChild(div_temp);

	// take the message and say it back to the user.
	//speechResponse(message);

	// // Show the send button and the text area
	// $('#rec').css('visibility', 'visible');
	// $('textarea').css('visibility', 'visible');

	// Append a new div to the chatlogs body, with an image and the text from API.AI

	// Find the last message in the chatlogs
  var $sentMessage = document.querySelectorAll(".chat:last-child");

  // Check to see if that message is visible
  checkVisibility($sentMessage);
}




function storeMessageToDB() {

 //pass;

}

// Funtion which shows the typing indicator
// As well as hides the textarea and send button
function showLoading()
{
  chatbx.appendChild(loader_icon);

	$("#loadingGif").show();

	// $('#rec').css('visibility', 'hidden');
	// $('textarea').css('visibility', 'hidden');

	$('.chat-form').css('visibility', 'hidden');

 }




// Function which hides the typing indicator
function hideLoading()
{
  rec_icon.src="Images/microphone.png"
	$('.chat-form').css('visibility', 'visible');
	$("#loadingGif").hide();

	// Clear the text area of text
	$(".input").val("");

	// reset the size of the text area
	$(".input").attr("rows", "1");

}



// Method which checks to see if a message is in visible
function checkVisibility(message)
{
  var prev= document.querySelectorAll(".chat:last-child");
	// Scroll the view down a certain amount
  console.log("prev");
  console.log(prev);
  $chatlogs=".chatlogs"
  var position = prev[0].offsetTop
                - $('.chatlogs').offset().top
                + $('.chatlogs').scrollTop();
	$('.chatlogs').stop().animate({scrollTop: position});
}





//----------------------------------------- Resize the textarea ------------------------------------------//
$(document)
    .one('focus.input', 'textarea.input', function(){
        var savedValue = this.value;
        this.value = '';
        this.baseScrollHeight = this.scrollHeight;
        this.value = savedValue;
    })
    .on('input.input', 'textarea.input', function(){
        var minRows = this.getAttribute('data-min-rows')|0, rows;
        this.rows = minRows;
        rows = Math.ceil((this.scrollHeight - this.baseScrollHeight) / 17);
        this.rows = minRows + rows;
	});
