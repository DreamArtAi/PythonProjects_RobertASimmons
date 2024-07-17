from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = 320, 640
Window.top = 20
from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):
    pass

class Home(Screen):
    pass

class MainScript(MDApp):

    def build(self):

        # Create a list of all screen, loop through it and add it to the screenmanager
        # and return the screenmanager.
        self.window_manager = WindowManager()

        screens = [
            Home(name="home")
        ]

        for screen in screens:
            self.window_manager.add_widget(screen)

        return self.window_manager

if __name__=="__main__":
    MainScript().run()