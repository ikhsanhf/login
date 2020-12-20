from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

engine = create_engine('sqlite:///latihan.db')
DBSession = sessionmaker()
DBSession.configure(bind=engine)
session = DBSession()
# kita letakkan statements membuat session disini
# supaya session selalu dibuat saat aplikasi di run

class LoginWindow(Widget):
    def login(self, *args):
        username_input = self.ids.username_input
        username_text = username_input.text
        password_input = self.ids.password_input
        password_text = password_input.text

        # lakukan query untuk mendapatkan objek/record yang memiliki
        # username sesuai dengan input. Karena hasil query selalu berbentuk
        # list maka kita harus iterasi
        for a in session.query(User).filter(User.username == username_text):
            if a.password != password_text:
                return
            label = self.ids.success
            label.text = "Success"

class LoginApp(App):
    def build(self):
        return LoginWindow()


if __name__ == '__main__':
    LoginApp().run()