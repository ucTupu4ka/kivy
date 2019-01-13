from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout




class BoxApp(App):
    def build(self):
        return Button()


if __name__ == "__main__":
    BoxApp().run()