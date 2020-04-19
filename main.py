import time
import datetime
import random
import threading
from threading import Thread
from random import seed
from random import randint
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition, WipeTransition, SwapTransition, \
    FadeTransition, RiseInTransition
from kivy.core.window import Window
from kivy.utils import platform
from kivy.clock import Clock, mainthread
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, NumericProperty, OptionProperty, AliasProperty, BooleanProperty, \
    BoundedNumericProperty, ObjectProperty
from kivy.utils import platform
from kivy.animation import Animation


Window.softinput_mode = 'below_target'
Window.keyboard_anim_args = {'d': 0.125, 't': 'in_out_quart'}
Window.size = (536, 953)
print(Window.size)


class Principal(Screen):
    redyx = NumericProperty(0)
    redyy = NumericProperty(0)
    greenx = NumericProperty(0)
    greeny = NumericProperty(0)
    backdropsrc = ObjectProperty(None)

    def on_pre_enter(self, *args):
        d = datetime.date.today()
        month = int(d.strftime('%m'))
        print(month)
        if month is 11 or 12 or 1 or 2:
            self.backdropsrc = './png/snow.zip'

    def on_enter(self, *args):
        Clock.schedule_once(self.comence, 0)

    def comence(self, *args):
        T1 = Thread(target=self.redshell)
        T2 = Thread(target=self.greenshell)
        T1.start()
        T2.start()

    def redshell(self, *args):
        Animation.cancel_all(self, 'redyx', 'redyy')
        seed(time.time())
        valuex = float(random.uniform(-0.5, 1.5))
        valuey = float(random.uniform(-0.5, 1.5))
        redanim = Animation(redyx=(valuex), redyy=(valuey), duration=3)
        redanim.start(self)
        Clock.schedule_once(self.redshell, 2)

    def greenshell(self, *args):
        Animation.cancel_all(self, 'greenx', 'greeny')
        seed(time.time())
        valuexx1 = float(random.uniform(-0.2, 0))
        valuexx2 = float(random.uniform(1, 1.2))
        valueyy1 = float(random.uniform(-0.2, 0))
        valueyy2 = float(random.uniform(1, 1.2))
        y = str(randint(1,2))
        x = str(randint(1,2))
        resultx = 'valuexx'+ x
        resulty = 'valueyy'+ y
        greenanim = Animation(greenx=eval(resultx), greeny=eval(resulty), duration=5)
        greenanim.start(self)
        Clock.schedule_once(self.greenshell, 5)

    def play(self, directory, num):
        print(time.time())
        seed(time.time())
        # Good Times
        if num == 1:
            value = randint(1, 10)
        # Bad times
        if num == 2:
            value = randint(1, 6)
        # Item fruitbowl
        if num == 3:
            value = randint(1, 8)
        # Catchphrase
        if num == 4:
            value = randint(1, 11)
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
            value = randint(1, 3)
        # Bam! Shock Dodge!
        if num == 14:
            value = randint(1, 1)

        sound = SoundLoader.load(directory + str(value) + '.wav')
        if sound:
            leng = sound.length
            duration = float(leng)
            sound.play()
            Principal.soundstorage = sound
            Clock.schedule_once(unload, duration+0.01)

    soundstorage = ''


def unload(*args):
    Principal.soundstorage.stop()
    Principal.soundstorage.unload()


class Setting(Screen):
    pass


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.backpress)

    def backpress(self, window, key, *args):
        if key == 27:
            if self.current_screen.name == "principal":
                return False
            elif self.current_screen.name == "settings":
                pass
                return True


def loadapp(*args):
    screens = [Principal(name="principal"), Setting(name="settings")]
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
        anim += Animation(imgvis=(1, 1, 1, 1), imgsize=(1,1), duration=1)
        anim.start(self)
        Clock.schedule_once(loadapp, 0)


Builder.load_file('startup.kv')
wm = WindowManager()
wm.add_widget(Loader(name="loader"))


class Primary(App):

    def build(self):
        return wm

    def on_enter(self):
        if platform == "android":
            Clock.schedule_once(self.remove_android_splash, 0)

    def remove_android_splash(self, *args):
        from jnius import autoclass
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        activity.removeLoadingScreen()

    def on_pause(self, *args):
        Animation.cancel_all()

    def on_resume(self, *args):
        Clock.schedule_once(Principal.greenshell, 0)
        Clock.schedule_once(Principal.redshell, 0)


if __name__ == "__main__":
    Primary().run()
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# End of Code
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
