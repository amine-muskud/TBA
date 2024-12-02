# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms
        Volcan = Room("Volcan", "Vous vous trouvez au sommet du volcan, vous apercevez au loin plusieurs lieux différents. A l'est, vous apercevez une plage qui semble animée. Au sud, vous apercevez un village. Enfin à l'est vous apercevez une immense jungle. Il serait judicieux de quitter le Volcan au plus vite et d'éviter de vous approchez du bord.")
        self.rooms.append(Volcan)
		
        Chemin = Room("Sentier de terre", "Vous êtes sur un sentier de terre, au sud il vous mène vers un village, à l'ouest vers une plage et à l'est vers une jungle")
        self.rooms.append(Chemin)

        Bord = Room("Bord du volcan", " Vous vous approchez doucement du bord du volcan lorsque vous êtes soudainenement pris de panique après avoir entendu un bruit effrayant, vous glissez et vous tomber dans la lave. Vous êtes mort, il ne fallait décidément pas s'approcher du bord...")
        self.rooms.append(Bord)
		
        Plage = Room("Plage", " Vous arrivez sur une plage bondée de monde. Vous apercevez un camion de glace, un terrain de volley et un peu plus loin un feu de camps. Vous remarquez aussi que le chemin reliant la Plage au Volcan n'est plus accessible " )
        self.rooms.append(Plage)
		
        Village = Room("Village", " Vous arrivez dans un village où vous êtes rapidement acceuilli par les habitants qui vous proposent de faire le tour du village. Vous pouvez ainsi visiter la ferme, la mairie ou en cas de faim aller vous restaurer en Kebab du coin" )
        self.rooms.append(Village)
		
        Jungle = Room("Jungle", " Vous arrivez dans une impressionnante Jungle. Vous apercevez une cabane perchée au loin, une grotte souterraine qui ne demande qu'à être explorée et un impressionant arbre vieux de plus de 100ans")
        self.rooms.append(Jungle)
		
        Kebab = Room(" Keb à Bord", "Vous arrivez au 'Keb à Bord', un délicieux restaurant où vous pouvez manger à votre faim. Il suffit de crier ' Chef ' pour commander " ) 
        self.rooms.append(Kebab)
		
        Mairie = Room(" Mairie du village ", " Vous arrivez dans la Mairie du Village, vous apercevez quelqu'un a l'accueil. Souhaitez-vous aller le voir ?" )
        self.rooms.append(Mairie)
		
        Ferme = Room(" Ferme du village", " Vous arrivez dans la ferme du village. Souhaitez-vous participer aux tâches du jour ? ")
        self.rooms.append(Ferme)
		
        Cabane = Room(" Cabane perchée ", " Vous êtes au pied d'une cabane perchée, souhaitez-vous y monter ? " )
        self.rooms.append(Cabane)
		
        Grotte = Room("Grotte souterraine", " Vous arrivez devant une grotte souterraine, souhaitez-vous y descendre ? " )
        self.rooms.append(Grotte)
		
        Arbre = Room(" Arbre de 100 ans " , " Vous arrivez devant l'arbre de 100 ans, vous apercevez quelque chose au pied de l'arbre. Souhaitez-vous examiner le pied de l'arbre ? " )
        self.rooms.append(Arbre)
		
        Glace = Room("Marchand de glace", " Vous arrivez devant le camion de glace. Vous avez très chaud. Souhaitez-vous vous rafraichir ? ")
        self.rooms.append(Glace)

        Feu = Room("Feu de camps ", " Vous arrivez au niveau d'un feu de camps desert. Vous apercevez un sac à dos abandonné. Souhaitez-vous jeter un coup d'oeil au sac à dos ? " )
        self.rooms.append(Feu)
		
        Volley = Room("Terrain de Volley", " Vous arrivez sur un terrain de volley. Il semblerait qu'une partie s'apprête à commencer. Souhaitez-vous jouer ? " )
        self.rooms.append(Volley)

        Interieur = Room("Interieur de la cabane", " Vous arrivez à l'interieur de la cabane")
        self.rooms.append(Interieur)

        Fgrotte = Room( " Fond de la grotte", " Vous êtes dans le fond de la grotte")
        self.rooms.append(Fgrotte)

        # Create exits for rooms

        Interieur.exits={"D": Cabane, "N" : None, "E" :None, "S" : None, "O" : None,"U": None}

        Volcan.exits = {"D": Chemin, "N" : None, "E" :None, "S" : None, "O" : None,"U": Bord}

        Plage.exits = {"D": None, "N" : Glace, "E" :Chemin, "S" : None, "O" : None,"U": None}

        Feu.exits = {"D":   None, "N" : None, "E" :None, "S" : Glace, "O" : None,"U": None}

        Volley.exits = {"D": None, "N" : None, "E" :Glace, "S" : None, "O" : None,"U": None}

        Glace.exits = {"D": None, "N" : Feu, "E" :None, "S" : None, "O" : Volley,"U": None}

        Village.exits = {"D": None, "N" : Chemin, "E" :None, "S" : Kebab, "O" : Mairie,"U": None}

        Mairie.exits = {"D": None, "N" : None, "E" :Village, "S" : Ferme, "O" : None,"U": None}      

        Ferme.exits = {"D": None, "N" : Mairie, "E" :Kebab, "S" : None, "O" : None,"U": None}

        Kebab.exits = {"D": None, "N" : Village, "E" :None, "S" : None, "O" : Ferme,"U": None}

        Cabane.exits = {"D": None, "N" : None, "E" :None, "S" : None, "O" : Jungle,"U": Interieur}

        Jungle.exits = {"D": None, "N" : None, "E" :Cabane, "S" : None, "O" : Chemin,"U": None}

        Grotte.exits = {"D": Fgrotte, "N" : Jungle, "E" :None, "S" : None, "O" : None,"U": None}

        Fgrotte.exits = {"D": None, "N" : None, "E" :None, "S" : None, "O" : None,"U": Grotte}

        Chemin.exits = {"D": None, "N" : None, "E" :Jungle, "S" : Village, "O" : Plage,"U": Volcan}



        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Volcan

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print("")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
