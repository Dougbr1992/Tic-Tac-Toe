from tic_tac_toe import Board
import unittest

class Test_tic_tac_toe(unittest.TestCase):


    def test_has_position(self):

        has_position = Board.HasPosition(0, 0, 1)

        self.assertEqual(has_position, True)



if __name__ == '__main__':
    unittest.main()
