from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time
from filestack import Client
from kivy.core.clipboard import Clipboard
import webbrowser

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        """
        starts camera and change the text of button
        """
        # set the visibility of camera frame
        self.ids.camera.opacity = 1

        self.ids.camera.play = True
        # changing button name when camera is running
        self.ids.camera_button.text = 'Stop Camera'

        # setting background of camera widget
        self.ids.camera.texture = self.ids.camera._texture

    def stop(self):
        """
        stops the camera and change the text of the button
        """
        # set the invisibility of camera frame
        self.ids.camera.opacity = 0

        self.ids.camera.play = False

        # changing button name when camera is running
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        """
        capture the image of camera and saves that under the current time
        as a file.
        """
        # getting current time for the name of file
        current_time = time.strftime('S%M%H%-d%m%Y')

        # saving captured screen as file with current_time.png
        self.filename = f'saved_imgs/{current_time}.png'
        self.ids.camera.export_to_png(self.filename)

        # changing screen to current captured img
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filename


class ImageScreen(Screen):
    error_message = 'Create link first please!'
    def create_link(self):
        """
        Acces the saved image file and uploads it to web and inserts the link
        to Label widget.
        """
        # gets the current file path
        file_path = App.get_running_app().root.ids.camera_screen.self.filename

        # initialize the FileSharer class
        fileshare = FileSharer(filepath=file_path)
        self.url = fileshare.share()

        # gets a current link under the Label widget
        self.ids.link.text = self.url

    def copy_link(self):

        """
        method that copy the shareable link after pressing copy link button
        """
        try:
            Clipboard.copy(self.url)
        except AttributeError:
            self.ids.link.text = self.error_message

    def open_link(self):
        """
        method that will open a browser window with saved image
        """
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.error_message

class FileSharer:
    def __init__(self, filepath, api_key='8ba98d13-ed91-47fc-a3ce-a4f1b0a28679'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        """
        method that will create a link using users API.key
        """
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
