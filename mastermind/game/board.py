import random

class Board:

    def __init__(self):
        """Class constructor.
        
        Args: 
            self(Board): an instance of the Board class.
        """
        self._items = []
        self._code = ''
        #self.prepare(Player.get_name)

    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self(board): an instance of the board class.
            player: player class used to call getname.
        """
        name = player.get_name()
        self._code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items.append([name, guess, hint])
        
    def _create_hint(self, guess):
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

            if self._code[index] == letter:
                hint += "x"

            elif letter in self._code:
                hint += "o"

            else:
                hint += "*"

        return hint

    def print_board(self):
        """Prints the board to the console.
        
        Args:
            self(board): An instance of the board class.
            
        Returns:
            text: Board data is returned to be printed.
        """

        text = "\n--------------------"
        
        for n in self._items:
            text += (f"\nPlayer {n[0]}: {n[1]}, {n[2]}")
        text += "\n--------------------"
        
        return text

    def check_code(self, hint):
        """Checks to see if the guess is the same as the code
        
        Args:
            self(board): an instance of the board class.
        Returns:
            correct(bool): A bool confirming whether or not the guess is true.
        """
        correct = True
        
        if hint == "xxxx":
            correct = False

        return correct