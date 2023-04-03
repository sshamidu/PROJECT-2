import PySimpleGUI as sg
import pyttsx3

text_to_speech_p2_engine = pyttsx3.init()
kind_of_voices = text_to_speech_p2_engine.getProperty('voices')

layout = [
    [sg.Text('Select the type of voice:', text_color='AliceBlue', background_color='coral4'),
     sg.Radio('Male', 'RADIO1', default=True, key='male', background_color='Green'),
     sg.Radio('Female', 'RADIO1', key='female', background_color='green')],
    
    [sg.Text('Enter text to speak:', text_color='AliceBlue', background_color='coral4'),
     sg.InputText(key='text_input'),
     sg.Button('Speak', button_color='purple', size=(10, 1))],
    
    [sg.Text('Adjust speed:', text_color='AliceBlue', background_color='coral4', size=(15, 1)),
     sg.Slider(range=(50, 200), orientation='h', size=(25, 20), default_value=100, key='speed')],
    
    [sg.Text('Adjust volume:', text_color='AliceBlue', background_color='coral4', size=(15, 1)),
     sg.Slider(range=(0, 100), orientation='h', size=(25, 20), default_value=100, key='volume')],
]

window = sg.Window('READ ALOUD', layout, background_color='CadetBlue4')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['text_input']
        speed = values['speed'] / 100.0
        volume = values['volume'] / 100.0
        if values['male']:
            text_to_speech_p2_engine.setProperty('voice', kind_of_voices[0].id)
        elif values['female']:
            text_to_speech_p2_engine.setProperty('voice', kind_of_voices[1].id) 

        text_to_speech_p2_engine.setProperty('rate', speed * 200)
        text_to_speech_p2_engine.setProperty('volume', volume)
        text_to_speech_p2_engine.say(text)
        text_to_speech_p2_engine.runAndWait()

window.close()
