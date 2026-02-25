""" 
Take in a FEN, parse the positions of the pieces, legal moves, and **more** and upload to the ontology. 


 FEN grammar: **Fields are seperated by a singular space.**  
    1st field: Placement of Pieces:  "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
                - lowercase letter denotes black piece, UPPERCASE denotes white piece.
                - Start from 8th rank, 1 => 8. 
                - Empty squares are denoted by numbers, depending how many empty squares there are between two pieces
                - rows seperated by /
    2nd field: indicates who moves next.  " w "
         "w" = white to move, "b" = black to move. always lowercase.

    3rd field: Castling rights (white|||black) " KQkq "
                - "K" - white can castle kingside
                - "Q" - white can castle queenside
                - "k" - black can castle kingside
                - "q" - black can castle queenside.
                - "-" - neither side can castle
    4th field: en passant      " - "
                - square BEHIND the pawn which has just moved. (ie, if e2 -> e4 then "e3" is added to the fourth field)
                - "-" - no en passant targets are available
    5th field: halfmove " 0 "
                how many moves both players have made since the last pawn advance 
                OR piece capture.
               !! This field is useful to enforce the 50-move draw rule. 
                When this counter reaches 100 (allowing each player to make 50 moves), the game ends in a draw
    6th field: full move " 1 "
                - how many turns in the game.

    example: starting position: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1

source: https://www.chess.com/terms/fen-chess
 """

from owlready2 import get_ontology
from typing import List, DefaultDict
from chess_logic import *

onto = get_ontology("file://BP_ontology.owx").load()



def _input() -> List[str]:
    """Take in FEN from user.
    ::args:: None
    ::Return:: List of strings, each value represents a field. 
    """ 
    print("Enter FEN:")
    FEN:str = input()
    stockfish(FEN)
    return FEN.strip().split(" ", 5)

def upload_position(info: List[str]):
    """Convert FEN to piece positions
    ::args:: info: List[str] : The full information of the board. each value in the list represents a field in FEN. 
    """
    
    board:List[List[str]] = create_board_rep(info[0].split("/"))
    move: str = info[1]
    castling_rights: str = info [2]
    en_passant: str = info[3]
    halfmove: str = info [4]
    fullmove: str = info[5]

    fen_to_class = {
        "p": "Pawn", "n": "Knight", "b": "Bishop", "r": "Rook", "q": "Queen", "k": "King",
        "P": "Pawn", "N": "Knight", "B": "Bishop", "R": "Rook", "Q": "Queen", "K": "King",
    }
    fen_letter = {  # for naming only
        "Pawn": "P", "Knight": "N", "Bishop": "B", "Rook": "R", "Queen": "Q", "King": "K"
    }

    onSquare = onto.onSquare
    WhitePiece = onto.WhitePiece
    BlackPiece = onto.BlackPiece
    legalMove = onto.legalMove

    
    counters = DefaultDict(int)

    for r in range(8):
        for c in range(8):
            ch = board[r][c]
            if ch == ".":
                continue

            piece_cls_name = fen_to_class[ch]
            piece_cls = getattr(onto, piece_cls_name)
            color_cls = WhitePiece if ch.isupper() else BlackPiece
            color_tag = "w" if ch.isupper() else "b"

            file_char = chr(ord("a") + c)
            rank_num = 8 - r
            sq = f"{file_char}{rank_num}"
            sq_ind = getattr(onto, sq)

            counters[(color_tag, piece_cls_name)] += 1
            idx = counters[(color_tag, piece_cls_name)]

            letter = fen_letter[piece_cls_name]
            ind_name = f"{color_tag}{letter}_{idx}"

            piece_ind = onto.Piece(ind_name)
            piece_ind.is_a.append(piece_cls)
            piece_ind.is_a.append(color_cls)
            onSquare[piece_ind] = [sq_ind]
            #legalMove  =  ???? >;c
    onto.save(file="BP_ontology_1.owx")


def create_board_rep(positions:List[str]) -> List[List[str]]:
    """Helper function, converts List of strings to a nice chess board representation
    ::args:: positions: List[str], FEN represntation of all piece positions
    ::Return:: board: List[List[str]], an 8x8 matrix representing the chess board.
    """

    board: List[List[str]] = []

    for r,s in enumerate(positions):
        rank: List[str] = []
        for ch in s: 
            if ch.isdigit():
                rank.extend(["."] * int(ch))

            else: 
                rank.append(ch)
        board.append(rank)
    return board

upload_position(_input())
