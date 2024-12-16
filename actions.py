# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        # Get the direction from the list of words.
        #direction = list_of_words[1]
        if list_of_words[1] in ['E', 'e', 'est', 'Est', 'EST'] :
            list_of_words[1] = 'E'
        if list_of_words[1] in ['S', 's', 'sud', 'Sud', 'SUD'] :
             list_of_words[1] = 'S'
        if list_of_words[1] in ['O', 'o', 'ouest', 'Ouest', 'OUEST'] :
             list_of_words[1] = 'O'
        if list_of_words[1] in ['N', 'n', 'nord', 'Nord', 'NORD'] :
             list_of_words[1] = 'N'
        if list_of_words[1] in ['U', 'u', 'up', 'Up', 'UP'] :
             list_of_words[1] = 'U'
        if list_of_words[1] in ['D', 'd', 'Down', 'DOWN', 'down'] :
             list_of_words[1] = 'D'
#
        direction = list_of_words[1]
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

        def back(game, list_of_words,number_of_parameters):
            player = game.player
            size = len(player.history)
            if size == 0:
                print(" Le retour en arrière est impossible !")
            else:
                lieu_precedent = player.history[-1]
                values = lieu_precedent.exits.values()
                keys = lieu_precedent.exits.keys()
                taille = len(values)
                for i in range(taille):
                    if values[i] == lieu_precedent :
                        direction = keys(i)
                        if direction == 'E' :
                            direction = "O"
                        if direction == 'O' :
                            direction = "E"
                        if direction == 'N' :
                            direction = "S"
                        if direction == 'S' :
                            direction = "N"
                        if direction == 'U' :
                            direction = "D"
                        if direction == 'D' :
                            direction = "U"
                        game.process_command( " go " + str(direction))