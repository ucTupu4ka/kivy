from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout


class BoxApp(App):
    def build(self):
        al = AnchorLayout(anchor_x = 'center', anchor_y = 'center')

        #gl = GridLayout(cols=10, padding=[30], spacing=3)
        #for x in range(50):
        #    gl.add_widget(Button(text="Кнопка"))

        bl = BoxLayout(orientation='vertical', size_hint=[.4, .4])
        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text="Enter"))

        al.add_widget(bl)
        return al



if __name__ == "__main__":
    BoxApp().run()