from collections import namedtuple
from datetime import datetime
from random import SystemRandom

# Custom, verbose type for a single grid element
GridPoint = namedtuple(
    typename='GridPoint',
    field_names=['x','y','letter']
)

PlacedWord = namedtuple(
    typename='PlacedWord',
    field_names=['word','points']
)

rand = SystemRandom(datetime.now()).randint

class WordGame(object):
    '''
    A `WordGame` contains a list of words, which can be used to generate one or
    more `WordGameBoard`s
    '''

    def __init__(
        self,
        words=None,
        rows=None,
        columns=None,
        allow_reversed=False,
        allow_diagonal=False,
    ):
        self.words = []
        if words:
            for word in words:
                self.add_word(word)



    def add_word(self, word, definition=None):
        self.words.append({
            'word': word,
            'definition': definition
        })

    def create_scramble(self,rows=None,columns=None):

        calculated_dimensions = int(max(
            [len(x['word']) for x in self.words]
        ) * 1.5)

        board = WordGameBoard(
            rows=rows or calculated_dimensions,
            cols=columns or calculated_dimensions,
            words=[x['word'] for x in self.words]
        )
        return board.output_scramble()


class WordGameBoard(object):
    '''
    A single board, with `GameWords` arranged so that overlaps may consist of
    zero or one letters. Contains a list of `WordGameWord`s.
    '''

    orientations = ['horizontal', 'vertical']

    def __init__(self,rows,cols,words):
        self.placed_words = []
        self.rows = rows
        self.cols = cols

        for word in words:
            self._place_word(word)

    def output_scramble(self):
        grid = []
        for row in range(self.rows):
            grid.append([])
            for col in range(self.cols):
                grid[row].append('-')

        filled = self._coords_filled()
        for (x,y) in filled:
            grid[x][y] = filled[(x,y)]
        return grid


        #print(repr(self.placed_words))

    def _coords_filled(self):
        coords = {}
        words = [word.points for word in self.placed_words]
        for word in words:
            for letter in word:
                coords[(letter.x,letter.y)] = letter.letter
        return coords

    def _place_word(self, word):
        orientation = self.orientations[rand(0,len(self.orientations)-1)]
        # TESTING
        orientation = 'horizontal'

        if orientation == 'horizontal':
            max_begin_column = (self.cols - len(word)) - 1
            column = rand(0,max_begin_column)
            row = rand(0,self.rows -1)
            points = []

            for offset, letter in enumerate(word):
                points.append(GridPoint(y=column+offset,x=row,letter=letter))

        self.placed_words.append(PlacedWord(word=word,points=points))