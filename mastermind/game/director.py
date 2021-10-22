from game.board import Board
from game.console import Console
from game.player import Player
from game.roster import Roster

class Director:
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._player_won = False
        self._roster = Roster()
        self._guess_limit = 20


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        self._board.print_board()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        
        if (self._player_won):
            self._console.write(f'\n{self._roster.get_current().get_name()} won!')
        else:
            self._console.write('Game Over. Turn Limit Reached.')

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
            self._board.prepare(player)
        # Advances current index to 0
        self._roster.next_player()

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.
        Args:
            self (Director): An instance of Director.
        """
        self._console.write(f'{self._roster.get_current().get_name()}\'s turn:')
        self._roster.get_current().set_guess(self._console.read('What is your guess? '))
        

    def _do_updates(self):
        """Processes the inputs from the beginning of each round of play. Updates variables
        as necessary.
        Args:
            self (Director): An instance of Director.
        """
        index = self._roster.current
        self._board._items[index][1] = self._roster.get_current().get_guess()
        self._board._items[index][2] = self._board._create_hint(self._roster.get_current().get_guess())
        self._keep_playing = self._board.check_code(self._board._items[index][2])
        if (self._keep_playing):
            self._roster.next_player()
            if (self._guess_limit == 1):
                self._keep_playing = False
            else: 
                self._guess_limit -= 1
        else:
            self._player_won = True

    def _do_outputs(self):
        """Prints the outputs at the end of each round of play. Utilizing the 
        updates from the previous function.
        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        board = self._board.print_board()
        self._console.write(board)
        self._console.write(f'Guesses Remaining: {self._guess_limit}')