from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout


class BoxApp(App):
    def build(self):
        #al = AnchorLayout(anchor_x = 'center', anchor_y = 'center')

        gl = GridLayout(cols=4, padding=[30], spacing=3)
        gl.add_widget(Button(text="7"))
        gl.add_widget(Button(text="8"))
        gl.add_widget(Button(text="9"))
        gl.add_widget(Button(text="x"))

        gl.add_widget(Button(text="4"))
        gl.add_widget(Button(text="5"))
        gl.add_widget(Button(text="6"))
        gl.add_widget(Button(text="-"))

        gl.add_widget(Button(text="1"))
        gl.add_widget(Button(text="2"))
        gl.add_widget(Button(text="3"))
        gl.add_widget(Button(text="+"))

        gl.add_widget(Widget())
        gl.add_widget(Button(text="0"))
        gl.add_widget(Button(text=","))
        gl.add_widget(Button(text="="))

        #bl = BoxLayout(orientation='vertical', size_hint=[.4, .4])
        #bl.add_widget(TextInput())
        #bl.add_widget(TextInput())
        #bl.add_widget(Button(text="Enter"))

        #al.add_widget(bl)
        return gl



if __name__ == "__main__":
    BoxApp().run()