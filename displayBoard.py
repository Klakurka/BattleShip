from sys import exit
from gameBoard import gameBoard

class displayBoard(object):

	def __init__(self, column, row):
		self.firing_Board = gameBoard(column, row)
		self.ship_Board = gameBoard(column, row)

	def display_Boards(self, board_Info):
		if len(board_Info) == (0):
			return

		occupied_Coordinates, shots_Received_Log, shots_Fired_Log, shots_Fired_Hit_Log = board_Info
		# occupied_Coordinates = Boat Coordinates, yours
		# shots_Fired_Hit_Log = Boat Coordinates, enemy
		# shots_Received_Log = all shots received, yours
		# shots_Fired_Log = all shots received, enemy

		self.firing_Board.update_Board(shots_Fired_Hit_Log, shots_Fired_Log)
		self.ship_Board.update_Board(occupied_Coordinates, shots_Received_Log)

		self.firing_Board.display_Board('Firing Board')
		self.ship_Board.display_Board('Ship Board')

		#print "occupied_Coordinates: " + str(occupied_Coordinates)
		#print "shots_Received_Log: " + str(shots_Received_Log)
		#print "shots_Fired_Log: " + str(shots_Fired_Log)
		#print "shots_Fired_Hit_Log: " + str(shots_Fired_Hit_Log)