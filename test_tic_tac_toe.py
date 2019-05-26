from tic_tac_toe import Board
from tic_tac_toe import HumanPlayer
from tic_tac_toe import ComputerPlayer
import unittest


# Testes para o tabuleiro. Nao importa quem e o jogador.
class Test_Board(unittest.TestCase):
    def test_EmptyBoard(self):
        # Niguem joga nenhuma posicao.
        # Todas as posicoes sao livres.
        board = Board()
        for row in range(3):
            for col in range(3):
                self.assertTrue(board.IsFree(row, col))

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


class Test_HumanPlayer(unittest.TestCase):
    def test_IsValidForDigit(self):
        # Verifique que IsValid() retorne true se e um int >=0, <9.
        board = Board()
        human_player = HumanPlayer(player_id="x")
        for val in range(9):
            self.assertTrue(board, human_player.IsValid(board, chr(val)))

    def test_IsValidForBadInput(self):
        # Verifique que IsValid() retorne false se nao e int >=0, <9.
        board = Board()
        human_player = HumanPlayer(player_id="x")
        self.assertFalse(human_player.IsValid(board, "a"))

        # TODO(doug): Verify for all sorts of bad input...

    def test_Id(self):
        # Verifique que o ID do jogador esta correto.
        player_id = "human_id"
        human_player = HumanPlayer(player_id=player_id)
        self.assertEqual(player_id, human_player.Id())


# Nao tem que testar cada funcion, mas tem que testar se o algoritmo funciona
# correto. Nao importa como ele foi escrito (que temos uma funcion HumanCanWin,
# etc. So e importante que o ComputerPlayer vai escolher a melhor posicao.
class Test_ComputerPlayer(unittest.TestCase):
    def test_PlayerId(self):
        computer_player = ComputerPlayer(computer_id="x", human_id="o")
        self.assertEqual(computer_player.Id(), "x")

    def test_EscolheParaGanharComLinha(self):
        board = Board()
        player_id = "x"
        computer_player = ComputerPlayer(computer_id=player_id, human_id="o")
        # Set pattern:
        #  * | x | x       Expect (0, 0)
        # ---+---+---
        #    |   |
        # ---+---+---
        #    |   |
        board.PlayPosition(0, 1, player_id)
        board.PlayPosition(0, 2, player_id)
        computer_player.Play(board)
        self.assertTrue(board.HasPosition(0, 0, player_id))
        self.assertTrue(board.PlayerWon(player_id))

    def test_EscolheParaGanharComColuna(self):
        board = Board()
        player_id = "x"
        computer_player = ComputerPlayer(computer_id=player_id, human_id="o")
        # Set pattern:
        #    | x |       Expect (2, 1)
        # ---+---+---
        #    | x |
        # ---+---+---
        #    | * |

        # TODO(doug)

    def test_EscolheParaGanharComTraversal(self):
        board = Board()
        player_id = "x"
        computer_player = ComputerPlayer(computer_id=player_id, human_id="o")
        # Set pattern:
        #  x |   |        Expect (2, 2)
        # ---+---+---
        #    | x |
        # ---+---+---
        #    |   | *

        # TODO(doug)

    def test_EscolheParaGanharComLinha(self):
        board = Board()
        player_id = "x"
        computer_player = ComputerPlayer(computer_id=player_id, human_id="o")
        # Set pattern:
        #    |   | x       Expect (0, 2)
        # ---+---+---
        #    | x |
        # ---+---+---
        #  * |   |

        # TODO(doug)

    def test_NaoDeixaOutroJogadorVencerComLinha(self):
        board = Board()
        player_id = "x"
        other_player_id = "o"
        computer_player = ComputerPlayer(computer_id=player_id,
                                         human_id=other_player_id)
        # Set pattern:
        #  * | o | o       Expect (0, 0) to be "x"
        # ---+---+---
        #    |   |
        # ---+---+---
        #    |   |
        board.PlayPosition(0, 1, other_player_id)
        board.PlayPosition(0, 2, other_player_id)
        computer_player.Play(board)
        self.assertTrue(board.HasPosition(0, 0, player_id))

    def test_NaoDeixaOutroJogadorVencerComColuna(self):
        board = Board()
        player_id = "x"
        other_player_id = "o"
        computer_player = ComputerPlayer(computer_id=player_id,
                                         human_id=other_player_id)
        # Set pattern:
        #    | o |        Expect (2, 1) to be "x"
        # ---+---+---
        #    | o |
        # ---+---+---
        #    | * |

        # TODO(doug)

    def test_NaoDeixaOutroJogadorVencerComTraversal(self):
        board = Board()
        player_id = "x"
        other_player_id = "o"
        computer_player = ComputerPlayer(computer_id=player_id,
                                         human_id=other_player_id)
        # Set pattern:
        #  o |   |        Expect (2, 2) to be "x"
        # ---+---+---
        #    | o |
        # ---+---+---
        #    |   | *

        # TODO(doug)

    def test_NaoDeixaOutroJogadorVencerComOutroTraversal(self):
        board = Board()
        player_id = "x"
        other_player_id = "o"
        computer_player = ComputerPlayer(computer_id=player_id,
                                         human_id=other_player_id)
        # Set pattern:
        #    |   | o       Expect (2, 0) to be "x"
        # ---+---+---
        #    | o |
        # ---+---+---
        #  * |   |

        # TODO(doug)

    def test_VaiJogarParaVencerEmVezDeBloquar(self):
        board = Board()
        player_id = "x"
        other_player_id = "o"
        computer_player = ComputerPlayer(computer_id=player_id,
                                         human_id=other_player_id)
        # Set pattern:
        #    | o | o       Expect (2, 2) to be "x"
        # ---+---+---
        #    |   |
        # ---+---+---
        #  x | x | *
        board.PlayPosition(0, 1, other_player_id)
        board.PlayPosition(0, 2, other_player_id)
        board.PlayPosition(2, 0, player_id)
        board.PlayPosition(2, 1, player_id)
        computer_player.Play(board)
        self.assertTrue(board.HasPosition(2, 2, player_id))
        self.assertTrue(board.PlayerWon(player_id))


if __name__ == '__main__':
    unittest.main()
