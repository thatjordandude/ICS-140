import time, random

def sequential_search(mylist, target):
    found = False
    index = 0
    while index < len(mylist) and not found:
        if mylist[index] == target:
            found = True
        else:
            index += 1
    return found

def binary_search(mylist, target):
    low = 0
    high = len(mylist) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) / 2
        mid = int(mid)
        if mylist[mid] == target:
            found = True
        else:
            if mylist[mid] < target:
                    low = mid + 1
            else:
                    high = mid - 1
    return found       

def create_unsorted_list(size):
    # Creates a random list of integers to sort
    random_list=[]
    for _ in range(size):
        random_list.append(random.randint(1,size))
    return random_list


def main():
    size = int(input("How large of a list should we sort? "))
    random_list = create_unsorted_list(size)
    search_for = random.randint(1,size)

    print(f"starting Sequential Search...")
    start = time.perf_counter_ns()
    found = sequential_search(random_list, search_for)
    end = time.perf_counter_ns()
    processing_time = end - start
    print(f"sequential finished in {processing_time:,d} nanoseconds.")
    if found:
        print("target found in list.")
    else:
        print("target not found in list.")

    random_list.sort()

    print(f"starting Binary Search...")
    start = time.perf_counter_ns()
    found = binary_search(random_list, search_for)
    end = time.perf_counter_ns()
    processing_time = end - start
    print(f"Binary Search finished in {processing_time:,d} nanoseconds.")
    if found:
        print("target found in list.")
    else:
        print("target not found in list.")

if __name__ == "__main__":
    main()
