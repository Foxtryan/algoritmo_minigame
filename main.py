# Kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen
# Python
import numpy as np



class Menu(Screen):
	pass

class TelaJogo(Screen):
	pass

class Minigame(App):
	
	def build(self):
		main_widget = Builder.load_string(open("interface.kv", encoding="UTF-8").read())
		return main_widget
		
if __name__ == '__main__':
	Minigame().run()