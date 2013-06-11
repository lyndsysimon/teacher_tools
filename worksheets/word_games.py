from collections import namedtuple
from datetime import datetime
from random import SystemRandom

# Custom, verbose type for a single grid element
GameBoardGridPoint = namedtuple(
    typename='GridPoint',
    field_names=['x','y']
)

rand = SystemRandom(datetime.now()).randint

class WordGame(object):
    '''
    A `WordGame` contains a list of words, which can be used to generate one or
    more `WordGameBoard`s
    '''

    def __init__(
        self,
        words=[],
        rows=None,
        columns=None,
        allow_reversed=False,
        allow_diagonal=False,
    ):
        self.words = words


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
        return board.output()


class WordGameBoard(object):
    '''
    A single board, with `GameWords` arranged so that overlaps may consist of
    zero or one letters. Contains a list of `WordGameWord`s.
    '''

    placed_words = []
    orientations = ['horizontal', 'vertical']

    def __init__(self,rows,cols,words):
        self.rows = rows
        self.cols = cols