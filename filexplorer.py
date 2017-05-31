import os 
import subprocess
import pygame
from screen import Screen
from button import *
import cursor
import pointer
from handler import Handler

"colors"
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)
yellow = (255,255,0)
violet = (160,10,226)
orange = (255,165,0)

pygame.init()

clock = pygame.time.Clock()
FPS = 60

handler = Handler()

def run():

	_width = 600
	_height = 400
	_tile_arr = []
	_button_list = []
	_font = pygame.font.SysFont(None, 25)
	_current_dir = None
	_file_box_list = []
	_c = 0
	_default_x = 20
	_default_y = 20
	_mod = 20


	window = Screen.new(_width, _height, orange)
	mouse_cursor = cursor.Cursor(window)
	mouse_pointer = pointer.Pointer(_width/2, _height/2, window, black)

	dir_box = Display_Box(window, _current_dir, _default_x, _default_y, 20, 250, _font, 0)

	_button_list.append(dir_box)

	_current_dir = get_current_dir()
	_current_files = format_list(_current_dir)[0]
	
	for i in _current_files:

		try:
			file_box = Display_Box(window, _current_files[_c], _default_x, (_default_y + _mod), 20, 250, _font, 0)
			_button_list.append(file_box)
			_mod += 20
			_c+=1
		except:
			_c = 0
			_mod = 20	
			break

	_obj_list = [mouse_pointer, mouse_cursor]

	handler.set_screen(window, _width, _height)

	update_obj_lists(_obj_list, _button_list, _tile_arr)

	while 1:

		##########

			

		##########

		update_obj_lists(_obj_list, _button_list, _tile_arr)

		handler.update(0)
		handler.draw()	

		pygame.display.update()
		clock.tick(FPS)


def msg(_screen, _txt, _x, _y):

	_color = (0,0,0)
	_font = pygame.font.SysFont(None, 20)

	screen_text = _font.render(_txt, True, _color)
	_screen.blit(screen_text, [_x, _y])


def get_current_dir():
	usr_home = os.environ.get("HOME")
	path = os.path.join(usr_home, "Documents")
	return path

def get_file_list(mypath):				
	f = []
	y = []
	for (dirpath, dirnames, filenames) in os.walk(mypath):
	    f.extend(dirnames)
	    y.extend(filenames)
	    break    
	return f,y

def format_list(mypath):
	file_list = []
	dir_list = []
	file_list = get_file_list(mypath)[1]
	dir_list = get_file_list(mypath)[0]
	return dir_list,file_list

def update_obj_lists(obj, button, _tile_arr):

	handler.set_lists(obj, button, _tile_arr)


run()