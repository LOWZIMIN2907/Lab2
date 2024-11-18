def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    user_input = input() # Read from the terminal console a sequence of numbers entered by the user using the Python system function “input()”
    string_list = user_input.split(", ") # Use the Python function “split(“,”)” to split the user entered string into a Python List of strings based on the “,’ comma character
    float_list = [float(number) for number in string_list] # Convert the Python List of strings to a List of floats which can be used later for calculating average, minimum and maximum values
    return float_list # Return type: List of Floats

def calc_average(float_list): # Input parameter: List
    print("calc_average")
    total = sum(float_list)
    count = len(float_list)
    average = total/count
    return average # Return type: Float

def find_min_max(float_list): # Input parameter: List
    print("find_min_max")
    min_value = min(float_list)
    max_value = max(float_list)
    return [min_value, max_value] # Return type: List of Floats in the format [min_temp, max_temp]

def sort_temperature(float_list): # Input parameter: List
    print("sort_temperature")
    return sorted(float_list) # Return type: List of Floats sorted in ascending order, To sort in descending order, use sorted(float_list, reverse=True).

def calc_median_temperature(float_list): # Input parameter: List
    print("calc_median_temperature")
    sorted_list = sorted(float_list)
    n = len(float_list) #length of the float list   

    if n % 2 != 0: median = sorted_list[n // 2] # if n is odd, it picks the middle value
    else: 
        m1 = sorted_list[n // 2 - 1] #if n is even, it picks the average of the 2 middle value
        m2 = sorted_list[n // 2]
        median = (m1 + m2) / 2
    
    return median # Return type: Float

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    float_list = get_user_input()
    print ("Average = " + str(calc_average(float_list)))
    print ("Min and Max = " + str(find_min_max(float_list)))
    print ("Sorted Temperature = " + str(sort_temperature(float_list)))
    print ("Median = " + str(calc_median_temperature(float_list)))

if __name__=="__main__":
    main()