import random

#TODO: saturation for wolves
#TODO: deer on deer = light fight, join up or ignore
#

class Biome:
	def __init__(self, veg, trees):
		self.veg = veg
		self.trees = trees
		self.meat = 0

		self.debug = False

class Pack:
	def __init__(self, name, x, y, size, packType):
		self.name = name
		
		self.x = x
		self.y = y

		self.size = size
		self.packType = packType

		self.decay = 0

		self.wantedVeg = 1
		self.wantedTrees = 0

		self.dead = False

	def update(self, world):
		if not self.conditionsGood():
			self.move(world)

			self.decay += 1

			if self.decay > 3:
				self.size -= random.randrange(1, 4)
				self.decay = 0

		self.dead = self.size < 1

	def conditionsGood(self):
		biome = world.getBiome(self.x, self.y)

		return biome.veg >= self.wantedVeg and biome.trees >= self.wantedTrees

	def move(self, world):
		xMin = 0
		xMax = 0

		yMin = 0
		yMax = 0

		if self.x > 0:
			xMin = -1

		if self.x < len(world.map[0])-1:
			xMax = 2

		if self.y > 0:
			yMin = -1

		if self.y < len(world.map)-1:
			yMax = 2

		self.x += random.choice(range(xMin, xMax))
		self.y += random.choice(range(yMin, yMax))


class World:
	def __init__(self):
		self.packs = []
		self.map = []

		for y in range(5):
			self.map.append([])
			for x in range(5):
				self.map[y].append(Biome(random.randrange(0, 20), random.randrange(0, 20)))

	def update(self):
		for pack in self.packs:
			pack.update(self)

		self.packs = [pack for pack in self.packs if not pack.dead]
		
		for y in range(0, len(self.map)):
			for x in range(0, len(self.map[y])):
				biome = self.map[y][x]

				biome.meat = 0

				for pack in self.packs:
					if (pack.x, pack.y) == (x, y):
						if pack.packType in ["DEER", "WOLF"]:
							biome.meat += pack.size
	
						if pack.packType == "DEER":
							if biome.veg >= pack.wantedVeg * pack.size:
								biome.veg -= pack.wantedVeg * pack.size
				
							else:
								biome.veg = 0

		have_interacted = []

		for pack in self.packs:
			for otherPack in self.packs:
				if (pack.x, pack.y) == (otherPack.x, otherPack.y) and pack != otherPack and not (pack, otherPack):
					if pack.packType == "DEER":
						if otherPack.packType == "DEER":
							print("YAH YEET")
		
							roll = random.randrange(0, 101)
							
							if roll >= 0 and roll <= 33:
								otherPack.size -= random.randrange(1, 3)
							
							elif roll > 33 or roll <= 66:
								print("ignore")
							
							else:
								print("join")



	def print(self):
		base = 2

		strings = ["" for i in range(len(self.map)+base)]

		strings[0] += "   "

		for i in range(0, len(self.map)):
			strings[0] += "  {}".format(i)

		strings[1] = "  +" + ("-" * (len(strings[0]) - 1))

		for y in range(0, len(self.map)):
			strings[y+base] += "{} | ".format(y)
			
			for x in range(0, len(self.map[y])):

				if self.map[y][x].debug:
					strings[y+base] += "!! "
				else:
					for pack in self.packs:
						if pack.x == x and pack.y == y:
							if pack.packType == "DEER":
								strings[y+base] += "DD"
								break

							elif pack.packType == "WOLF":
								strings[y+base] += "WW"
								break

					else:
						if self.map[y][x].veg > 0:
							strings[y+base] += "V"
	
						else:
							strings[y+base] += " "
	
						if self.map[y][x].trees > 0:
							strings[y+base] += "T"
	
						else:
							strings[y+base] += " "

					strings[y+base] += " "
		
		for string in strings:
			print(string)

	def getBiome(self, findX, findY):
		for y in range(0, len(self.map)):
			for x in range(0, len(self.map[y])):
				if (x, y) == (findX, findY):
					return self.map[y][x]

		return False

world = World()
deer = Pack("Deer", 0, 0, 10, "DEER")
deer2 = Pack("Deer", 0, 0, 10, "DEER")
world.packs.append(deer)
world.packs.append(deer2)

while True:	
	world.update()
	world.print()
	print(world.getBiome(deer.x, deer.y).meat)

	inp = input(">")