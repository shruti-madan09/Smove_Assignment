import json

# reading json input from file bookingordering.json
with open('example.json') as json_input:
  input = json.load(json_input)
  json_input.close()

possible_routes = []
input_length = len(input)

# input list will be iterated over to set each booking as starting point of possible routes
for each in input:
  possible_routes.append([each])

# possible_routes lists will be keep getting updated untill all the routes in it have been completely created
while len(possible_routes[0]) < input_length:
  # current possible routes will be saved in a temp variable
  temp_routes = possible_routes[:]
  # possible routes will be emptied
  possible_routes = []
  # temp_routes will be iterated over to add the next booking in each sequence in it
  # the updated sequence will be written in possible routes, so temp_routes can be overwritten in the next iteration
  for route in temp_routes:
    # for each route the last booking in the sequence will be fetched
    last_step = route[-1]
    # list of bookings ids which are already part of the route are fetched to avoid duplicates
    existing_steps = [x.get("id") for x in route]
    # without_relocation: a list of bookings that can succeed the last booking booking of the route, without needing any relocation
    without_relocation = [x for x in input if x.get("id") not in existing_steps and x.get("start") == last_step.get("end")]
    with_relocation = []
    # with_relocation: all remaining bookings if without_relocation list is empty
    if without_relocation == []:
      with_relocation = [x for x in input if x.get("id") not in existing_steps and x.get("start") != last_step.get("end")]
    # for each booking in without_relocation/with_relocation list, the current route will be appened and added to possible_routes
    for each in without_relocation:
      possible_routes.append(route+[each])
    for each in with_relocation:
      possible_routes.append(route+[each])


# all eligible routes will be iterated over to find the one with zero or minimum relocations
final_output = []
minimum_relocations = 0
for route in possible_routes:
  relocations  = 0
  for each in range(0, input_length-1):
    if route[each].get("end") != route[each+1].get("start"):
      relocations += 1
  if final_output == [] or relocations < minimum_relocations:
    minimum_relocations = relocations
    final_output = [x.get("id") for x in route]
  if final_output != [] and minimum_relocations == 0:
    break

print "relocations "+str(minimum_relocations)
# writing the final sequence in file output.json
with open('output.json', 'w') as f:
    json.dump(final_output, f)
