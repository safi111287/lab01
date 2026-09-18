def shipping_cost_calculator():
    try:
        package_weight = float(
            input("Enter package weight in kg (greater than 0 and up to 50 kg): ")
        )
        if package_weight <= 0 or package_weight > 50:
            print("Package weight must be greater than 0 kg and no more than 50 kg")
            return
        
        destination_zone = int(
            input("Enter destination zone (1, 2, or 3): ")
        )
        if destination_zone < 1 or destination_zone > 3:
            print("Destination zone must be 1, 2, or 3.")
            return
        
    except ValueError:
        print("Invalid input please enter numeric values only")
        return

    if package_weight <= 2:
        rate_per_kg = 5.00
        weight_band = "Light"
    elif package_weight <= 10:
        rate_per_kg = 7.50
        weight_band = "Standard"
    else:
        rate_per_kg = 10.00
        weight_band = "Heavy"

    if destination_zone == 1:
        zone_multiplier = 1.00
    elif destination_zone == 2:
        zone_multiplier = 1.20
    else:
        zone_multiplier = 1.40

    shipping_cost = package_weight * rate_per_kg * zone_multiplier

    print(
        f"Shipping cost for a {package_weight:.1f} kg package "
        f"in the {weight_band} rate band to Zone {destination_zone} "
        f"is ${shipping_cost:.2f}."
    )

def grade_classifier():
    try:
        mark = float(
            input("Enter a grade from 0 to 100: ")
        )
        if mark < 0 or mark > 100:
            print("Grade must be between 0 and 100")
            return
    
    except ValueError:
        print("Invalid input please enter a numeric grade")
        return

    if mark >= 90:
        letter_grade = "A"
    elif mark >= 80:
        letter_grade = "B"
    elif mark >= 70:
        letter_grade = "C"
    elif mark >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print(f"Your grade is {mark:.1f}% which is a {letter_grade}")

def loan_affordability_check():
    try:
        monthly_income = float(
            input("Enter your monthly income (greater than 0): ")
        )
        if monthly_income <= 0:
            print("Monthly income must be greater than 0")
            return

        monthly_payment = float(
            input("Enter the proposed monthly payment (greater than 0): ")
        )
        if monthly_payment <= 0:
            print("Monthly payment must be greater than 0")
            return
        
    except ValueError:
        print("Invalid input please enter numeric values only")
        return

    payment_to_income_ratio = monthly_payment / monthly_income
    if payment_to_income_ratio <= 0.30:
        affordability = "Affordable"
    elif payment_to_income_ratio <= 0.40:
        affordability = "Borderline"
    else:
        affordability = "Not affordable"

    print(
        f"Your payment to income ratio is {payment_to_income_ratio:.1%} "
        f"This payment is considered {affordability}"
    )

def bmi_category_reporter():
    try:
        height_cm = float(
            input("Enter height in cm (greater than 0 and up to 300 cm): ")
        )
        if height_cm <= 0 or height_cm > 300:
            print("Height must be greater than 0 and no more than 300 cm")
            return
    
        weight = float(
            input("Enter weight in kg (greater than 0 and up to 500 kg): ")
        )
        if weight <= 0 or weight > 500:
            print("Weight must be greater than 0 and no more than 500 kg")
            return

    except ValueError:
        print("Invalid input please enter numeric values only")
        return

    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    print(f"Your BMI is {bmi:.1f}, which falls in the {category} category")

def main():
    print("Choose one option: ")
    print("1. Calculate shipping cost")
    print("2. Classify grade")
    print("3. Check loan affordability")
    print("4. Report BMI category")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        shipping_cost_calculator()
    elif choice == '2':
        grade_classifier()
    elif choice == '3':
        loan_affordability_check()
    elif choice == '4':
        bmi_category_reporter()
    else:
        print("Invalid choice please select a valid option")

if __name__ == "__main__":
    main()