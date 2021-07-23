from __future__ import unicode_literals
import eel
import pyautogui
import notes_driver as notes
import weather_class as wc
import Voice_Assistant as VA
import speech_recognition as sr
from mail_driver import send_mail_driver
from input_module import get_input,put_output
from news import News
from covid_statistics import COVID
from write_driver import Notepad_Driver
from pywinauto import application
from file_organizer_class import file_organizer
from Fasttext_python import fasttext_QA






eel.init('GUI/web')
fullname=''
firstname=''
email_username=''
email_password=''
notes_list=[]

weather_obj =wc.weather()
mail_obj=send_mail_driver()

py_obj=None

@eel.expose
def login(name, uname, pwd):
    global firstname
    global fullname
    global email_username
    global email_password
    firstname=name.split()[0].lower().capitalize()
    fullname=name
    email_username=uname
    email_password=pwd
    print(name, uname, pwd)

@eel.expose
def note_writer():
    app = application.Application()
    r = sr.Recognizer()
    obj = Notepad_Driver()
    obj.open_win(app)

    with sr.Microphone(device_index=1) as mic:
        while True:
            r.adjust_for_ambient_noise(mic, duration=0.2)
            audio = r.listen(mic)
            try:
                result = r.recognize_google(audio).lower()
                print("You said " + result)
                words = result.lower()
                if words == "exit":
                    obj.save_win("pibot_notepad.txt",app)
                    break
                else:
                    words = words + " "
                    obj.write_win(words, app)
                    # obj.write_win(" ", app)
            except LookupError:
                print("Please, speak more clearly")


@eel.expose
def get_name():
    global firstname
    print(firstname)
    return firstname

@eel.expose
def request_python_module(request):
    global py_obj
    captured = py_obj.get_answer(request)
    return captured


@eel.expose
def python_activate():
    global py_obj
    tmp=fasttext_QA()
    tmp.load_model()
    py_obj=tmp
    put_output("Python Mode Activated")

@eel.expose
def python_deactivate():
    global py_obj
    py_obj=None
    put_output("Deactivated python mode")
    print("------------------>>Deactivated<<--------------------")


@eel.expose
def response_get(text):
    val=VA.request_response(text)
    print('->',val)
    return val

@eel.expose
def file_organize(pos):
    print(pos)
    obj1=file_organizer(pos)
    obj1.organize()
    put_output('Files are organized ')

@eel.expose
def news_get():
    news=News()
    news_str=news.gettop5()
    put_output("Top 5 latest news are")
    return news_str

cov = COVID()
@eel.expose
def put_covid_total_stats():
    global cov
    return "Total#"+cov.gettotal()

@eel.expose
def put_covid_state_stats():
    global cov
    return "State#"+cov.getstate()

@eel.expose
def voice_input():
    return get_input()
@eel.expose
def volumeup():
    pyautogui.press("volumeup")
@eel.expose
def volumemax():
    i=0
    while(i<10):
        pyautogui.press("volumeup",presses=10)
        i+=1
@eel.expose
def volumedown():
    pyautogui.press("volumedown")
@eel.expose
def volumemute():
    pyautogui.press("volumemute")


@eel.expose
def voice_output(text):
    put_output(text)




@eel.expose
def notes_insert(message):
    global notes_list
    if(len(notes_list) <10):
        notes.add_todo(message,notes_list)
        put_output("Successfully added to Notes")
    else:
        put_output("Maximum notes limit reached.")

@eel.expose
def print_notes():
    global notes_list
    if(len(notes_list) != 0):
        put_output("Here is your notes")
        return notes.show_todo(notes_list)
    else:
        put_output("No notes available")
        return None

@eel.expose
def remove_notes(position):
    global notes_list
    if (len(notes_list) > 0):
        if ('one' in position) or ('1' in position) or ('first' in position):
            position=1
        elif ('two' in position) or ('2' in position) or ('second' in position):
            position=2
        elif ('three' in position) or ('3' in position) or ('third' in position):
            position=3
        elif ('four' in position) or ('4' in position) or ('fourth' in position):
            position=4
        elif ('five' in position) or ('5' in position) or ('fifth' in position):
            position=5
        elif ('six' in position) or ('6' in position) or ('sixth' in position):
            position=6
        elif ('seven' in position) or ('7' in position) or ('seventh' in position):
            position=7
        elif ('eight' in position) or ('8' in position) or ('eighth' in position):
            position=8
        elif ('nine' in position) or ('9' in position) or ('ninth' in position):
            position=9

        try:
            print(position)
            print(type(position))
            notes.remove_todo(position,notes_list)
            put_output("successfully removed the note")
        except Exception as E:
            print(E)
            put_output("Some Error occured")
    else:
        put_output("No note to remove")


@eel.expose
def weather_getter():
    print("Fetching weather")
    weather_obj.get_city()
    weat=['weather_result_output',weather_obj.Temperature(),weather_obj.Weather_desc(),weather_obj.city_print(),weather_obj.weathermain()]
    weat=' '.join(weat)
    eel.fetch_weather(weat)

@eel.expose
def send_email(reciever,subject,message):
    global email_username
    global email_password
    mail_obj.credentials(email_username,email_password)
    status=mail_obj.send(reciever,subject,message)
    if(status[0] == 0):
        print(status[1])
        put_output("Some Error Occured")
    else:
        put_output(status[1])


eel.start('index.html',size=(1000,1450))