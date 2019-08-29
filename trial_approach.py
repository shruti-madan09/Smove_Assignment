import json
import random

# reading json input from file bookingordering.json
with open('bookingordering.json') as json_input:
  input = json.load(json_input)
  json_input.close()

final_output = []
minimum_relocations = 0
input_length = len(input)
number_of_tries = 0

# a random route will be created and the number of relocations in it will be calculated
# this will be repeated untill either a route with zero relocations is found 
# or the minimum relocations remains same consistently for input_length times
while True:
	# a copy of input is created
	input_copy = input[:]
	# a random index will be chosen from the input list as the starting point of the route
	# this index will be removed from the input list
	current_index = random.randint(0,input_length-1)
	current_position = input_copy[current_index]
	current_path = [current_position.get("id")]
	del input_copy[current_index]
	relocations = 0
	# once a starting point is chosen the remaining route will be created
	while len(current_path) != input_length:
		without_relocation = []
		with_relocation = []
		# the left over input list will be iterated to create two lists
		# without_relocation: one with bookings that can be appended to the route, without needing a relocation 
		# with_relocation: all remaining bookings
		for index, each in enumerate(input_copy):
			if each.get("start") == current_position.get("end"):
				without_relocation.append([index, each])
			else:
				with_relocation.append([index, each])
		# if without_relocation list is non empty, an index will be chosen from it at random and appended to the route
		# if without_relocation list is empty, an index will be chosen at random from with_relocation list and appended to route
		# the booking which is appended will be deleted from the input list
		# if the booking was picked from with_relocation list, relocation count will be incremented
		if without_relocation != []:
			current_index = random.randint(0,len(without_relocation)-1)
			current_position = without_relocation[current_index][1]
			current_path.append(current_position.get("id"))
			del input_copy[without_relocation[current_index][0]]
		else:
			current_index = random.randint(0,len(with_relocation)-1)
			current_position = with_relocation[current_index][1]
			current_path.append(current_position.get("id"))
			del input_copy[with_relocation[current_index][0]]
			relocations += 1

	# Everytime a new route is created the minimum_relocations and final_ouput will be updated
	# if its number of relocations is lesser than the current minimum
	# number_of_tries will indicate how many times a specific minimum was acheived
	if final_output == [] or relocations < minimum_relocations:
		final_output = current_path
		minimum_relocations = relocations
		number_of_tries = 0
	elif relocations == minimum_relocations:
		number_of_tries  += 1

	# Condition to check if minimum_relocations is 0 or number_of_tries = input_length
	if (final_output != [] and minimum_relocations == 0) or number_of_tries == input_length:
		break

print "relocations "+str(minimum_relocations)
# writing the final sequence in file output.json
with open('output.json', 'w') as f:
    json.dump(final_output, f)
