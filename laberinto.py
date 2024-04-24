import time

class ThreadManager:
    def __init__(self):
        self.threads = []

    def addThread(self, thread):
        self.threads.append(thread)

    def start(self):
        for thread in self.threads:
            thread.start()

    def join(self):
        for thread in self.threads:
            thread.join()

    def stop(self):
        for thread in self.threads:
            thread.stop()  

class Game:
    def __init__(self):
        self.maze = None
        self.bicho = []
        self.threadManager = ThreadManager()
        
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

    def fabricarBichoAgresivo(self, room):
        bicho = Bicho(Agresivo())
        bicho.vidas = 5
        bicho.poderes = 2
        bicho.posicion = room
        return bicho

    def fabricarBichoPerezoso(self, room):
        bicho = Bicho(Perezoso())
        bicho.vidas = 3
        bicho.poderes = 0
        bicho.posicion = room
        return bicho

    def fabricarNorte(self):
        return Norte().get_instance()

    def fabricarEste(self):
        return Este().get_instance()

    def fabricarOeste(self):
        return Oeste().get_instance()

    def fabricarSur(self):
        return Sur().get_instance()
    
    def lanzarHilos(self):
        for bicho in self.bicho:
            self.threadManager.addThread(bicho)
        self.threadManager.start()
        
    def stopThreds(self):
        self.threadManager.stop()
        self.threadManager.join()
        
    
class MapElement:
    def __init__(self):
        pass
    def entrar(self):
        pass

    def abrir(self):
        pass

    def recorrer(self):
        pass

        
class Hoja(MapElement):
    def accept(self, visitor):
        visitor.visitHoja(self)
        
class Tunel(Hoja):
    def __init__(self):
        super().__init__()
        self.maze = None

    def entrar(self, alguien):
        self.maze.entrar(alguien)

    

class Decorator(Hoja):
    def __init__(self, component):
        self.component = component
        
class Contenedor(MapElement):
    def __init__(self):
        self.hijos=[]
        self.num= None
        self.forma= None
        
    def agregarhijo(self, hijo):
        self.hijos.append(hijo)
        
    def eliminarhijo(self, hijo):
        self.hijos.remove(hijo)
        
    def addOrientation(self, orientation):
        self.orientations.append(orientation)
    
    def removeOrientation(self, orientation):
        self.orientations.remove(orientation)

    def goNorth(self, someone):
        self.north.enter(someone)
        
    def goEast(self, someone):
        self.east.enter(someone)
        
    def goSouth(self, someone):
        self.south.enter(someone)
        
    def goWest(self, someone):
        self.west.enter(someone)
        
    def recorrer(self, bloque):
        bloque(self)
        for hijo in self.hijos:
            hijo.recorrer(bloque)
            
    

class Maze(Contenedor):
    def __init__(self):
        self.rooms = []

    def addRoom(self, room):
        self.rooms.append(room)

    def entrar(self, alguien):
        self.rooms[0].entrar(alguien)
        
    def getRoom(self, id):
        for room in self.rooms:
            if room.id == id:
                return room
        return None
    
    def recorrer(self, bloque):
        bloque(self)
        for room in self.rooms:
            room.recorrer(bloque)
    

class Room(MapElement):
    def __init__(self, id):         
        self.north = Wall()
        self.east = Wall()
        self.west = Wall()
        self.south = Wall()
        self.id = id

    def entrar (self, alguien):
        print(alguien, "entrando en la habitación", self.id)

    def esHabitacion(self):
        return True
        
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

    def recorrer(self):
        pass
    
    def enter(self,someone):
        if (self.opened):
            if someone.position == self.side1:
                self.side2.enter(someone)
            else:
                self.side1.enter(someone)
        else:
            print("La puerta "+str(self)+" está cerrada"+"\n")
       
       
    def abrir(self):
        self.opened = True
        
        
    def cerrar(self):
        self.opened = False
      
    def esPuerta(self):
        return True
        
class Wall(MapElement):
    def __init__(self):
        pass # Walls don't need any special attributes
    def entrar(self):
        print("¡No puedes entrar aquí!")

class Bomba (Decorator):
    def __init__(self):
        super().__init__()
        self.active = False

    def print(self):
        print("Bomba")

    def entrar(self, alguien):
        print(alguien + " caminó hacia una bomba")


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

    def __init__(self, vidas, poderes, posicion, modo):
        self.vidas = vidas
        self.poderes = poderes
        self.posicion = None
        self. modo = modo

    def actua(self):
        print("El bicho está actuando...")
        self.modo.actua(self)
        
    def esAgresivo(self):
        return self.modo.esAgresivo()
    
    def esPerezoso(self):
        return self.modo.esPerezoso()
    
    def irNorte(self):
        self.posicion.irNorte(self)
        
    def irEste(self):
        self.posicion.irEste(self)
        
    def irOeste(self):
        self.posicion.irOeste(self) 
        
    def irSur(self):
        self.posicion.irSur(self)

class Modo:

    def __init__(self, nombre):
        self.nombre = nombre

    def actua(self, bicho):
        self.caminar(bicho)
        self.dormir(bicho)
        
    def caminar(self, bicho):
        pass
    
    def dormir(self, bicho):
        time.sleep(4)
        print(bicho, "dormido")
        
    def esAgresivo(self):
        return False
    
    def esPerezoso(self):
        return False
        
class Agresivo(Modo):
    def __init__(self):
        super().__init__("ataque")
        
    def esAgresivo(self):
        return True
    

class Perezoso(Modo):
    def __init__(self):
        super().__init__("defensa")
        
    def esPerezoso(self):
        return True

class Orientacion: 
    
    def __init__(self):
        pass
    
    def poner(self, orientacion): 
        pass
        
class Norte(Orientacion):
    def __init__(self):
        if not Norte._instance:
            super().__init__()
            Norte._instance = self
    
    def poner(self):
        super().poner("norte")
        
    def recorrer(self, bloque, contenedor):
        contenedor.norte.recorrer(bloque)

class Sur(Orientacion):
    def __init__(self):
        if not Sur._instance:
            super().__init__()
            Sur._instance = self
    
    def poner(self):
        super().poner("sur")
        
    def recorrer(self, bloque, contenedor):
        contenedor.sur.recorrer(bloque)
    
class Este(Orientacion):
    def __init__(self):
        if not Este._instance:
            super().__init__()
            Este._instance = self
    
    def poner(self):
        super().poner("este")
        
    def recorrer(self, bloque, contenedor):
        contenedor.este.recorrer(bloque)
    
class Oeste(Orientacion):
    def __init__(self):
        if not Oeste._instance:
            super().__init__()
            Oeste._instance = self
    
    def poner(self):
        super().poner("oeste")
        
    def recorrer(self, bloque, contenedor):
        contenedor.oeste.recorrer(bloque)
        
class Noreste(Orientacion):
    def __init__(self):
        if not Noreste._instance:
            super().__init__()
            Noreste._instance = self

    def poner(self):
        super().poner("noreste")

    def recorrer(self, bloque, contenedor):
        contenedor.noreste.recorrer(bloque)
        
class Noroeste(Orientacion):
    def __init__(self):
        if not Noroeste._instance:
            super().__init__()
            Noroeste._instance = self
            
    def recorrer(self, bloque, contenedor):
        contenedor.noroeste.recorrer(bloque)
        
class Sureste(Orientacion):
    def __init__(self):
        if not Sureste._instance:
            super().__init__()
            Sureste._instance = self

    def recorrer(self, bloque, contenedor):
        contenedor.sureste.recorrer(bloque)
        
class Suroeste(Orientacion):
    def __init__(self):
        if not Suroeste._instance:
            super().__init__()
            Suroeste._instance = self

    def recorrer(self, bloque, contenedor):
        contenedor.suroeste.recorrer(bloque)
        
class Forma:
    def __init__(self):
        self.orientaciones = []
        self.points = None
        self.extent=None
        self.num=None

    def poner(self, forma):
        pass
    
    def recorrer(self, bloque):
        for o in self.orientaciones:
            o.recorrer(bloque, self)
            
class Cuadrado(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.points = None
        self.extent = None
        self.num = None

    def poner(self):
        super().poner("cuadrado")
        
    def irAlNorte(self, alguien):
        self.norte.entrar(alguien)
        
    def irAlSur(self, alguien):
        self.sur.entrar(alguien)
        
    def irAlEste(self, alguien):
        self.este.entrar(alguien)
        
    def irAlOeste(self, alguien):
        self.oeste.entrar(alguien)
    
game = Game()
alguien = "Pepito"
game.make2RoomsMaze()
game.maze.entrar(alguien)

game= Game()
game.make2RoomsMazeFM()


game = BombedGame()
game.make2RoomsMazeFM()
game.maze.entrar(alguien)


