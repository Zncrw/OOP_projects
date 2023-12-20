from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
import wikipedia

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        # Get user input as string
        search = self.manager.current_screen.ids.user_search.text
        # Get the page from wikipedia
        page = wikipedia.page(search)
        # Get first image on the page
        img_link = page.images[0]
        print(f"Title: {page.title}")
        print(f"URL: {page.url}")
        print(f"Images: {page.images}")

        return img_link
    def save_file(self):
        # Download image
        req = requests.get(self.search_image())
        imagepath = 'images/image.jpg'
        # Save image as user search.jpg
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        return file
    def set_img(self):
        # Set the image as background of app
        self.manager.current_screen.ids.img.source = self.save_file()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()




