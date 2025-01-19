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
        if size >= 1 :
            last_room = game.player.history.pop()
            game.player.current_room = last_room
            print(game.player.current_room.get_long_description())
            return True

    def look(game, list_of_words,number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        lieu_actuel = game.player.current_room
        lieu_actuel.get_inventory()
        return True

    def take(game, list_of_words,number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        item_name = list_of_words[1]
        player = game.player
        current_room = player.current_room

        item = None
        for obj in current_room.inventory:
            if obj.name == item_name:
                item = obj
                break

        if item is None:
            print(f"L'objet : {item_name} n'est pas présent dans la salle.")
            return False

        i = 0
        for items in player.inventory :
            i = i + items.weight
        if i + item.weight > player.max_weight:
            print("L'objet est trop lourd ! Il va falloir vous décharger de quelques affaires...")
            return False
        else:

            current_room.inventory.remove(item)
            player.inventory[item] = item.description
            print(f"Vous avez récuperé l'objet : {item.name} .")
            return True


    def check(game, list_of_words,number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        game.player.get_inventory()
        return True
    
    def drop(game, list_of_words,number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        item_name = list_of_words[1]
        player = game.player
        current_room = player.current_room

        item = None
        for obj in player.inventory:
            if obj.name == item_name:
                item = obj
                break

        if item is None:
            print(f"L'objet : {item_name} n'est pas présent dans votre inventaire.")
            return False
        
        else:
            current_room.inventory.add(item)
            player.inventory.pop(item)
            print(f"Vous avez jeté l'objet : {item.name} .")
            return True
        

    def talk(game, list_of_words,number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        character_name = list_of_words[1]
        current_room = game.player.current_room
        character = None

        if character_name not in current_room.characters:
            print(f"{character_name} n'est pas dans cette pièce.")
            return False
        character = current_room.characters[character_name]
        message = character.get_msg()
        print(f"{character_name} s'adresse à vous : {message}")
        return True