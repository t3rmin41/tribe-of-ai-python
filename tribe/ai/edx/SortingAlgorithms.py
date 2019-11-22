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


# Let's implement Mergesort! This is a complex problem
# because it applies recursion to sorting algorithms, but
# it's also by far the most efficient sorting algorithm we'll
# cover.

# First, we need a function definition: MergeSort should take
# as input one list.

def mergesort(lst):
    # Then, what does it do? mergesort should recursively
    # run mergesort on the left and right sides of lst until
    # it's given a list only one item. So, if lst has only
    # one item, we should just return that one-item list.

    if len(lst) <= 1:
        return lst

    # Otherwise, we should call mergesort separately on the
    # left and right sides. Since each successive call to
    # mergesort sends half as many items, we're guaranteed
    # to eventually send it a list with only one item, at
    # which point we'll stop calling mergesort again.
    else:

        # Floor division on the length of the list will
        # find us the index of the middle value.
        midpoint = len(lst) // 2

        # lst[:midpoint] will get the left side of the
        # list based on list slicing syntax. So, we want
        # to sort the left side of the list alone and
        # assign the result to the new smaller list left.
        left = mergesort(lst[:midpoint])

        # And same for the right side.
        right = mergesort(lst[midpoint:])

        # So, left and right now hold sorted lists of
        # each half of the original list. They might
        # each have only one item, or they could each
        # have several items.

        # Now we want to compare the first items in each
        # list one-by-one, adding the smaller to our new
        # result list until one list is completely empty.

        newlist = []
        while len(left) and len(right) > 0:

            # If the first number in left is lower, add
            # it to the new list and remove it from left
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]

            # Otherwise, add the first number from right
            # to the new list and remove it from right
            else:
                newlist.append(right[0])
                del right[0]

        # When the while loop above is done, it means
        # one of the two lists is empty. Because both
        # lists were sorted, we can now add the remainder
        # of each list to the new list. The empty list
        # will have no items to add, and the non-empty
        # list will add its items in order.

        newlist.extend(left)
        newlist.extend(right)

        # newlist is now the sorted version of lst! So,
        # we can return it. If this was a recursive call
        # to mergesort, then this sends a sorted half-
        # list up the ladder. If this was the original
        # call, then this is the final sorted list.

        return newlist