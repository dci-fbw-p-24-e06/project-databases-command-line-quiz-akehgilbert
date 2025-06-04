from quiz_service import take_quiz
from topic_service import add_new_topic
from question_service import add_new_question


def show_menu():
    while True:
        print("\n***** Welcome To Command_Line_Quiz *****")
        print("\nSelect Your Choice:")
        print("1. Take a Quiz")
        print("2. Add a New Topic")
        print("3. Add a New Question")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            take_quiz()
        elif choice == '2':
            add_new_topic()
        elif choice == '3':
            add_new_question()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select from 1-4.")
