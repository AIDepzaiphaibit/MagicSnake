import pygame
from GameSetColor import *
import random

pygame.init()

_width = 500
_heigh = 400

_display = pygame.display.set_mode([500, 500])
pygame.display.set_caption('App')

def object_checking(size1, size2):
    if size1[0] <= size2[0]+size2[2] and size2[0] <= size1[0]+size1[2] and size1[1] <= size2[1]+size2[3] and size2[1] <= size1[1]+size1[3]:
        return True
    return False
def random_apple():
	pos = random.randint(0, 475)
	return pos

_run = True

_left = True
_right = False
_up = False
_down = False

move_left = True
move_right = False
move_up = False
move_down = False

size1 = [250, 250, 25, 25]
size2 = [random.randint(0, 475), random.randint(0, 475), 25, 25]

if _left == True:
	_right = False
	move_left = True
if _right == True:
	_left = False
	move_right = True
if _up == True:
	_down = False
	move_up = True
if _down == True:
	_up = False
	move_down = True

_speed = pygame.time.Clock()

_score_data = 0

font = pygame.font.SysFont('san', 35)

while _run:
	_speed.tick(500)
	_display.fill(color.classic_color.black)
	if move_left == True:
		size1[0] -= 1
	if move_right == True:
		size1[0] += 1
	if move_up == True:
		size1[1] -= 1
	if move_down == True:
		size1[1] += 1

	if size1[0] < 0:
		size1[0] = 475
	if size1[0] > 475:
		size1[0] = 0
	if size1[1] < 0:
		size1[1] = 475
	if size1[1] > 475:
		size1[1] = 0


	if object_checking(size1, size2) == True:
		_score_data += 1
		size2[0] = random.randint(0, 475)
		size2[1] = random.randint(0, 475)
	_score_data = _score_data
	_score_text = font.render(f'Score: {_score_data}', True, color.classic_color.white)

	_apple = pygame.draw.rect(_display, color.classic_color.red, (size2[0], size2[1], size2[2], size2[3]))
	_snake = pygame.draw.rect(_display, color.classic_color.green, (size1[0], size1[1], size1[2], size2[3]))

	_display.blit(_score_text, (50, 5))

	for _event in pygame.event.get():
		if _event.type == pygame.QUIT:
			_run = False
		if _event.type == pygame.KEYDOWN:
			if _event.key == pygame.K_LEFT:
				move_left = True
				move_right = False
			if _event.key == pygame.K_RIGHT:
				move_right = True
				move_left = False
			if _event.key == pygame.K_UP:
				move_up = True
				move_down = False
			if _event.key == pygame.K_DOWN:
				move_down = True
				move_up = False
	pygame.display.flip()
pygame.quit()