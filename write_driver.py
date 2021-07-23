from pywinauto import application
import speech_recognition as sr
r = sr.Recognizer()

class Notepad_Driver:

    def open_win(self,app):
        app.start("Notepad.exe")
    def save_win(self,filename,app):
        app.Notepad.menu_select("File->SaveAs")
        app.SaveAs.Edit.set_edit_text(filename)
        app.SaveAs.Save.click(double=True)
    def write_win(self,inp,app):
        if(len(inp)!=0):
            for i in inp:
                app.Notepad.Edit.type_keys(i, with_spaces =True,with_newlines=True,
                        pause=0.05,
                        with_tabs=True )



if __name__ == '__main__':
    app = application.Application()
    obj=Notepad_Driver()
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
                    break
                else:
                    words=words+" "
                    obj.write_win(words, app)
                    #obj.write_win(" ", app)
            except LookupError:
                print("Please, speak more clearly")


