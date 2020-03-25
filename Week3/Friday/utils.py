# min length - 11 , max length - 21
def test_input(input):
	if not isinstance(input, list):
		raise ValueError('Input is not a list')
	else:
		if len(input) < 11 or len(input) > 21:
			raise ValueError('Invalid number of frames')
		else:
			for i in input:
				if i < 0 or i > 10:
					raise ValueError('Invalid score')
			return True

def return_the_input_with_list_of_tuples(input):
	list_frames = []
	frame = []
	
	if test_input(input):
		for i in range(0, len(input)):
			size_frame = len(frame)
			
			if i == len(input) - 1 and size_frame == 1:
				frame.append(input[i])
				list_frames.append(frame)
			elif input[i] == 10 and (size_frame == 0 or frame[0] == 0):
				list_frames.append([10,0])
			elif input[i] == 10 and size_frame == 1:
				raise ValueError('Erro')
			elif size_frame == 2:
				list_frames.append(frame)
				frame = []		
				if i == len(input) - 1:
					list_frames.append([input[i]])
				elif input[i] == 10:
					list_frames.append([10,0])
				else:
					frame.append(input[i])	
			else:
				frame.append(input[i])
		if len(frame) == 1:
			list_frames.append(frame)
		return list_frames


def check_number_of_frames(list_frames):
	if len(list_frames) == 10:
		return frame_number_10(list_frames)
	elif len(list_frames ) == 11:
		return frame_number_11(list_frames)
	elif len(list_frames) == 12:
		return frame_number_12(list_frames)
	else:
		raise ValueError('Invalid number of frames') 


def frame_number_10(list_frames):
	if sum(list_frames[9]) >= 10:
		raise ValueError("Invalid number of frame")
	for i in range(0,9):
		if sum(list_frames[i]) > 10:
			raise ValueError("Invalid frame")

	return list_frames

def frame_number_11(list_frames):

	if sum(list_frames[9]) != 10:
		raise ValueError('Invalid tenth frame')
	for i in list_frames:
		if sum(i) > 10:
			raise ValueError('Invalid frame')

	return list_frames

def frame_number_12(list_frames):
	lst = [10, 0]
	if list_frames[9] == lst and list_frames[10] == lst and list_frames[11] == lst:
		return list_frames
	else:
		raise ValueError("Invalid frame")


def return_game(lst):
	return check_number_of_frames(return_the_input_with_list_of_tuples(lst))