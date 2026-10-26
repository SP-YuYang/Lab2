def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height**2)
    print("BMI = " + str(bmi))
    return bmi

def check_weight_class(bmi):
    print("checking BMI's weight class : " + str(bmi))
    if bmi < 18.5:
        weight_class = "Under Weight"
    elif bmi > 25.0:
        weight_class = "Over Weight"
    else:
        weight_class = "Normal Weight"
    print("Weight Class is : " + weight_class)
    return weight_class

bmi = calculate_bmi(weight=57, height=1.73)
weight_class = check_weight_class(bmi)
print("The Output BMI is : " + str(bmi))