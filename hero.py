class Hero():

    def __init__(self,pos,manager):
        self.manager = manager
        #self.land = land
        self.hero = loader.loadModel("smiley")
        self.hero.setPos(pos)
        self.hero.setScale(0.3)
        self.hero.setColor(1,0,0)

        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1)
        base.camLens.setFov(90)

    def accept_events(self):
        base.accept("w",self.move)
        base.accept("a",self.turn_left)
        base.accept("s",self.move_back)
        base.accept("d",self.turn_right) 
        base.accept("mouse3",self.build_block)
        base.accept("c",self.manager.save_map)
        base.accept("v",self.manager.load_map)
        base.accept("p",self.manager.clear)
        base.accept("l",exit)

        base.accept("w-repeat",self.move)
        base.accept("a-repeat",self.turn_left)
        base.accept("s-repeat",self.move_back)
        base.accept("d-repeat",self.turn_right) 

    def turn_left(self):
        old = self.hero.getH() 
        new = old + 10            
        self.hero.setH(new%360) 

    def turn_right(self):
        self.hero.setH((self.hero.getH()-10)%360) 

    def pusto(self):
        old = self.hero.getPos()
        dx,dy = self.check_angle()
        new = old[0] + dx, old[1] + dy, old[2]
        return not self.manager.check_position(new)

    def pusto_up(self):
        old = self.hero.getPos()
        dx,dy = self.check_angle()
        new = old[0] + dx, old[1] + dy, old[2] + 1
        return not self.manager.check_position(new)

    def bottom_is_empty(self):
        old = self.hero.getPos()
        
        new = old[0], old[1], old[2] - 1
        return not self.manager.check_position(new)

    def gravity(self):
        pustota = 0

        while self.bottom_is_empty():
            old = self.hero.getPos()
            new = old[0], old[1], old[2] - 1
            self.hero.setPos(new)
            pustota += 1
            print(old)

            if pustota == 50:
                exit()

    def move(self):
        old = self.hero.getPos()
        dx,dy = self.check_angle()
        self.gravity()

        if self.pusto():
            new = old[0] + dx, old[1] + dy, old[2]
            self.hero.setPos(new)
        else:
            if self.pusto_up():
                new = old[0] + dx, old[1] + dy, old[2] + 1
                self.hero.setPos(new)
        self.gravity()

    def move_back(self):
        old_pos = self.hero.getPos()
        dx,dy = self.check_angle()
        self.gravity()
        new_pos = old_pos[0] - dx, old_pos[1] - dy, old_pos[2]
        self.hero.setPos(new_pos)
        if self.pusto():
            new = old_pos[0] + dx, old_pos[1] + dy, old_pos[2]
            self.hero.setPos(new)
        else:
            if self.pusto_up():
                new = old_pos[0] + dx, old_pos[1] + dy, old_pos[2] + 1
                self.hero.setPos(new)

    def check_angle(self):
        angle = self.hero.getH()

        if 0 <= angle <= 20:
            return 0,1
        if 20 <= angle <= 65:
            return -1,1
        if 65 <= angle <= 110:
            return -1,0
        if 110 <= angle <= 155:
            return -1,-1
        if 155 <= angle <= 200:
            return 0,-1
        if 200 <= angle <= 245:
            return 1,-1
        if 245 <= angle <= 290:
            return 1,0
        if 290 <= angle <= 355:
            return 1,1
        if angle >= 355:
            return 0,1 

    def build_block(self):
        old_pos = self.hero.getPos()
        step_x,step_y = self.check_angle() 

        block_pos = old_pos[0] + step_x, old_pos[1] + step_y, old_pos[2]
        self.manager.addBlock(block_pos) 