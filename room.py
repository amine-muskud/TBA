# Define the Room class.

class Room:
    """
    Cette classe représente les différentes salles accessibles. Une salle est définie par son nom "name" et sa description "description"
    
    Attributs:
        name (str) : Le nom de la salle
        description (str) : la description de ce que contient la salle
        direction (str) : Correspond à une direction à suivre ( NORD, SUD, EST, OUEST)
    
    Méthodes:
        __init__(self,name,description) : Le constructeur
        get_exit(self,direction) : Donne la sortie qu'on obtient pour une direction donnée ( si la sortie existe )
        get_exit_string(self) : Donnes les différentes sorties possibles pour la salle dans laquelle on se trouve
        get_long_description(self) : Donne la description de la salle ainsi que les différentes sorties possibles
    
    Examples:

    >>> room = Room("nom de la salle", "description de la salle" )
    >>> room.name
    "nom de la salle"
    >>> room.description
    "description de la salle"
    """
    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
