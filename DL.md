
# Classes


## All Classes

| Concept                    | Desc                             | Range | Domain |
| -------------------------- | -------------------------------- | ----- | ------ |
| Piece                      | Each piece: has [[#Subclasses]]. |       |        |
| Square                     | All squares on the board.        |       |        |
| Under Attack               |                                  |       |        |
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
| Disadvana                  |                                  |       |        |
|                            |                                  |       |        |

### Rook Classes 
build upon this for the baseline variation, so only focus on this for now.

| Class                | Desc |
| -------------------- | ---- |
| Open File            |      |
| Controlled Open File |      |
| Open File Battle     |      |
| Piece Activity       |      |
| Passive              |      |
| Active               |      |
| Under Attack         |      |
|                      |      |


## Subclasses

| Parent Class | Name of Subclass |
| ------------ | ---------------- |
| Piece        | Bishop           |
|              | BlackPiece       |
|              | King             |
|              | Knight           |
|              | Pawn             |
|              | Queen            |
|              | Rook             |
|              | WhitePiece       |
|              |                  |

# Obj Properties

| Name        | Desc                                                            |                     |
| ----------- | --------------------------------------------------------------- | ------------------- |
| isAttacking | A is attacking B if A has a legal move on the square of B       | done in python      |
| legalMove   | all legal moves of a piece                                      |                     |
| onSquare    | a piece is on a square.                                         |                     |
| isDefending | A is defending B if A can see B AND A and B are the same colour |                     |
| hasPiece    | A square s had a piece A if A is on s                           | Inverse of onSquare |
