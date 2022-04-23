# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.mapManager = Mapmanager()
        self.mapManager.create_floor()
        self.mapManager.create_walls()
        self.mapManager.load_map_txt()
        gg = Hero((0,1,2),self.mapManager)
        
game = Game()
game.run()
#wwdaaww