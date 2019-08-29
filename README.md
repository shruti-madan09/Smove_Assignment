# Smove Assignment

## Problem Statement
* A booking comprises of
  * id
  * start location
  * end location

* Relocation: Is required between two adjacent bookings (b1, b2) if end of b1 is not same as start of b2.

* Problem: To design and implement an algorithm that takes a sequence of bookings as input, and outputs a single permutation of the input that minimises the total number of relocations within the sequence.

* Sample Input: A json file containing the bookings information in the following format
```
[
	{ "id": 1, "start": 23, "end": 42 },

	{ "id": 2, "start": 77, "end": 45},

	{ "id": 3, "start": 42, "end": 77 }
]
```

* Sample Output: A json file containing sequence of booking ids in the following format
```
[1, 3, 2]
```
<br />

## Solution
Divides input list into sub lists in such a way that each sub list is a sequence of bookings where no relocation is required. The number of sub lists would indicate the relocations required and merging the sub lists would yield the final route.

### Logic
1. The first booking (0th index) from the input list is picked up.
2. A list (known as sub route) is created with the booking from step 1 as the initial entry. This booking is removed from the input list.
3. The remaining input list is iterated over
   1. If a booking is found whose start is the same as end of the last element of the sub route from step 2, that booking is appended to it. This booking is removed from the input list. _(If there are multiple such bookings, the first one is picked)_
   2. If a booking is found whose end is the same as start of the first element of the sub route from step 2, that booking is prepended to it. This booking is removed from the input list. _(If there are multiple such bookings, the first one is picked)_
4. Step 3 is repeated until no booking to append or prepend is found.
5. Steps 1 to 4 are repeated to create different sub routes.
6. Number of relocations: Number of sub routes - 1
7. Final route: Concatenation of sub routes

### Time Complexity
O(N*N), where N is the length of input set

### Technology Used
python 2.7

### File Name
* code file: final_approach.py
* input file: bookingordering.json
* output file: output.json

### Command to Run
python final_approach.py  _(the input file bookingorder.json needs to be in the path, where this command is run)_

<br />

## Other Solutions
I've also decided to submit two more approaches I went through before coming up with the final solution. The idea behind submitting these is to showcase the thought process that went behind solving this challenge.

### Brute Force
Generates multiple eligible routes and finds the one with minimum relocations. While this is a solution that guarantees the most accurate result, its the most time consuming, which makes it feasible to be executed only for a very small input set.

#### Logic
1. A specific booking from the input list is taken as the starting point for a possible route.
2. List of bookings is fetched whose start is same as the end of the last booking in the route.
3. All possible routes are created for each booking in the list created in step 2.
4. If the list in step 2 is empty, all possible routes with remaining bookings will be created.
5. Bookings considered in step 2 or 4 will only be the ones that have not already been included in the route.
6. Steps 2 to 5 are repeated until complete routes are created.
7. Steps 1 to 6 are repeated for every booking in the input list.
8. All possible routes are iterated over and the one with minimum relocations is picked as the result.

#### File Name: brute.py

#### Command to Run: python brute.py

### Another Solution
Creates an eligible route randomly and keeps track of the number of relocations in it. This is repeated until either a route with 0 relocations is found or the same minimum relocation count is calculated repeatedly for a fixed number of times.

#### Logic
1. One booking is chosen at random from the input list and a route is initialized with this booking.
2. List of bookings is fetched whose start is same as end of the last booking in the route.
3. Any one booking is picked at random from the list from step 2 and appended to the route.
4. If the list in step 2 is empty, one booking is picked at random from all the remaining ones. The number of relocations is incremented by one if this step is executed.
5. The bookings considered in step 3 or 4 are the ones that have not already been included in the route.
6. Steps 2 to 5 are executed until one complete route is created. If the number of relocations of this route is lesser than the current minimum (or this is the first route generated), the current minimum and the final result are updated.
7. Steps 1 to 5 are repeated until either the current minimum relocations is 0 or the current minimum relocation is calculated to the same value N times. (N being the length of input set).

#### File Name: trial_approach.py

#### Command to Run: python trial_approach.py
