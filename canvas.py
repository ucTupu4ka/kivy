from kivi.app import App
from kivy.uix.widget import Widget

from kivy.graphics import (Color, Ellipse, Rectangle, Line

class PainterWidget(Widget):
    def __init__(self, **kwargs):
        super(PainterWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 1, 0, 1)
            Ellipse(pos = (100, 100), size = (50, 50))

class PaintApp(App):
    def build(self):
        return PainterWidget()

if __name__ == '__main__':
    PaintApp().run()