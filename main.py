from quiz_service import take_quiz
from topic_service import create_topic, list_topics
from question_service import add_question


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
            topic_name = input("\nEnter the new topic name: ")
            try:
                topic_id = create_topic(topic_name)
                print(f"\nTopic '{topic_name}' added successfully with ID {topic_id}!") # noqa
            except Exception as e:
                print(f"\nError adding topic: {e}")
        elif choice == '3':
            topics = list_topics()

            if not topics:
                print("\nNo topics found! Please add a topic first.")
                continue

            print("\nAvailable Topics:")
            for tid, name in topics:
                print(f"{tid}. {name}")

            try:
                topic_id = int(input("\nEnter topic ID to add a question: "))
            except ValueError:
                print("Invalid topic ID! Please enter a valid number.")
                continue

            module = input("Enter module name: ")
            submodule = input("Enter submodule name: ")
            try:
                difficulty = int(input("Enter difficulty level (1-3): "))
                if difficulty not in [1, 2, 3]:
                    raise ValueError()
            except ValueError:
                print("Difficulty must be 1, 2, or 3.")
                continue

            question = input("Enter the question: ")
            right_answer = input("Enter the correct answer: ")
            wrong_answers = [input(f"Enter wrong answer {i+1}: ") for i in range(3)] # noqa

            try:
                add_question(topic_id, module, submodule, difficulty, question, right_answer, wrong_answers) # noqa
                print("\nQuestion added successfully!")
            except Exception as e:
                print(f"Error adding question: {e}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select from 1-4.")


if __name__ == "__main__":
    show_menu()
