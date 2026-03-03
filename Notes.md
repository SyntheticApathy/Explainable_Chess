- SWRL seems useful ? https://en.wikipedia.org/wiki/Semantic_Web_Rule_Language https://owlready2.readthedocs.io/en/latest/rule.html
	- not now, but maybe later
- the chess library is a godsend
- Flush out DL classes. What are the general concepts
	- think of formalisation after description.
	- Row/File as subclasses of square ? Make it easier I think 
- Use FEN for now.(PGN might be more useful for checking with opening database as it stores all the moves, this will make finding the goals easier (middle/early game) removes the need for ML recognition)
- **Focus for now on new players; easy explanation, general concepts**
- Transition states are important, a good move improves position or piece. 
	- Best move for new players $\neq$ Best engine move, improving pieces/position is always good.
- Pawn chains are like super important.
- Focus on Rook
	- Open File
	- Battle on File
	- Passive
	- Active
	- Under Attack
- Modal Logic might be very useful here, create separate ontologies for user questions and then utilise modal logic for answering questions



## Problems


#### DL
- Open File/Rank/Diagonal
	- Might just be easier to do it in python
		- Used python, works now.
- ControlledFile/Rank/Diagonal
	- currently just checks for black, and only if Black has a rook on the file. Needs to be formalised better.
		- Open world problem is annoying
- Active Piece
	- OPEN WORLD PROBLEM AHHHHHHHHHHHHHH
##### DLN
- literally everything.
- Work out basic ruleset for rook first, then expand
	- A Controlled File is only an advantage iff the rook is defended and active.


#### Modal Logic
- This might be more important than originally thought
	- Go n moves deep into a position, get evaluations, describe position (ontology), then go back to original. Apply modal logic to find if a piece move / positional arrangement is necessary.



#### LLM
- For now LLM is local, ssh into pc is kinda iffy ngl; sometimes work sometimes not bcs of the pi.
- Fix Prompt: 
	- Keep temp 0 for now
	- Fix per colour 
	- Get rid of the ontology artefacts
	- expand ruleset
	- maybe less restrictive output.
- llm integration
	- query from onto
	- for now only DL
	- convai + psai helpful here ;3
		- https://www.kaggle.com/code/dawidek123/project-situated-ai-notebook1-up#4.-Instruct-the-LLM-to-produce-the-query-or-components-of-the-query-(e.g.,-keywords)-against-the-KG


#### Queries
- Really bad for now, just query everything. Fix for more specific.
- Split by colour, legal moves aren't 
- important.
	- LLM generated queries? maybe? def for user questions
