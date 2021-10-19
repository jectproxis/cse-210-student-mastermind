import random

class Board:

    def __init__(self):
        """Class constructor.
        
        Args: 
            self(Board): an instance of the Board class.
        """
        self._items = []

    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self(board): an instance of the board class.
            player: player class used to call getname.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]
        
    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.
        
        Args:
            self(Board): An instance of the board class.
            code(string): The code to compare the guess with.
            guess(string): The guess that was made.
            
        Returns:
            string: A hint in the form [xxxx]
        """

        hint = ""

        for index, letter in enumerate(guess):

            if code[index] == letter:
                hint += "x"

            elif letter in code:
                hint += "o"

            else:
                hint += "*"

        return hint

    def print_board(self, player):
        """Prints the board to the console.
        
        Args:
            self(board): An instance of the board class.
            
        Returns:
            text: Board data is returned to be printed.
        """

        text = "\n--------------------"

        for items, words in enumerate(self._items):
            text += (f"\nPlayer {player.get_name}: {self._items[1]}, {self._items[2]}")


    