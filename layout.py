from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout


class BoxApp(App):
    def build(self):
        #al = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
        #al.add_widget(Button(text="Кнопка 1", size_hint=[.5, .5]))

        #gl = GridLayout(cols=10, padding=[30], spacing=3)

        #for x in range(50):
        #    gl.add_widget(Button(text="Кнопка"))

        #bl = BoxLayout(orientation='horizontal', padding=[50], spacing=100)
        #bl.add_widget(Button(text="Кнопка 1"))
        #bl.add_widget(Button(text="Кнопка 2"))
        #bl.add_widget(Button(text="Кнопка 3"))

        return al



if __name__ == "__main__":
    BoxApp().run()