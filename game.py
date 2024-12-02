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
        Volcan = Room("Volcan", "Vous vous trouvez au sommet du volcan, vous apercevez au loin plusieurs lieux différents. A l'est, vous apercevez une plage qui semble animé. Au sud, vous apercevez un village. Enfin à l'est vous apercevez une immense jungle. Il serait judicieux de quitter le Volcan au plus vite et d'éviter de vous approchez du bord.")
        self.rooms.append(Volcan)
		
        Bord = Room("Bord du volcan", " Vous vous approchez doucement du bord du volcan lorsque vous êtes soudainenement pris de panique après avoir entendu un bruit effrayant, vous glissez et vous tomber dans la lave. Vous êtes mort, il ne fallait décidément pas s'approcher du bord...")
        self.rooms.append(Bord)
		
        Plage = Room("Plage", " Vous arrivez sur une plage bondé de monde. Vous apercevez un camion de glace, un terrain de volley et un peu plus loin un feu de camps. Vous remarquez aussi que le chemin reliant la Plage au Volcan n'est plus accessible " )
        self.rooms.append(Plage)
		
        Village = Room("Village", " Vous arrivez dans un village où vous êtes rapidement acceuilli par les habitants qui vous propose de faire le tour du village. Vous pouvez ainsi visiter la ferme, la mairie ou en cas de faim aller vous restaurer en Kebab du coin" )
        self.rooms.append(Village)
		
        Jungle = Room("Jungle", " Vous arrivez dans une impressionnante Jungle. Vous apercevez un cabane perché au loin, une grotte souterraine qui ne demande qu'à être exploré et un impressionant arbre vieux de plus de 100ans")
        self.rooms.append(Jungle)
		
        Kebab = Room(" Keb à Bord", "Vous arrivez au 'Keb à Bord', un délicieux restaurant où vous pouvez manger à votre faim. Il suffit de crier ' Chef ' pour commander " ) 
        self.rooms.append(Kebab)
		
        Mairie = Room(" Mairie du village ", " Vous arrivez dans la Mairie du Village, vous apercevez quelqu'un a l'accueil. Souhaitez-vous allez le voir ?" )
        self.rooms.append(Mairie)
		
        Ferme = Room(" Ferme du village", " Vous arrivez dans la ferme du village. Souhaitez-vous participer aux tâches du jour ? ")
        self.rooms.append(Ferme)
		
        Cabane = Room(" Cabane perché ", " Vous êtes au pieds d'un cabane perché, souhaitez-vous y monter ? " )
        self.rooms.append(Cabane)
		
        Grotte = Room("Grotte souterraine", " Vous arrivez devant une grotte souterraine, souhaitez-vous y descendre ? " )
        self.rooms.append(Grotte)
		
        Arbre = Room(" Arbre de 100 ans " , " Vous arrivez devant l'arbre de 100 ans, vous apercevez quelque chose au pieds de l'arbre. Souhaitez-vous examiner le pieds de l'arbre ? " )
        self.rooms.append(Arbre)
		
        Glace = Room("Marchand de glace", " Vous arrivez devant le camion de glace. Vous avez très chaud. Souhaitez-vous vous rafraichir ? ")
        self.rooms.append(Glace)

        Feu = Room("Feu de camps ", " Vous arrivez au niveau d'un feu de camps desert. Vous apercevez un sac à dos abandonnées. Souhaitez-vous jeter un coup d'oeil au sac à dos ? " )
        self.rooms.append(Feu)
		
        Volley = Room("Terrain de Volley", " Vous apercevez un terrain de volley. Il semblerait qu'une partie s'apprête à commencer. Souhaitez-vous jouer ? " )
        self.rooms.append(Volley)

        Interieur = Room("Interieur de la cabane", " Vous arrivez à l'interieur de la cabane")
        self.rooms.append(Interieur)

        # Create exits for rooms

        Interieur.exits={"DOWN": Cabane, "N" : None, "E" :None, "S" : None, "O" : None}

        Volcan.exits = {"N" : None, "E" : Jungle, "S" : Village, "O" : Plage,"Bord" : Bord}

        Plage.exits = {"Feu_de_camp" : Feu, "Volley" : Volley, "Marchand_de_glaces" : Glace, "Chemin_village" : Village,"N" : None, "E" :None, "S" : None, "O" : None}

        Feu.exits = {"Volley" : Volley, "Marchand_de_glaces" : Glace, "Chemin_village" : Village,"N" : None, "E" :None, "S" : None, "O" : None}

        Volley.exits = {"Feu_de_camp" : Feu, "Marchand_de_glaces" : Glace, "Chemin_village" : Village,"N" : None, "E" :None, "S" : None, "O" : None}

        Glace.exits = {"Feu_de_camp" : Feu, "Volley" : Volley, "Chemin_village" : Village,"N" : None, "E" :None, "S" : None, "O" : None}

        Village.exits = {"Mairie" : Mairie, "Ferme" : Ferme, "Kebab" : Kebab, "Chemin_plage" : Plage, "N" : Volcan, "E" :None, "S" : None, "O" : None}

        Mairie.exits = {"Ferme" : Ferme, "Kebab" : Kebab, "Chemin_plage" : Plage, "N" : Volcan,"E" :None, "S" : None, "O" : None}      

        Ferme.exits = {"Mairie" : Mairie, "Kebab" : Kebab, "Chemin_plage" : Plage, "N" : Volcan, "E" :None, "S" : None, "O" : None}

        Kebab.exits = {"Mairie" : Mairie, "Ferme" : Ferme, "Chemin_plage" : Plage, "N" : Volcan,"E" :None, "S" : None, "O" : None}

        Jungle.exits = {"UP" : Cabane, "DOWN" : Grotte, " Arbre'" : Arbre, "O" : Volcan,"N" : None, "E" :None, "S" : None}

        Cabane.exits = {"DOWN" : Grotte, "Arbre'" : Arbre, "O" : Volcan, "UP" : Interieur,"N" : None, "E" :None, "S" : None}

        Grotte.exits = {"UP" : Cabane, "Arbre" : Arbre, "O" : Volcan,"N" : None, "E" :None, "S" : None}

        Arbre.exits = {"UP" : Cabane, "DOWN" : Grotte, "O" : Volcan,"N" : None, "E" :None, "S" : None}



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
            ####if len(list_of_words)==2:
             ###   direction_word = list_of_words[1]
              ##  if direction_word not in self.rooms:
               #     print(" Il n'est pas possible d'aller dans cette direction !")

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
