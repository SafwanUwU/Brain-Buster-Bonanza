def quiz_game():
    print("Welcome to the Quiz Game!")
    score = 0
    questions = [
        ("What is the capital of France?", "paris"),
        ("What is 5 + 7?", "12"),
        ("Which planet is known as the Red Planet?", "mars"),
        ("What is the largest mammal?", "blue whale"),
        ("What programming language is this game written in?", "python")
    ]
    for question, correct_answer in questions:
        answer = input(f"{question} ").lower()
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer.capitalize()}.")
    print(f"\nYour final score is {score}/{len(questions)}!")
quiz_game()