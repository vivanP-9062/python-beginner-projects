print("bmi calculator")
weight=  float(input("what is your weight in kg\n"))
height= float(input("what is your height in meters\n"))
bmi = weight/ height **2

print("your bmi is: " + str((round(bmi, 2))) + "\n")

print ("""if your bmi is Below 18.5 = Underweight

18.5 - 24.9 = Normal weight

25 - 29.9 = Overweight

30 and above = Obese""")