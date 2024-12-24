# an app to that calculates your Body Mass  Index
body_weight = float(input('Please input your body weight in Kilogram (Kg): \n'))
height = float(input('Please input your height in Meters (M): \n'))

# formula to calculate the Bmi
bmi_results = body_weight / (height ** 2)
if bmi_results > 30:
    print ('You are an obese')
elif 18.55 > bmi_results <=24.9:
    print (f'You are under normal weight of {bmi_results} of BMI')
elif  25 < bmi_results <= 29.9:
    print (f'You are Overweight {bmi_results} of BMI')
else: print(f'You are underweight {bmi_results} of BMI')


