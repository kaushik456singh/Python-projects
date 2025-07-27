score = 0
questions = {
    "What is the capital of India?": "Delhi",
    "What is 2 + 2?": "4",
    "Which planet is known as the Red Planet?": "Mars"
}
for q, a in questions.items():
    ans = input(q + " ")
    if ans.strip().lower() == a.lower():
        score += 1
print(f"Your score: {score}/{len(questions)}")