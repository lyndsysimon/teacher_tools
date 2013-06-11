from collections import namedtuple
from datetime import datetime
from random import SystemRandom

# Custom, verbose type for a single grid element
GameBoardGridPoint = namedtuple(
    typename='GridPoint',
    field_names=['x','y']
)

class WordGame(object):
    '''
    A `WordGame` contains a list of words, which can be used to generate one or
    more `WordGameBoard`s
    '''

    def __init__(
        self,
        word_list=[],
        rows=None,
        columns=None,
        allow_reversed=False,
        allow_diagonal=False,
    ):
        self._rand = SystemRandom(datetime.now()).randint

        self.word_list = word_list
        self._update_dimensions()

    orientations = ['horizontal', 'vertical']

    def create_board(self,rows=None,columns=None):
        # If rows or columns passed, make sure they're big enough
        if rows is not None and rows < self.min_dimensions:
            raise ValueError(
                'Game board must be at least %s rows' % self.min_dimensions)
        if columns is not None and columns < self.min_dimensions:
            raise ValueError(
                'Game board must be at least %s columns' % self.min_dimensions)

        rows = rows or self.min_dimensions
        columns = columns or self.min_dimensions

        board = dict()
        for word in self.word_list:
            board = self._place_word_horizontal(word, board, rows, columns)

        return board

    def _update_dimensions(self):
        '''
        Taking into account the words in word_list, update minimum dimensions
        '''
        # Update dimensions
        self.min_dimensions = int(max([len(x) for x in self.word_list]) * 1.5)

    def _place_word_horizontal(self, word, board, rows, cols):
        '''
        Place a word on the game board, horinzontally
        '''
        word_position = {}

        # get start column
        max_valid_column = (cols - len(word)) - 1
        start_column = self._rand(0, max_valid_column)

        # get row
        start_row = self._rand(0, rows - 1)

        for offset, letter in enumerate(word):
            word_position[
                GridPoint(x=start_column + offset, y=start_row)
            ] = letter

        board.update(word_position)

        return board

class GameWord(object):
    def __init__(self, word, points):
        self.word = word
        self.points = points

class WordGameBoard(object):
    '''
    A single board, with `GameWords` arranged so that overlaps may consist of
    zero or one letters. Contains a list of `WordGameWord`s.
    '''
    def __init__(self,rows,cols):
        grid = []
        for x in range(cols):
            grid.append([])
            for y in range(rows):
                grid[x].append(None)
        self.grid = grid

    words = []

    def add_word(self, word):
        for x in self.words:
            # check if two or more points overlap
            if (x.points & word.points) > 1:
                raise OverlapError()

        # make sure overlapping points contain the same letters


        self.words.append(word)

    def _debug(self):
        for y in range(len(self.grid)):
            line = ['']
            for x in range(len(self.grid[y])):
                if self.grid[x][y] is None:
                    line.append('-')
                else:
                    line.append(self.grid[x][y])
            print(''.join(line))