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
    pass

def loan_affordability_check():
    pass

def bmi_category_reporter():
    pass

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
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()