import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyFrontend(GridLayout):
    pass

class kivyApp(App):
    def build(self):
        return MyFrontend()

if __name__ == '__main__':
    kivyApp().run()