import modules.constants as const



def changePositionInList(mylist, item, Newposition):
	mylist.remove(item)
	mylist.insert(Newposition, item)
	return mylist

def definePossibleMoves(moves):
	for k in moves:	
		if snake.isNextPositionFree(k):
			continue
		else:	
			moves.remove(k)

	return moves


def BetterOne(snake, food_position):

	moves = [const.UP,const.DOWN,const.RIGHT,const.LEFT]
	

	snake_position = snake.positions[0]
	snakeToFoodVector = (food_position[0]-snake_position[0], food_position[1] - snake_position[1])
	rel_x, rel_y = snakeToFoodVector
	

	if rel_x > 0:
		changePositionInList(moves,const.RIGHT, 0)
	elif rel_x < 0:
	 	changePositionInList(moves, const.LEFT, 0)
	if rel_y > 0:
		changePositionInList(moves, const.DOWN, 0)
	elif rel_y < 0:
		changePositionInList(moves, const.UP, 0) 

	for i in range(len(moves)):
		if NA.isDead(snake, moves[i]):
			continue
		else:
			rightMove = moves[i]
			break

	return rightMoves
"""

if snake.position[0] != food_position:
	moves = BetterOne(snake,food_position)
	if isDead(snake, moves):
		while len(moves) < 2:
			positionHistory, snake.positions, moves = Backtrack(positionHistory, positions, moves)
		moves = moves[1:]




"""

def set_path(snake, food_position):
	path = []
	moves = BetterOne(snake, food_position)

		if isDead(snake, defaultMove):
			AllpositionList = Update_AllpositionList(-1, AllpositionsList)
			snake.positions = AllpositionsList[-1]

		else:
			log_positions_list(positions, allPositions)
			path.append(moves[0])










def log_positions_list(positions, AllpositionsList):
	AllpositionList.append(positions)
	return AllpositionList


def Backtrack(AllpositionList):
	return AllpositionList[-1]

def Update_AllpositionList(currentIteration, AllpositionList):
	AllpositionList = AllpositionList[:currentIteration]
	return AllpositionList

def isDead(snake, move):
	x, y = move
	actualHeadPosition = snake.positions[0]
	nextHeadPosition = (((actualHeadPosition[0]+(x*const.GRID)) % const.WIDTH), (actualHeadPosition[1] + (y*const.GRID)) % const.HEIGHT )
	if len(snake.positions) > 2 and nextHeadPosition in snake.positions[2:]:
		return True
	else:
		return False

