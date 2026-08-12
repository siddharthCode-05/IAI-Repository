from datetime import datetime


def greet_user():
    print("\nHello! I am your Student Study Assistant.")
    print("I can help you with basic study calculations and recommendations.")


def get_current_datetime():
    current_time = datetime.now()
    print("\nCurrent date and time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_study_percentage():
    try:
        total_hours = float(input("\nEnter total study hours: "))
        completed_hours = float(input("Enter completed study hours: "))

        if total_hours <= 0:
            print("Total study hours must be greater than zero.")
            return

        if completed_hours < 0 or completed_hours > total_hours:
            print("Completed hours must be between 0 and total study hours.")
            return

        percentage = (completed_hours / total_hours) * 100

        print(f"Study Percentage: {percentage:.2f}%")

    except ValueError:
        print("Please enter valid numbers.")


def study_recommendation():
    try:
        percentage = float(input("\nEnter your study completion percentage: "))

        if percentage < 0 or percentage > 100:
            print("Please enter a percentage between 0 and 100.")
            return

        if percentage >= 80:
            print("Recommendation: Excellent progress! Keep following your study plan.")
        elif percentage >= 60:
            print("Recommendation: Good progress. Try to maintain consistency.")
        elif percentage >= 40:
            print("Recommendation: You can improve. Make a simple daily study schedule.")
        else:
            print("Recommendation: Start with small daily goals and gradually increase them.")

    except ValueError:
        print("Please enter a valid percentage.")


def main():

    while True:

        print("\n================================")
        print("     STUDENT STUDY ASSISTANT")
        print("================================")

        print("1. Greeting")
        print("2. Current Date & Time")
        print("3. Calculate Study Percentage")
        print("4. Get Study Recommendation")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            greet_user()

        elif choice == "2":
            get_current_datetime()

        elif choice == "3":
            calculate_study_percentage()

        elif choice == "4":
            study_recommendation()

        elif choice == "5":
            print("\nThank you for using the Student Study Assistant!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()