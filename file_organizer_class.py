import os
import shutil

class file_organizer:
    def __init__(self,pos):
        self.pos=pos
        self.path_document=r"C:\Users\lenovo\Documents"
        self.path_desktop=r"C:\Users\lenovo\Desktop"
        self.path_downloads=r"C:\Users\lenovo\Downloads"
        self.path_test=r"C:\Users\lenovo\Desktop\demo_file_organizer"
    def organize(self):
        if self.pos==1:
            path=self.path_document
        elif self.pos==2:
            path=self.path_desktop
        elif self.pos==3:
            path=self.path_downloads
        else :
            path=self.path_test
        print(path)
        files=os.listdir(path)
        for file in files:
            filename,extension=os.path.splitext(file)
            extension=extension[1:]

            if os.path.exists(path+'/'+extension):
                shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
            else:
                os.makedirs(path+'/'+extension)
                shutil.move(path+'/'+file,path+'/'+extension+'/'+file)

if __name__== "__main__":
    obj2=file_organizer(4)
    obj2.organize()

