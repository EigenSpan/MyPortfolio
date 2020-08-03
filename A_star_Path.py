# A* Pathfinding algorithm

import pygame
import math
from queue import PriorityQueue

pygame.init()

Width = 500

WIN = pygame.display.set_mode((Width, Width))
pygame.display.set_caption("A* Pathfinder")

red = (255,0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
orange = (255, 165, 0)
pink = (255, 20, 147)
black = (0, 0, 0)
grey = (128, 128, 128)
yellow = (204, 204, 0)

class Node:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = white
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	def position(self):
		return self.row, self.col

	def wall(self):
		return self.color == black

	def open(self):
		return self.color == green

	def closed(self):
		return self.color == red

	def start(self):
		return self.color == yellow

	def end(self):
		return self.color == orange

	def reset(self):
		self.color = white

	def make_wall(self):
		self.color = black

	def make_open(self):
		self.color = green

	def make_closed(self):
		self.color = red

	def make_start(self):
		self.color = yellow

	def make_end(self):
		self.color = orange

	def make_path(self):
		self.color = blue

	def draw_node(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		# DOWN NEIGHBOR
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].wall():
			self.neighbors.append(grid[self.row + 1][self.col])
		
		# UP NEIGHBOR
		if self.row > 0 and not grid[self.row - 1][self.col].wall():
			self.neighbors.append(grid[self.row - 1][self.col])
		
		# LEFT NEIGHBOR
		if self.col > 0 and not grid[self.row][self.col - 1].wall():
			self.neighbors.append(grid[self.row - 1][self.col])
		
		# RIGHT NEIGHBOR
		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].wall():
			self.neighbors.append(grid[self.row][self.col + 1])


	def __lt__(self, other):
		return False



def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x2- x1) + abs(y2 - y1)

def shortest_path(last_node, current, draw):
	while current in last_node:
		current = last_node[current]
		current.make_path()
		draw()



def a_star(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	last_node = {}
	g_value = {node: float("inf") for row in grid for node in row}
	g_value[start] = 0
	f_value = {node: float("inf") for row in grid for node in row}
	f_value[start] = h(start.position(), end.position())


	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			shortest_path(last_node, end, draw)
			end.make_end()
			start.make_start()
			return True

		for neighbor in current.neighbors:
			temp_g_value = g_value[current] + 1

			if temp_g_value < g_value[neighbor]:
				last_node[neighbor] = current
				g_value[neighbor] = temp_g_value
				f_value[neighbor] = temp_g_value + h(neighbor.position(), end.position())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_value[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False


def my_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			node = Node(i, j, gap, rows)
			grid[i].append(node)

	return grid

def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, grey, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, grey, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
	win.fill(white)

	for row in grid:
		for node in row:
			node.draw_node(win)

	draw_grid(win, rows, width)
	pygame.display.update()

def clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap
	return row, col

def main(win, width):
	Rows = 50
	grid = my_grid(Rows, width)

	start = None
	end = None

	run = True
	started = False

	while run:
		draw(win, grid, Rows, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			# LEFT MOUSE BUTTON
			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = clicked_pos(pos, Rows, width)
				node = grid[row][col]
				if not start:
					start = node
					start.make_start()
				
				elif not end:
					end = node
					end.make_end()

				elif node != end and node != start:
					node.make_wall()

			# RIGHT MOUSE BUTTON
			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				row, col = clicked_pos(pos, Rows, width)
				node = grid[row][col]
				node.reset()
				if node == start:
					start = None

				elif node == end:
					end = None
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for node in row:
							node.update_neighbors(grid)
					a_star(lambda: draw(win, grid, Rows, width), grid, start, end)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = my_grid(Rows, width)

	pygame.quit()
 

main(WIN, Width)

















