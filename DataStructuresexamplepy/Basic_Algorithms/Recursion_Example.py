#######################Recursive Call Stack#######################
###////////////////////////////////////////////////////////////###
def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  
  while len(call_stack) != 0:
    return_value = call_stack.pop()
    print("Return value of {0} adding to result {1}".format(return_value['n_value'], result))
    result += return_value['n_value']
  return result, call_stack

sum_to_one(4)

########################Recursive Sum to 1########################
###////////////////////////////////////////////////////////////###
# Define sum_to_one() below...
def sum_to_one(n):
  if n == 1:
    return n
  print("Recursing with input: {0}".format(n))
  return n + sum_to_one(n - 1)

# uncomment when you're ready to test
print(sum_to_one(7))

#########################Flatten Function#########################
###////////////////////////////////////////////////////////////###
# define flatten() below...
def flatten(my_list):
  result = []
  for el in my_list:
    if isinstance(el, list):
      print("list found!")
      flat_list = flatten(el)
      result += flat_list
    else:
      result.append(el)
  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))

#######################Fibonacci_Sequence########################
###///////////////////////////////////////////////////////////###
# define the fibonacci() function below...
def fibonacci(n):
  # base cases
  if n == 1:
    return n
  if n == 0:
    return n
  
  # recursive step
  print("Recursive call with {0} as input".format(n))
  return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"

########################_Recursive_Trees_########################
###///////////////////////////////////////////////////////////###
def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"

  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]
  
  print("Middle index: {0}".format(middle_idx))
  print("Middle value: {0}".format(middle_value))
  
  tree_node = {"data": middle_value}
  tree_node["left_child"] = build_bst(my_list[ : middle_idx])
  tree_node["right_child"] = build_bst(my_list[middle_idx + 1 : ])

  return tree_node
  
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"

#######################Binary_Search_Tree########################
###///////////////////////////////////////////////////////////###
# GETS THE DEPTH OF THE BINARY TREE
def depth(tree):
  if not tree:
    return 0

  left_depth = depth(tree["left_child"])
  right_depth = depth(tree["right_child"])

  if left_depth > right_depth:
    return left_depth + 1
  else:
    return right_depth + 1

# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node

# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 

# test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)