from tkinter import Button
import PySimpleGUI as sg
from yt_dlp import YoutubeDL
import ffmpeg

#settingfirst
ydl_opts = {"format": "best"}

#setting theme
sg.theme('DarkGray14')

#rayout
layout = [[sg.Text('MxYtdownloader',font=("yu Gothic UI",20))],
[sg.Text(" ")],
[sg.Text("typeurl"),sg.InputText("",key="url")],
[sg.Button("convert mp4",key="button1"),sg.Button("convert mp3",key="button2")]
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
        ydl_opts = ""
        ydl_opts = {"format": "best"}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    elif event == 'button2': ##This is mp3 convert
        ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
        url = values["url"]
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
window.close()