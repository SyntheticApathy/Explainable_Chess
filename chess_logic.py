"""
Use Stockfish to apply chess rules to a given position, get legal moves, best moves, etc **to be finished**
source: https://pypi.org/project/stockfish/
"""
import chess
from stockfish import Stockfish
from typing import List


sf = Stockfish(path="bin/stockfish", depth = 5)
FEN = "8/2k5/2r5/1ppp4/8/1R6/1K6/8 w - - 0 1"


def getLegalMoves(fen:str) -> List[str]:
    FEN = fen
    sf.set_fen_position(FEN)

    #get all legal moves for both players
    moves_preflip = [*sf.get_perft(1)[1]]
    sf.flip()
    moves_postflip = [*sf.get_perft(1)[1]]
   
    return moves_preflip + moves_postflip
    
def get_threat_map(FEN: str, square_name: str):
    """
    Returns a list of all squares a piece at square_name can 'see',
    ignoring whether the target square is same colour.
    """
    board = chess.Board(FEN)
    square_index = chess.parse_square(square_name)
    # .attacks() gives the squares reached by the piece
    attacked_indices = board.attacks(square_index)
    return [chess.square_name(s) for s in attacked_indices]

def get_eval(): #lol
    return sf.get_evaluation()
