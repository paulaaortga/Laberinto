# LABERINTO

Patrón Builder:

    Se crea el proyecto builder con las clases Director y LaberintoBuilder

Patrón Decorator:

    Añadida la clase Decorator

Patrón Composite: 

     Se crean las clases ElementoMapa, Contenedor y Hoja

Patrón Singleton: 

    Se crea la clase Orientación y las subclases Norte, Sur, Este y Oeste

Patrón Factory Method: 

    Se crean varios métodos de fabricación dentro de la clase juego 

Patrón Strategy: 

    Creamos la clase Modo con dos subclases Agresivo y Perezoso en las que añadimos sus respectivos métodos

Patrón Iterator: en el caso del laberinto aplicados dicho patrón con un iterador interno, en este caso implementamos el método recorrer

Patrón State:

    Este patrón se ha implementado en la puerta agregando un EstadoPuerta que a su vez tiene dos subclases: Abierta y Cerrada. El State también
    se ve en la clase Ente de la cual tenemos dos tipos: Vivo y Muerto.

Patrón Template Method: 

    Es aplicado en la clase Modo con un método plantilla en este caso actua(), a partir de ese método los bichos desarrollan más habilidades como dormir, atacaar 
    o caminar.

Patrón Observer: 

    Es aplicado añadiendo una nueva clase llamada LaberintoGUI, a través de este patrón implementaremos la vista del juego 
