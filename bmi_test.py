def calculate_bmi(height, weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))

    bmi = weight/(height**2)

    print("BMI=" + str(bmi))

    if bmi < 18.5:
        print("Under Weight")
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")

# Prompt the user for input
try:
    height = float(input("Enter your height in meters: "))  # Convert input to float
    weight = float(input("Enter your weight in kilograms: "))  # Convert input to float

    calculate_bmi(height, weight)  # Call the function with user inputs
except ValueError:
    print("Invalid input! Please enter numeric values for height and weight.")