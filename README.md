//Laberinto 
class Game:

    def __init__(self):
        self.maze = None
        
    def create_wall(self):
        return Wall()
    
    def create_door(self, side1, side2):
        door = Door(side1, side2)
        return door
    
    def create_room(self, id):
        room= Room(id)
        room.north= self.create_wall()
        room.east = self.create_wall()
        room.south= self.create_wall()
        room.west = self.create_wall()
        return room
    
    def create_maze(self):
        return Maze()   
    
    
    def  make2RoomsMazeFM(self):
        game = Game()
        self.maze = self.create_maze()
        room1 = self.create_room(1)
        room2 = self.create_room(2)
        door = game.create_door(room1, room2)
        room1.south= door
        room2.north = door
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)
        
        return self.maze
        
    
    def make2RoomsMaze(self):
        self.maze= Maze()
        room1 = Room(1)
        room2 = Room(2)
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)
        door= Door(room1, room2)
        room1.south = door
        room2.north = door
        return self.maze

        
    
class MapElement:

    def __init__(self):
        pass
    def entrar(self):
        pass

class Maze(MapElement):

    def __init__(self):
        self.rooms = []

    def addRoom(self, room):
        self.rooms.append(room)

    def entrar(self):
        self.rooms[0].entrar()
        
        
class Hoja(MapElement):

    def accept(self, visitor):
        visitor.visitHoja(self)

class Decorator(Hoja):

    def __init__(self, component):
        self.component = component
        
class Contenedor(MapElement):

    def __init__(self):
        self.hijos=[]
        
    def agregarhijo(self, hijo):
        self.hijos.append(hijo)
        
    def eliminarhijo(self, hijo):
        self.hijos.remove(hijo)


class Room(MapElement):

    def __init__(self, id):         
        self.north = Wall()
        self.east = Wall()
        self.west = Wall()
        self.south = Wall()
        self.id = id

    def entrar (self):
        print("Entrando en la habitación", self.id)

        
        
class Door(MapElement):

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.opened = False
    def entrar(self):
        if self.opened:
            self.side1.entrar()
        else:
            print("¡La puerta está bloqueada!")
        
        
class Wall(MapElement):

    def __init__(self):
        pass # Walls don't need any special attributes
    def entrar(self):
        print("¡No puedes entrar aquí!")



class BombedGame(Game):

    def create_wall(self):
        return BombedWall()

class BombedWall(Wall):

    def __init__(self):
        self.active = False
        
    def entrar(self):
        if self.active: 
            print("La bomba ha explotado")
        return super().entrar()

class Bicho:

    def __init__(self, vidas, poderes):
        self.vidas = vidas
        self.poderes = poderes

    def actua(self):
        print("El bicho está actuando...")
        self.usar_poder()

class Modo:

    def __init__(self, nombre):
        self.nombre = nombre

    def actua(self, bicho):
        self.caminar(bicho)
        
    def caminar(self, bicho):
        pass
        
class Agresivo(Modo):

    def __init__(self):
        super().__init__("ataque")

class Perezoso(Modo):

    def __init__(self):
        super().__init__("defensa")

class Orientacion: 
    
    def __init__(self):
        pass
    
    def poner(self, orientacion): 
        pass
        
class Norte(Orientacion):

    def __init__(self):
        pass
    
    def poner(self):
        super().poner("norte")

class Sur(Orientacion):

    def __init__(self):
        pass
    
    def poner(self):
        super().poner("sur")
    
class Este(Orientacion):

    def __init__(self):
        pass
    
    def poner(self):
        super().poner("este")
    
class Oeste(Orientacion):

    def __init__(self):
        pass
    
    def poner(self):
        super().poner("oeste")
    
    
game = Game()
game.make2RoomsMaze()
game.maze.entrar()

game= Game()
game.make2RoomsMazeFM()


game = BombedGame()
game.make2RoomsMazeFM()
game.maze.entrar()
