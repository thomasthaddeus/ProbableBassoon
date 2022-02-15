#prints the board

def board(box):
	print("\n\t\t|\t|\t\n\t{}\t|\t{}\t|\t{}\n\t___|___|___\n\t\t|\t|\t\n\t{}\t|\t{}\t|\t{}\n\t___|___|___\n\t\t|\t|\t\n\t{}\t|\t{}\t|\t{}\n\t   |   |   ".format(box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7], box[8]))
    	
print(board)