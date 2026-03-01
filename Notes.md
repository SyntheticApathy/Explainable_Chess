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



## Problems
#### DL
- isDefending implementation


#### LLM
- For now LLM is local, ssh into pc is kinda iffy ngl; sometimes work sometimes not bcs of the pi.
- god i love linux
- llm integration
	- query from onto
	- for now only DL
	- convai + psai helpful here ;3
		- https://www.kaggle.com/code/dawidek123/project-situated-ai-notebook1-up#4.-Instruct-the-LLM-to-produce-the-query-or-components-of-the-query-(e.g.,-keywords)-against-the-KG
	- fix prompting, get rid of "The white Rook is making a legal move to square owx.e5."
	