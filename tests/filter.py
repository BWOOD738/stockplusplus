import random
def filter_sorting(ltest, filter, sort, sbound, ebound, bound):
    # Duplicate the input list
    filtered_list = ltest[:]

    # Apply filtering based on the filter value
    if filter == 1:
        filtered_list = [x for x in filtered_list if sbound <= x <= ebound]
    elif filter == 2:
        filtered_list = [x for x in filtered_list if x > bound]
    elif filter == 3:
        filtered_list = [x for x in filtered_list if x < bound]

    # Apply sorting based on the sort value
    if sort == 'asc':
        filtered_list.sort()
    elif sort == 'des':
        filtered_list.sort(reverse=True)

    return filtered_list

ltest = []

for i in range(0, 10):
    ltest.append(i)
random.shuffle(ltest)
print("Original List:", ltest)

m = 0
while m == 0:
    # Sorting
    sort = None
    print("Filters and Sorting algorithm:")
    while sort not in ['asc', 'des', 'none']:
        sort = input("Sorting (asc/des/none): ")

    # Filtering
    filter = None
    while filter is None or not (-1 < filter < 4):
        print("Filtering:")
        print("0) no filter    1) boundaries      2) greater than      3) less than")
        filter = input("Enter a filter option (1/2/3): ")
        try:
            filter = int(filter)
        except ValueError:
            print("Invalid input. Please enter a number (1/2/3).")
            filter = None

    sbound = None
    ebound = None
    bound = None
    if filter == 1:

        while sbound is None or sbound < 0:
            try:
                sbound = int(input("Starting boundary: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        while ebound is None or ebound <= sbound:
            try:
                ebound = int(input("Ending boundary: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
    elif filter == 2 or filter == 3:

        while bound is None or bound <= -1:
            try:
                bound = int(input("Enter boundary: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    finallist = filter_sorting(ltest, filter, sort, sbound, ebound, bound)
    print("Filtered and Sorted List:", finallist)
