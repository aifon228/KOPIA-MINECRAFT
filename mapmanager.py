import pickle

class Mapmanager():
    def __init__(self):
        self.model = 'block.egg' # модель кубика в файле block.egg
        self.texture = 'neon.jpg'# текстура кубика           
        self.color = (0,1,0,1)
        self.startNew()

    def startNew(self):       
	    self.land = render.attachNewNode("Land")

    def addBlock(self, position):
        block = loader.loadModel(self.model)
        texture = loader.loadTexture(self.texture)
        block.setTexture(texture)
        #block.setColor(self.color)
        block.setPos(position)
        block.reparentTo(self.land)

    def check_position(self, position):
        position = position[0], position[1], position[2]

        for block in self.land.getChildren():
            if position == block.getPos():
                return True

    def create_floor(self):
        self.texture = 'neon.jpg'
        for x in range(10):
            for y in range(10):
                self.addBlock((x,y,0))

    def create_walls(self):
        self.texture = 'neon.jpg'
        for x in range(10):
            for y in [10,10]:
                for z in range(30):
                    self.addBlock((x,y,z))

    def save_map(self):
        blocks = self.land.getChildren()
        with open("karta.dat","wb") as file:
            pickle.dump(len(blocks), file)
            for block in blocks:
                x, y, z =block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos,file)

    def load_map(self):
        self.clear()
        with open("karta.dat","rb") as file:
            length = pickle.load(file)
            for i in range(length):
                pos = pickle.load(file)
                self.addBlock(pos)

    def load_map_txt(self):
        with open("map.txt","r") as file:
            data = file.readlines()

        x = 0
        for string in data:
            y = 0
            temp = string.split(" ")[:-1]

            for z in temp:
                self.addBlock((x,y,int(z)))
                y += 1
            x += 1

    def clear(self):
        self.land.removeNode()
        self.startNew() 


