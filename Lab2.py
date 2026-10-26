
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    avg = calc_average(num_list)
    print("Average of the numbers is : " + str(avg))
    min_max = find_min_max(num_list)
    print("The Smallest and Biggest numbers respectively is : " + str(min_max))

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    print("===get_user_input===")
    input_numbers = input("Input: ")
    input_list = input_numbers.split()
    float_list = []
    for i in input_list:
        float_list.append(i)
    print("The List of input numbers are : " + str(float_list))
    return float_list
    
def calc_average(float_list):
    print("===calc_average===")
    sum = 0.0
    for i in float_list:
        sum = sum + float(i)
    avg = sum / len(float_list)
    return avg

def find_min_max(float_list):
    print("===find_min_max===")
    min = None
    max = None
    for i in float_list:
        if min == None:
            min = i
        elif min > i:
            min = i
    for i in float_list:
        if max == None:
            max = i
        elif max < i:
            max = i
    return [min , max]

def sort_temperature(float_list):
    print("===sort_temperature===")

def calc_median_temperature(List):
    print("===calc_median_temperature===")
          
if __name__ == "__main__":
    main()
