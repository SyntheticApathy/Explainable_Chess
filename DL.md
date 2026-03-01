
# Classes


## All Classes

| Concept                    | Desc                             | Range | Domain |
| -------------------------- | -------------------------------- | ----- | ------ |
| Piece                      | Each piece: has [[#Subclasses]]. |       |        |
| Square                     | All squares on the board.        |       |        |
| Safe King                  |                                  |       |        |
| Weak King                  |                                  |       |        |
| Isolated Pawn              | No pawns on adjacent files       |       |        |
| Pawn Chain                 | Multiple pawns diagonal          |       |        |
| Lines of Sight             |                                  |       |        |
| Open File                  |                                  |       |        |
| Controlled Open File       |                                  |       |        |
| Open File Battle           |                                  |       |        |
| Passive                    |                                  |       |        |
| Controlled Squares         |                                  |       |        |
| King Safety Imbalance      |                                  |       |        |
| Piece Activity             |                                  |       |        |
| Development Lead           |                                  |       |        |
| Space Advantage            |                                  |       |        |
| Initiative                 |                                  |       |        |
| Tempo Gain                 |                                  |       |        |
| Tactical Threat            |                                  |       |        |
| Hanging Piece              |                                  |       |        |
| Overloaded Defender        |                                  |       |        |
| Pinned Piece               |                                  |       |        |
| Skewer Threat              |                                  |       |        |
| Discovered Attack          |                                  |       |        |
| Back Rank Weakness         |                                  |       |        |
| Unprotected Back Rank      |                                  |       |        |
| Weak Square                |                                  |       |        |
| Outpost                    |                                  |       |        |
| Key Square                 |                                  |       |        |
| Dark-Square Weakness       |                                  |       |        |
| Light-Square Weakness      |                                  |       |        |
| Weak Colour Complex        |                                  |       |        |
| Bad Bishop                 |                                  |       |        |
| Good Bishop                |                                  |       |        |
| Knight vs Bishop Advantage |                                  |       |        |
| Rook Activity              |                                  |       |        |
| Queen Activity             |                                  |       |        |
| Coordination               |                                  |       |        |
| Piece Harmony              |                                  |       |        |
| Dominant Piece             |                                  |       |        |
| Restricted Piece           |                                  |       |        |
| Trapped Piece              |                                  |       |        |
| Loose Pieces               |                                  |       |        |
| Defender Shortage          |                                  |       |        |
| Critical Defender          |                                  |       |        |
| Attacking Potential        |                                  |       |        |
| Defensive Resources        |                                  |       |        |
| Counterplay                |                                  |       |        |
| Passed Pawn                |                                  |       |        |
| Connected Passers          |                                  |       |        |
| Backward Pawn              |                                  |       |        |
| Doubled Pawns              |                                  |       |        |
| Pawn Majority              |                                  |       |        |
| Pawn Break                 |                                  |       |        |
| Weak Pawn                  |                                  |       |        |
| Hanging Pawns              |                                  |       |        |
| Open Diagonal              |                                  |       |        |
| Strong Diagonal            |                                  |       |        |
| Open File                  |                                  |       |        |
| Semi-Open File             |                                  |       |        |
| Invasion Square            |                                  |       |        |
| Entry Point                |                                  |       |        |
| Zugzwang Potential         |                                  |       |        |
| Endgame Favorable          |                                  |       |        |
| Transition Advantage       |                                  |       |        |
| Conversion Plan            |                                  |       |        |
| Attack Plan                |                                  |       |        |
| Defense Plan               |                                  |       |        |
| Strategic Threat           |                                  |       |        |
| Tactical Motif Present     |                                  |       |        |
| King Hunt Potential        |                                  |       |        |
| Mate Threat                |                                  |       |        |
| Forced Line Available      |                                  |       |        |
| Sacrifice Candidate        |                                  |       |        |
| Exchange Sacrifice Motif   |                                  |       |        |
| Fortress Potential         |                                  |       |        |
| Perpetual Check Threat     |                                  |       |        |
| Advantage                  |                                  |       |        |
| Disadvantage               |                                  |       |        |
|                            |                                  |       |        |
|                            |                                  |       |        |

## Board Classes

| Name     | Desc                |
| -------- | ------------------- |
| Diagonal | has [[#Subclasses]] |
| File     | has [[#Subclasses]] |
| Rank     | has [[#Subclasses]] |
| Square   | each square         |

## Piece Classes

## Rook Classes 
- build upon this for the baseline variation, so only focus on this for now.



## Subclasses
### Piece subclasses

| Parent Class | Name of Subclass | Desc |     |
| ------------ | ---------------- | ---- | --- |
| Piece        | Bishop           |      |     |
|              | BlackPiece       |      |     |
|              | King             |      |     |
|              | Knight           |      |     |
|              | Pawn             |      |     |
|              | Queen            |      |     |
|              | Rook             |      |     |
|              | WhitePiece       |      |     |


### Board subclasses
| Parent Class | Subclass        | Desc                                         |
| ------------ | --------------- | -------------------------------------------- |
| Diagonal     |                 |                                              |
|              | DiagonalNW      | All diagonals pointing a8 -> h1              |
|              | OpenDiagonal    | A diagonal which doesn't have any pieces     |
|              | Closed Diagonal | A diagonal which does have atleast one piece |
|              | DiagonalNE      | All diagonals pointing a1 -> h8              |
| File         |                 |                                              |
|              | Open File       | A File which does not have any pieces        |
|              | Closed File     | A file which does have pieces                |
| Rank         |                 |                                              |
|              | OpenRank        | A rank which does not have any pieces        |
|              | ClosedRank      | A rank which does have pieces                |
# Obj Properties

| Name        | Desc                                                            | Formalisation          |
| ----------- | --------------------------------------------------------------- | ---------------------- |
| isAttacking | A is attacking B if A has a legal move on the square of B       | done in python         |
| underAttack | A is under Attack if B isAttacking A                            | Inverse of isAttacking |
| legalMove   | all legal moves of a piece                                      | done in python         |
| onSquare    | a piece is on a square.                                         | done in python         |
| isDefending | A is defending B if A can see B AND A and B are the same colour | done in python         |
| hasPiece    | A square s had a piece A if A is on s                           | Inverse of onSquare    |
| hasSquare   | A file or a Row has a square                                    |                        |
