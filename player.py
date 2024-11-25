# Define the Player class.
class Player():
    """
    Cette classe représente un joueur. Un joueur est composé d'un nom et une direction.

    Attributs :
        name (str): Le nom du playeur.
        direction (str): La direction à suivre.

    Méthodes :
        __init__(self, name) : Le constructeur.
        move(self, direction) : Définir la méthode de déplacement.

    Exemples :

    >>> player = Player("Arthur" , "N")
    >>> player.name
    'Arthur'
    >>> player.direction
    'N'
        
    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    