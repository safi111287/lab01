def shipping_cost_calculator():
    pass

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