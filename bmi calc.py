def bmi_app():
    height = input("How tall are you?")
    weight = input("How much do you weigh?")
    bmi_value = int(weight)/(int(height)/100)**2
    print('Your BMI is {}'.format(round(bmi_value, 2)))
    if bmi_value < 18.5:
        print("You should eat more")
    elif bmi_value >= 18.5 and bmi_value <= 24:
        print("good job!")
    else: print('you\'re overweight')

bmi_app()
