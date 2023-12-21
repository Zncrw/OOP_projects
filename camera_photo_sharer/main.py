from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        # changing button name when camera is running
        self.ids.camera_button.text = 'Stop Camera'
        # setting background of camera widget
        self.ids.camera.texture = self.ids.camera._texture

    def stop(self):
        self.ids.camera.play = False
        # changing button name when camera is running
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        # getting current time for the name of file
        current_time = time.strftime('S%M%H%-d%m%Y')
        # saving captured screen as file with current_time.png
        filename = f'saved_imgs/{current_time}.png'
        self.ids.camera.export_to_png(filename)
        # changing screen to current captured img
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = filename


class ImageScreen(Screen):
    pass


class FileSharer:
    def __init__(self, filepath, api_key='8ba98d13-ed91-47fc-a3ce-a4f1b0a28679'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    @property
    def build(self):
        return RootWidget()


MainApp().run()
