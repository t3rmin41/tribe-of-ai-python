def sort_with_bubbles(lst):
    # Set swap_occurred to True to guarantee the loop runs once
    swap_occurred = True

    # Run the loop as long as a swap occurred the previous time
    while swap_occurred:

        # Start off assuming a swap did not occur
        swap_occurred = False

        # For every item in the list except the last one...
        for i in range(len(lst) - 1):

            # If the item should swap with the next item...
            if lst[i] > lst[i + 1]:
                # Then, swap them! But these lines aren't
                # quite right: fix this code!
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                # One more line is needed here; add it!
                swap_occurred = True
    return lst


# We've written the function, sort_with_select, below. It takes
# in one list parameter, a_list. Our version of selection sort
# involves finding the minimum value and moving it to an
# earlier spot in the list.
#
# However, some lines of code are blank. Complete these lines
# to complete the selection_sort function. You should only need
# to modify the section marked 'Write your code here!'

def sort_with_select(a_list):
    # For each index in the list...
    for i in range(len(a_list)):

        # Assume first that current item is already correct...
        minIndex = i

        # For each index from i to the end...
        for j in range(i + 1, len(a_list)):

            # Complete the reasoning of this conditional to
            # complete the algorithm! Remember, the goal is
            # to find the lowest item in the list between
            # index i and the end of the list, and store its
            # index in the variable minIndex.
            #
            # Write your code here!
            if a_list[j] < a_list[minIndex] : # if element at index i+1 is higher than at minimum inex
                minIndex = j

        # Save the current minimum value since we're about
        # to delete it
        minValue = a_list[minIndex]

        # Delete the minimum value from its current index
        del a_list[minIndex]

        # Insert the minimum value at its new index
        a_list.insert(i, minValue)

    # Return the resultant list
    return a_list
