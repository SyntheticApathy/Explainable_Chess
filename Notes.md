- Flush out DL classes. What are the general concepts?
	- think of formalisation after description.
- Use FEN for now.(PGN might be more useful for checking with opening database as it stores all the moves, this will make finding the goals easier (middle/early game) removes the need for ML recognition)
- Focus for now on new players; easy explanation, general concepts
- Transition states are important, a good move improves position or piece. 
	- Best move for new players $\neq$ Best engine move, improving pieces/position is always good.
- Pawn chains are like super important.
- Focus on Rook
	- Open File
	- Battle on File
	- Passive
	- Active
	- Under Attack



## Problems
- legalMove doesn't encode special moves: castling(two moves at once), promotion.
	- these are exceptions to normal moves, but is it really needed?
- Think of how to implement legalMoves
	- isAttacking comes from that (legalMove piece $\to$ piece or maybe square?)