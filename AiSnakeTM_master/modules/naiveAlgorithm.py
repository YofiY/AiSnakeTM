import modules.constants as const
import random


def changePositionInList(mylist, item, Newposition):
	mylist.remove(item)
	mylist.insert(Newposition, item)
	return mylist

def definePossibleMoves(moves, snake):
	for k in moves:
		if snake.length > 1 and (k[0]*-1, k[1]*-1) == snake.direction:
			moves.remove(k)
	return moves
			
def choose_move(snake, food_position):

	moves = [const.UP,const.DOWN,const.RIGHT,const.LEFT]
	

	snake_position = snake.positions[0]
	snakeToFoodVector = (food_position[0]-snake_position[0], food_position[1] - snake_position[1])
	rel_x, rel_y = snakeToFoodVector
	

	if rel_x > 0:
		moves =	changePositionInList(moves,const.RIGHT, 0)
	elif rel_x < 0:
	 	moves = changePositionInList(moves, const.LEFT, 0)
	if rel_y > 0:
		moves = changePositionInList(moves, const.DOWN, 0)
	elif rel_y < 0:
		moves = changePositionInList(moves, const.UP, 0) 

	moves = definePossibleMoves(moves, snake)
	rightMove = random.choice(moves)

	for i in range(len(moves)):
		if isDead(snake, moves[i]):
			continue
		else:
			rightMove = moves[i]
			break

	return rightMove


def isDead(snake, move):
	x, y = move
	actualHeadPosition = snake.positions[0]
	nextHeadPosition = (((actualHeadPosition[0]+(x*const.GRID)) % const.WIDTH), (actualHeadPosition[1] + (y*const.GRID)) % const.HEIGHT )
	if len(snake.positions) > 2 and nextHeadPosition in snake.positions[2:]:
		return True
	else:
		return False








