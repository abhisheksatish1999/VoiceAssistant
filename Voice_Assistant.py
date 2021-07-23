from neuralintents import GenericAssistant
import sys
import re
from input_module import put_output
from weather_class import weather
from image_searcher import image_search
from yt_player import player



class Generic_Assistant_mod(GenericAssistant):
    def __init__(self, *args, **kwargs):
        super(Generic_Assistant_mod, self).__init__(*args, **kwargs)
    def request(self,message):
        ints = self._predict_class(message)

        if ints[0]['intent'] in self.intent_methods.keys():
            #print(self.intent_methods[ints[0]['intent']])
             return self.intent_methods[ints[0]['intent']](message)
        else:
            ans=self._get_response(ints, self.intents)
            return ans


weather_obj =weather()
def get_weather(message):
    weather_obj.get_city()
    weat=['weather_result_output',weather_obj.Temperature(),weather_obj.Weather_desc(),weather_obj.city_print(),weather_obj.weathermain()]
    weat='#'.join(weat)
    return weat






def get_image(query):
    inp=re.findall("image of(.*)",query)
    if(len(inp)==0):
        inp=re.findall("images of(.*)",query)
    imgsrch = image_search(inp[0])
    imglinks=imgsrch.search_now()
    imglinks='image_search_output#'+imglinks
    return imglinks

def email_sender(message):
    return 'email_send_flag'


def add_note(message):
    return "notes_insert_output"
def remove_note(message):
    return "notes_remove_output"
def show_note(message):
    return "notes_show_output"

def python_module(message):
    return "python_mode_activate"

def play_youtube(message):
    message=message.lower()
    if("pybot" in message):
        message=message.replace("pybot","")
    if ("pibot" in message):
        message = message.replace("pibot", "")
    message=message.strip()
    if(message.startswith("play")):
        message=message.replace("play","",1)
    elif(message.startswith("open youtube and play")):
        message=message.replace("open youtube and play", "", 1)
    message = message.strip()
    if (message.endswith("on youtube")):
        message=message.replace("on youtube", "")
    message = message.strip()
    print(message)

    yt=player(message)
    yt.search_video()
    return "youtube_show_output"




def features(message):
    return "features#I can help you with :-<br /> 1. python_module : Used to help with python based questions and problems. <br /> 2. Weather : Will show the current weather and temperature from the system. <br /> 3. show_images : By this command I will collect and display the image requested by the user. <br /> 4. add_notes : You can add notes to the existing note file. <br /> 5. show_notes : I can display you the requested note files. <br /> 6. remove_notes : You can delete the specified notes. <br /> 7. note_writer : You can open the note writer and can write note by reciting the desired words and the I will type for you. <br /> 8. get_news : I can give you the latest news from the internet. <br /> 9. youtube_player : You can request for a video and I can open the video in the browser for you. <br /> 10. covid_stat : By this command I can display you the Covid Statistics of India and your current state. <br />  11. email : I can compose an Email and send to the requested receiver <br />  12. vol_up : I can increase the level of the system volume. <br />  13. vol_down : I can decrease the level of the system volume. <br />  14. vol_max : I can set the system volume to the maximum level. <br />  15. vol_mute : I can set the system volume to the minimum level. <br /> 16. file_organizer : This command will hlp to organise files of the given directory according to the file type <br /> 17. exit : By this command I will terminate myself. "
#def hello(message):
#    speaker.say("Hello,What can I do for you?")
#    speaker.runAndWait()

def quit(message):
    put_output(" See you later. Goodbye")
    sys.exit(0)

def volumeup(message):
    return "volume_up"

def volumemax(message):
    return "volume_max"

def volumedown(message):
    return "volume_down"

def volumemute(message):
    return "volume_mute"

def organize(message):
    return "File_organiser"

def news_getter(message):
    return "show_news_output"

def covid_stat(message):
    return "show_covid_stat"
def note_write(message):
    return "notepad_write_module"


mappings = {
            "exit" : quit,
            "Weather" :get_weather,
            "show_images":get_image,
            "add_notes":add_note,
            "show_notes":show_note,
            "remove_notes":remove_note,
            "get_news":news_getter,
            "youtube_player":play_youtube,
            "covid_stat":covid_stat,
            "email":email_sender,
            "vol_up":volumeup,
            "bot_features":features,
            "vol_max":volumemax,
            "vol_down":volumedown,
            "vol_mute":volumemute,
            "note_writer":note_write,
            "file_organizer":organize,
            "python_module":python_module
            }
assistant = Generic_Assistant_mod('initial_intents-1.json', intent_methods=mappings)
assistant.train_model()


def request_response(message):
    return assistant.request(message)

        

