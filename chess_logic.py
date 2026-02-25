"""
Use Stockfish to apply chess rules to a given position, get legal moves, best moves, etc **to be finished**
source: https://pypi.org/project/stockfish/
"""

from stockfish import Stockfish
sf = Stockfish(path="bin/stockfish", depth = 5)


def stockfish(FEN:str):
    sf.set_fen_position(FEN)

    #get all possible moves 
    moves = [*sf.get_perft(1)[1]]
    print(moves)



def test(FEN:str):
    sf.set_fen_position(FEN)
    print(sf.get_perft(1))
    return sf.get_best_move()
