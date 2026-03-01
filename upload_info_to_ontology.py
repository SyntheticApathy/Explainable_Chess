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

    example: starting position: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

source: https://www.chess.com/terms/fen-chess
 """

from owlready2 import get_ontology
from typing import List, DefaultDict
from chess_logic import *

onto = get_ontology("BP_ontology.owx").load()



def _input():
    """Take in FEN from user.
    ::args:: None
    ::Return:: The new Ontology
    """ 
    print("Enter FEN:")
    FEN:str = input()
    
    legal_moves = getLegalMoves(FEN)
    return upload_position(FEN.strip().split(" ", 5), legal_moves)
    

def upload_position(info: List[str], legal_moves):
    """Convert FEN to piece positions
    ::args:: info: List[str] : The full information of the board. each value in the list represents a field in FEN.
             legal_moves: List[str] : The list of all legal moves for a player in this position.
    ::Return:: The new Ontology
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
    
    

    
    counters = DefaultDict(int)
    cntr:int = 0
    created_pieces = []
    
    for r in range(8):
        for c in range(8):
            ch = board[r][c]
            
            #get current square name
            file_char = chr(ord("a") + c)
            rank_num = 8 - r
            sq = f"{file_char}{rank_num}"
            sq_ind = getattr(onto, sq)
            
            if ch == ".":
                sq_ind.isEmpty = [True]
                continue
            sq_ind.isEmpty = [False]
            piece_cls_name = fen_to_class[ch]
            piece_cls = getattr(onto, piece_cls_name)
            color_cls = WhitePiece if ch.isupper() else BlackPiece
            color_tag = "w" if ch.isupper() else "b"





            #create piece
            counters[(color_tag, piece_cls_name)] += 1
            idx = counters[(color_tag, piece_cls_name)]
            letter = fen_letter[piece_cls_name]
            ind_name = f"{color_tag}{letter}_{idx}"
            piece_ind = onto.Piece(ind_name)
            piece_ind.is_a.append(piece_cls)
            piece_ind.is_a.append(color_cls)

            #on square
            onSquare[piece_ind] = [sq_ind]
            #store in array so we can then access it to check for properties
            piece_ind.temp_sq = sq
            created_pieces.append(piece_ind)
    
    for piece in created_pieces:
            
 #     ACTUAL LEGAL MOVES (From Stockfish)
        moves = [m for m in legal_moves if m.startswith(piece.temp_sq)]
        for m in moves:
            dest_sq_ind = getattr(onto, m[2:4])
            piece.legalMove.append(dest_sq_ind)

        # THREAT ZONE (Attacking and Defending)
        # Get all squares this piece 'points' at, including teammates
        threatened_squares = get_threat_map(" ".join(info), piece.temp_sq)

        for sq_name in threatened_squares:
            dest_sq_ind = getattr(onto, sq_name)
            target_piece = onto.search_one(onSquare=dest_sq_ind)

            if target_piece:
                # Check for color matching
                is_white = onto.WhitePiece in piece.is_a
                target_is_white = onto.WhitePiece in target_piece.is_a
                target_is_black = onto.BlackPiece in target_piece.is_a

                if (is_white and target_is_black) or (not is_white and target_is_white):
                    # Enemy color = Attacking
                    piece.isAttacking.append(target_piece)
                elif (is_white and target_is_white) or (not is_white and target_is_black):
                    # Same color = Defending
                    piece.isDefending.append(target_piece)
        del piece.temp_sq


            

    onto.save(file=f"Ontologies/udpated_ontology{cntr}.owx")
    onto1 = get_ontology(f"Ontologies/udpated_ontology{cntr}.owx").load()

    cntr+=1
    
   
    
    return onto1


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
    
    for r in board:
        print(r)


    return board


