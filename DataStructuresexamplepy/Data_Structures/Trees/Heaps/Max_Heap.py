### Has a runtime of O(logN)
### Based in using the binary tree

class MaxHeap:
  def __init__(self):
    # Initialize an empty heap with a dummy element at index 0
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!

  # Returns the index of the parent of the node at index idx
  def parent_idx(self, idx):
    return idx // 2

  # Returns the index of the left child of the node at index idx
  def left_child_idx(self, idx):
    return idx * 2

  # Returns the index of the right child of the node at index idx
  def right_child_idx(self, idx):
    return idx * 2 + 1

  # END OF HEAP HELPER METHODS

  # Adds a new element to the heap
  def add(self, element):
    # Increment the count of elements
    self.count += 1
    # Print the element being added and the current state of the heap list
    print("Adding: {0} to {1}".format(element, self.heap_list))
    # Append the new element to the end of the heap list
    self.heap_list.append(element)
    # Restore the heap property by moving the new element to its proper position
    self.heapify_up()

  # Restores the heap property by moving the last element up to its proper position
  def heapify_up(self):
    # Print the start of the heapify process
    print("Heapifying up")
    # Start with the last element (newly added element)
    idx = self.count
    # Continue until we reach the root (index 1)
    while self.parent_idx(idx) > 0:
      # Get the current node (child) and its parent
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      # If the parent is less than the child, swap them
      if parent < child:
        print("swapping {0} with {1}".format(parent, child))
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      # Move to the parent index and continue
      idx = self.parent_idx(idx)
    # Print the final state of the heap list after heapify process
    print("Heap Restored {0}".format(self.heap_list))
