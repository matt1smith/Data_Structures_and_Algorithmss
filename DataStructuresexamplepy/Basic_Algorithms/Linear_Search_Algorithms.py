#Goes through all possibilities of an answer until it reaches the right one(refer to laptop screen shots)

#Best for when an object is positioned near the begginig of a list or a search needs to be performed on an unsorted list because linear search traverses the entire list from beginning to end, regardless of its order.
#Worst for when an object is positioned near the end of a list
#Average for when an object is positioned in the middle of a list

#run time is equal to n/the number of objects in a list

###########################BASIC SEARCH###########################
###////////////////////////////////////////////////////////////###
number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33

def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

try:
  # Call the function below...
  result = linear_search(number_list, target_number)
  print(result)
  linear_search(number_list, 100)
except ValueError as error_message:
  print("{0}".format(error_message))

#######################FINDING DUPLICATES#########################
###////////////////////////////////////////////////////////////###
# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

#Linear Search Algorithm
def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if matches:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))

#Function call
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)

########################FINDING MAXIMU#M##########################
###////////////////////////////////////////////////////////////###
# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

#Linear Search Algorithm
def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index

# Function call
highest_score = linear_search(test_scores)

#Prints out the highest score in the list
print(highest_score)

