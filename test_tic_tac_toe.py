from tic_tac_toe import Board
import unittest

# Testes para o tabuleiho. Nao importo quem e o jogador. 
class Test_tic_tac_toe(unittest.TestCase):
    def test_EmptyBoard(self):
        # Niguem joga nenhuma posicao.
        # Todas as posicoes sao livres.
        board = Board()
        for row in range(3):
            for col in range(3):		
                self.assertTrue(board.IsFree(row,col))
    
    def test_PlayedPosition(self):
        # Um jogador vai jogar uma posicao... Teste se a mudansa foi feita no
        # tabuleiro. Repare que a valor do "player_id" nao importa.
        board = Board()
        player_id = "x" 
        row = 2
        col = 1
        board.PlayPosition(row, col, player_id)
        self.assertTrue(board.HasPosition(row, col, player_id))
        self.assertFalse(board.IsFree(row, col))

    def test_PlayerWinsWithDiagonal(self):
        # Um jogador vai jogar 3 posicoes na transversal. Teste que assim vai
        # vencer com diagonal, e nao com linha ou coluna.
        board = Board()
        player_id = "x"
        board.PlayPosition(0, 0, player_id)
        board.PlayPosition(1, 1, player_id)
        board.PlayPosition(2, 2, player_id)

        self.assertTrue(board.WonWithTransversal(player_id))
        self.assertFalse(board.WonWithRow(player_id))
        self.assertFalse(board.WonWithCol(player_id))

    def test_PlayerWinsWithOtherDiagonal(self):
        # Um jogador vai jogar 3 posicoes na transversal. Teste que assim vai
        # vencer com diagonal, e nao com linha ou coluna.
        board = Board()
        player_id = "x"
        board.PlayPosition(2, 0, player_id)
        board.PlayPosition(1, 1, player_id)
        board.PlayPosition(0, 2, player_id)

        self.assertTrue(board.WonWithTransversal(player_id))
        self.assertFalse(board.WonWithRow(player_id))
        self.assertFalse(board.WonWithCol(player_id))

    def test_PlayerWinsWithRow(self):
        # TODO(doug): Test the following for every possible row:
        #  - WonWithRow() returns true.
        #  - PlayerWon() returns true.
        #  - WonWithCol() returns false.
        #  - WonWithTransversal() returns false.
        pass

    def test_PlayerWinsWithCol(self):
        # TODO(doug): Same but with columns.
        pass



if __name__ == '__main__':
    unittest.main()
