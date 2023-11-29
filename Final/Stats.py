import random
import statistics

def get_input():
    chosen_range = 21
    while chosen_range > 20 or chosen_range < 1:
        chosen_range = int(input('Enter size of list (number between 1 - 20): '))
    return chosen_range

def get_total(list):
    return sum(list)

def get_average(list):
    return statistics.mean(list)

def get_median(list):
    list.sort()
    middle_index = len(list) // 2
    if len(list) % 2 == 0:
        median = list[middle_index - 1] + list[middle_index]
    else:
        median = list[middle_index]
    return median

def generate_list(size: int):
    generated_list = []
    for number in range(size):
        number = random.randint(1, 10)
        generated_list.append(number)
    return generated_list

def main():
    created_list = generate_list(get_input())
    total = get_total(created_list)
    average = get_average(created_list)
    median = get_median(created_list)

    print('Your created list is:')
    for items in created_list:
        print(items)
    print('Your sum is: {}\nYour average is: {}\n Your median is: {}'.format(total, average, median))

main()