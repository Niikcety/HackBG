
def is_length_valid(length):
	spl_length = length.split(':')
	if len(spl_length) != 2 and len(spl_length) != 3:
		raise Exception('Invalid size of length')
	else:
		for i in spl_length:
			if not i.isdigit():
				raise Exception('Length containing characters different than int')
			if int(i) <0 or int(i) > 60:
				raise Exception('Length containing integer bigger than 60')
	return True

def length_to_seconds(length):
	splt_length = length.split(':')

	if len(splt_length) == 2:
		return int(splt_length[0]) * 60 + int(splt_length[1])
	else:
		return int(splt_length[0]) * 3600 + int(splt_length[1]) * 60 + int(splt_length[2])

def length_to_minutes(length):
	splt_length = length.split(':')

	if len(splt_length) == 2:
		return int(splt_length[0]) 
	else:
		return int(splt_length[0]) * 60 + int(splt_length[1]) 

def length_to_hours(length):
	splt_length = length.split(':')

	if len(splt_length) == 2:
		return 0
	else:
		return int(splt_length[0]) 

def from_seconds_to_string(seconds):
	hours = seconds // 3600
	minutes = seconds % 3600 // 60
	second = seconds % 3600 % 60

	return str(hours) + ':' + str(minutes) + ':' + str(second)