print("bmi calculator")
weight=  float(input("what is your weight in kg\n"))
height= float(input("what is your height in meters\n"))
bmi = weight/ height **2

print("your bmi is: " + str((round(bmi, 2))) + "\n")
if bmi < 18.5:
    print("you are underweight")
elif bmi <= 24.9:
    print("you are normal weight")
elif bmi <= 29.9:
    print("you are overweight")
else:
    print("you are obese")
