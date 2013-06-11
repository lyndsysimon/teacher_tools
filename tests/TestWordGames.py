import os
import sys

root_path = os.path.abspath(os.path.join(os.path.pardir, os.path.pardir))

if root_path not in sys.path:
    sys.path.append(root_path)

import unittest
from teacher_tools.worksheets.word_games import WordGame


class WordGameTest(unittest.TestCase):
    words = [
        'cat',
    ]
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_game(self):
        game = WordGame()

    def test_add_word(self):
        game = WordGame()
        game.add_word(self.words[0])
        self.assertEqual(len(game.words), 1)
        self.assertEqual(game.words[0]['word'], self.words[0])

    def test_create_scramble(self):
        game = WordGame()
        game.add_word(self.words[0])
        self.assertEqual(len(game.words), 1)
        scramble = game.create_scramble()



if __name__ == '__main__':
    unittest.main()