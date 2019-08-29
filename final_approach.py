import json

# reading json input from file bookingordering.json
with open('bookingordering.json') as json_input:
  input = json.load(json_input)
  json_input.close()

# sub_routes will be a list of lists
# Each list in sub_routes will be a sequence of bookings where no relocation is required.
# among the different lists in sub_routes, relocation will be required.
# number of relocations = length of sub_routes - 1 
# final sequence of bookings will be the concatenation of lists in sub_routes
sub_routes = []
# the logic below will be executed until all the bookings in the input have been distributed amongst lists in sub_routes
while input != []:
	# picking the first booking in input list and adding it to a new list in sub_routes
	# also removing this booking from input list
	sub_routes.append([input[0]])
	del input[0]
	# iterating over the left over input list to find bookings and add to the lastet sequence in sub_routes
	# the latest sequence in sub_routes means the last entry in it
	while True:
		# considering the last booking in the latest sequence
		# and finding any booking whose start is same as end of the it
		# any one booking that satisfies this condition will be deleted from the input list
		to_append = None
		for each in input:
			if sub_routes[-1][-1].get("end") == each.get("start"):
				to_append = each
				break
		# the booking found above will be appended to the latest sequence
		if to_append:
			sub_routes[-1].append(to_append)
			input = [x for x in input if x.get("id") != to_append.get("id")]
		
		# considering the first booking in the latest sequence
		# and finding any booking whose end is same as start of the it
		# any one booking that satisfies this condition will be deleted from the input list
		to_prepend = None
		for each in input:
			if sub_routes[-1][0].get("start") == each.get("end"):
				to_prepend = each
				break
		# the booking found above will be prepended to the latest sequence
		if to_prepend:
			sub_routes[-1] = [to_prepend] + sub_routes[-1]
			input = [x for x in input if x.get("id") != to_prepend.get("id")]

		# if there is no booking to be appended/prepended  to the latest sequence this iteration will be terminated
		# in the next iteration the new sequence will be added in sub_routes
		if not to_append and not to_prepend:
			break

# concatenation of sub_routes indicates the final route
# length of sub_routes - 1 indicates the number of relocations
final_output = []
for route in sub_routes:
	final_output += [x.get("id") for x in route]

print "relocations "+str(len(sub_routes)-1)
# writing the final sequence in file output.json
with open('output.json', 'w') as f:
    json.dump(final_output, f)
