def calculate_bmi(height, weight): 
    print("Height = " + str(height)) 
    print("Weight = " + str(weight))

    bmi = weight / (height ** 2)

    print("BMI = " + str(bmi))

    if bmi < 18.5:
        print("Under Weight")
        return bmi, -1
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
        return bmi, 0
    else:
        print("Over Weight")
        return bmi, 1

calculate_bmi(weight=57, height=1.73) 