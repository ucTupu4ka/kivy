from kivy.app import App
from kivy.uix.widget import Widget

from kivy.graphics import (Color, Ellipse, Rectangle, Line)


class PainterWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 1, 0, 1)
            rad = 30
            Ellipse(pos=(touch.x - rad / 2, touch.y - rad / 2), size=(rad, rad))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)

class PaintApp(App):
    def build(self):
        return PainterWidget()


if __name__ == '__main__':
    PaintApp().run()
