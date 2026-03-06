def calculate_bmi_category(height_m, weight_kg):
    # TODO: Calculate BMI value
    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

# Test your function
print(calculate_bmi_category(1.75, 68)) # Should be 'Normal'