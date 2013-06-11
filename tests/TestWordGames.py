import os
import sys

root_path = os.path.abspath(os.path.join(os.path.pardir, os.path.pardir))

if root_path not in sys.path:
    sys.path.append(root_path)

import unittest
from teacher_tools.worksheets.word_games import WordGame


class WordGameTest(unittest.TestCase):
    words = [
        'penguin',
        'cat',
        'lion',
        'tiger',
        'bear',
        'anteater',
        'aardvark',
        'tiltawhirl'
        'bird',
        'party',
        'queen',
        'wandering',
    ]

    def test_create_game(self):
        game = WordGame(self.words)

if __name__ == '__main__':
    unittest.main()