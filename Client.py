#import kivy
#kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import socket

MAX_BUF = 1024  # bytes



class MyApp(App):
    def build(self):
        def connect(instance):
            global client
            ADDRESS_TO_SERVER = (ip.text, int(port.text))
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                client.connect(ADDRESS_TO_SERVER)
                instance.background_color = (0, 1, 0, 1)
            except OSError: instance.background_color = (1, 0, 0, 1)

        def send(instance):
            answer.text = ""
            try:
                client.send(bytes(message.text.encode()))
                answer.insert_text(str(client.recv(MAX_BUF).decode('UTF-8')))
                #print("Получен ответ - " + str(client.recv(MAX_BUF).decode('UTF-8')))
            except NameError: pass

        Al = AnchorLayout()
        Gl = GridLayout(rows=3, cols=3, padding=30)
        Gl.add_widget(Widget())
        Gl.add_widget(Label(text="Все чётные буквы делаются заглавными"))
        Gl.add_widget(Widget())
        ip = TextInput(hint_text="localhost")
        Gl.add_widget(ip)
        port = TextInput(hint_text="8686")
        Gl.add_widget(port)
        Gl.add_widget(Button(text="Подключиться", on_press=connect))
        message = TextInput(hint_text="Сообщение серверу")
        Gl.add_widget(message)
        Gl.add_widget(Button(text="Отправить", on_press=send))
        answer = TextInput(hint_text="Ответ сервера")
        Gl.add_widget(answer)
        Al.add_widget(Gl)
        return Al


if __name__ == '__main__':
    MyApp().run()
