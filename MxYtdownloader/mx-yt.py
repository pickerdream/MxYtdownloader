from tkinter import Button
import PySimpleGUI as sg
from yt_dlp import YoutubeDL

#settingfirst
ydl_opts = {"format": "best"}

#setting theme
sg.theme('DarkGray14')

#rayout
layout = [[sg.Text('MxYtdownloader',font=("yu Gothic UI",20))],
[sg.Text("typeurl"),sg.InputText("",key="url")],
[sg.Button("convert",key="button1")]
]

#create window
window = sg.Window('MxYtdownloader', layout)

#roop
while True:
    event, values = window.read()
    if event ==sg.WIN_CLOSED:
        break
    elif event == 'button1':
        url = values["url"]
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
window.close()