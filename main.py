import time
import random
from random import seed
from random import randint
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition, WipeTransition
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.utils import platform
from kivy.animation import Animation

Window.softinput_mode = 'below_target'
Window.keyboard_anim_args = {'d': 0.125, 't': 'in_out_quart'}


threadshell = ObjectProperty(None)


class Principal(Screen):

    greenshell = ObjectProperty(None)
    redshell = ObjectProperty(None)
    redyx = NumericProperty(0)
    redyy = NumericProperty(0)
    greenx = NumericProperty(0)
    greeny = NumericProperty(0)
    backdropsrc = ObjectProperty(None)
    animtime = NumericProperty(99)
    backdropsource = ObjectProperty(None)
    layer1posx = NumericProperty(0.5)
    layer1posy = NumericProperty(0)
    layer2posx = NumericProperty(0)
    layer2posy = NumericProperty(0)
    stoploop = 0

    def on_pre_enter(self, *args):
        if wm.has_screen("setting") is False:
            screen = Setting(name="setting")
            wm.add_widget(screen)
        import datetime
        d = datetime.date.today()
        month = int(d.strftime('%m'))
        if month == 11:
            self.backdropsrc = './png/snow.zip'
            self.animtime = 0.016
        if month == 12:
            self.backdropsrc = './png/snow.zip'
            self.animtime = 0.016
        if month == 1:
            self.backdropsrc = './png/snow.zip'
            self.animtime = 0.016
        if month == 2:
            self.backdropsrc = './png/snow.zip'
            self.animtime = 0.016

    def on_enter(self, *args):
        l1 = Animation(layer1posx=0.8, layer1posy=1.5, duration=20)
        l2 = Animation(layer2posx=1, layer2posy=2, duration=20)
        l1 += Animation(layer1posx=1, layer1posy=-0.5, duration=0)
        l2 += Animation(layer2posx=1, layer2posy=-2, duration=0)
        l1 += Animation(layer1posx=0.3, layer1posy=1.5, duration=20)
        l2 += Animation(layer2posx=0, layer2posy=3, duration=20)
        l1 += Animation(layer1posx=0, layer1posy=-0.5, duration=0)
        l2 += Animation(layer2posx=0, layer2posy=-2, duration=0)
        l1.repeat = True
        l2.repeat = True
        l1.start(self)
        l2.start(self)
        Principal.stoploop = 0
        import threading
        t1 = threading.Thread(target=self.shells)
        t1.start()

    def on_leave(self, *args):
        Animation.cancel_all(self)
        Principal.stoploop = 1

    def shells(self, *args):
        if Principal.stoploop == 0:
            seed(time.time())
            valuexx1 = float(random.uniform(-0.2, 0))
            valuexx0 = float(random.uniform(1, 1.2))
            valueyy1 = float(random.uniform(-0.2, 0))
            valueyy0 = float(random.uniform(1, 1.2))
            valuex = float(random.uniform(-0.5, 1.5))
            valuey = float(random.uniform(-0.5, 1.5))
            resultx = 'valuexx' + str(int(valuex))
            resulty = 'valueyy' + str(int(valuey))
            redanim = Animation(redyx=(valuex), redyy=(valuey), duration=5)
            redanim.repeat = False
            greenanim = Animation(greenx=eval(resultx), greeny=eval(resulty), duration=5)
            greenanim.repeat = False
            redanim.start(self)
            greenanim.start(self)
            Clock.schedule_once(self.shells, 5)

    def play(self, directory, num):
        from kivy.core.audio import SoundLoader
        print(time.time())
        seed(time.time())
        # Good Times
        if num == 1:
            value = randint(1, 12)
        # Bad times
        if num == 2:
            value = randint(1, 7)
        # Item fruitbowl
        if num == 3:
            value = randint(1, 12)
        # Catchphrase
        if num == 4:
            value = randint(1, 13)
        # Oh baby!
        if num == 5:
            value = randint(1, 2)
        # Disbelief
        if num == 6:
            value = randint(1, 7)
        # Suprise
        if num == 7:
            value = randint(1, 3)
        # Let's go!
        if num == 8:
            value = randint(1, 5)
        # Wow!
        if num == 9:
            value = randint(1, 2)
        # Hey Troy!
        if num == 10:
            value = randint(1, 4)
        # Laugh
        if num == 11:
            value = randint(1, 5)
        # Random Noises
        if num == 12:
            value = randint(1, 3)
        # Random Frases
        if num == 13:
            value = randint(1, 4)
        # Bam! Shock Dodge!
        if num == 14:
            value = randint(1, 1)

        sound = SoundLoader.load(directory + str(value) + '.wav')
        if sound:
            leng = sound.length
            duration = float(leng)
            sound.play()

    def settings(self):
        wm.transition = CardTransition()
        wm.transition.direction = "left"
        wm.current = "setting"


class Setting(Screen):

    def youtube(self):
        import webbrowser
        if platform == "android":
            import android
        webbrowser.open("https://www.youtube.com/Nmeade")

    def twitch(self):
        import webbrowser
        if platform == "android":
            import android
        webbrowser.open("https://www.twitch.tv/Nmeade")

    def twitter(self):
        import webbrowser
        if platform == "android":
            import android
        webbrowser.open("https://twitter.com/nmeade")

    def instagram(self):
        import webbrowser
        if platform == "android":
            import android
        webbrowser.open("https://www.instagram.com/nmeade5/")

    def git(self):
        import webbrowser
        if platform == "android":
            import android
        webbrowser.open("https://github.com/Whatnoww/Configurable-Soundboard")


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.backpress)

    def backpress(self, window, key, *args):
        if key == 27:
            if self.current_screen.name == "principal":
                return False
            elif self.current_screen.name == "setting":
                wm.transition.direction = 'right'
                wm.current = "principal"
                return True


def loadapp(*args):
    screens = [Principal(name="principal")]
    for screen in screens:
        wm.add_widget(screen)
    wm.transition = WipeTransition()
    Clock.schedule_once(homescreen, 4)


def homescreen(*args):
    wm.current = 'principal'


class Loader(Screen):
    float = ObjectProperty(None)

    def on_enter(self, *args):
        print('on enter fired')
        anim = Animation(backdrop=(0.2, 0.2, 0.7, 1), duration=1)
        anim += Animation(sizing=(5000, 5000), posing=(2375), duration=1)
        anim += Animation(imgvis=(1, 1, 1, 1), imgsize=(1, 1), duration=1)
        anim.start(self)
        Clock.schedule_once(loadapp, 0)


from kivy.lang import Builder

Builder.load_file('startup.kv')
wm = WindowManager()
wm.add_widget(Loader(name="loader"))


class Primary(App):

    def build(self):
        return wm

    def on_enter(self):
        if platform == "android":
            Clock.schedule_once(self.remove_android_splash)

    def remove_android_splash(self, *args):
        from jnius import autoclass
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        activity.removeLoadingScreen()
        from android import hide_loading_screen
        hide_loading_screen()

    def on_pause(self, *args):
        Animation.cancel_all(Principal)
        Principal.stoploop = 1
        return True

    def on_resume(self, *args):
        pass


if __name__ == "__main__":
    Primary().run()
