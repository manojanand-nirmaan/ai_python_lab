def calculate_bmi_categories(patients):
    categories = []
    for height, weight in patients:
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            categories.append(f'{height}, {weight} - Underweight')
        elif bmi < 25:
            categories.append(f'{height}, {weight} - Normal')
        elif bmi < 30:
            categories.append(f'{height}, {weight} - Overweight')
        else:
            categories.append(f'{height}, {weight} - Obese')

    return categories

patients_data = [
    (1.75, 68),
    (1.60, 45),
    (1.80, 85),
    (1.65, 95)
]

print(calculate_bmi_categories(patients_data))