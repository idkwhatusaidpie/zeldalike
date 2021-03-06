import pygame

from pygame.locals import *
from pygame.sprite import Group

import Player, wall

mapArea = [800,600]
width = mapArea[0]
height = mapArea[1]

def main():
	clock = pygame.time.Clock()

	#initialize and prepare screen
	pygame.init()
	screen = pygame.display.set_mode((mapArea[0], mapArea[1]))
	pygame.display.set_caption("Zeldalike")
	
	black = 0, 0, 0

	#creates a group
	sprites = Group()
	player = Player.Player()
	sprites.add(player)

	walls = Group()
	newWall = wall.Wall(150,200,50,20,(255,255,0))
	walls.add(newWall)

	#adds player to the sprites group

	#main game loop
	done = False
	while not done:
		clock.tick(60)
		screen.fill(black)
		sprites.draw(screen)
		walls.draw(screen)

		#basic event if statement block
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				done = True
				break

			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					player.move(2,0)
				if event.key == K_LEFT:
					player.move(-2,0)
				if event.key == K_UP:
					player.move(0,-2)
				if event.key == K_DOWN:
					player.move(0,2)
				

			if event.type == KEYUP:
				if event.key == K_RIGHT:
					player.move(-2,0)
				if event.key == K_LEFT:
					player.move(2,0)
				if event.key == K_UP:
					player.move(0,2)
				if event.key == K_DOWN:
					player.move(0,-2)
				
		
		player.update([width,height],walls)

		pygame.display.flip()

if __name__ == '__main__':
	main()