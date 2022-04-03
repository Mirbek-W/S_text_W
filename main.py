from concurrent.futures import thread
from threading import Thread
from tkinter import *

import pyautogui 
from vosk import Model, KaldiRecognizer
from time import sleep 
import json, pyaudio
import pyttsx3


def window1():

    root=Tk()
    root.geometry("309x310")
    root.resizable(width=False, height=False)
    root.title("слова в текст ")
    root.iconbitmap(r'icons/rec.ico')








    def iop12():
           #создание звука голос 
        tts = pyttsx3.init()
        voices = tts.getProperty('voices')
        tts.setProperty('voice', 'ru') 
          # Попробовать установить предпочтительный голос
        for voice in voices:
            if voice.name == 'Irina':
                tts.setProperty('voice', voice.id)
         #c tts.say(text)
        tts.say("чтобы выйти, или закрыть программу скажите выйти!")
        tts.runAndWait()
        

        # тут начинает работает микрофон и после проверка
        model= Model("vosksmall")
        rec= KaldiRecognizer(model,16000)
        p=pyaudio.PyAudio()
        stream=p.open(format=pyaudio.paInt16,channels=1, rate=16000,input=True,frames_per_buffer=8000)
        stream.start_stream()
    
        def listen():
            while True:
                data=stream.read(4000,exception_on_overflow=False)
                if (rec.AcceptWaveform(data)) and (len(data)>0):
                        answer=json.loads(rec.Result())
                        if answer ["text"]:
                            yield answer ["text"]

        for text in listen():
            print(text) #  выводит на консоль то что слышал !!!!
            pyautogui.press(text)
    



    

    
 
        # условные операторы проверка текста 
            if  text =="выход":
                tts.say("отключение микрофона!")
                tts.runAndWait()
                return
                
            elif text =="как твойии дела":
                print("вопрос был как твойии дела!!!")




    


        tts.runAndWait()# голос закрытия как Mainloop

            






        
    


    
# загружаем картинку


    loadimage = PhotoImage(file="icons/record.png")
    roundedbutton = Button(root, image=loadimage,command=iop12) 
    roundedbutton["border"] = "0" # Обязательно убираем border!!!
    roundedbutton.grid(column=0,row=0)



    








    root.mainloop()







window1()







