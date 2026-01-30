from tools.answer_evaluator import AnswerEvaluatorTool

evaluator = AnswerEvaluatorTool()

# TEST MCQ - correct
result = evaluator.forward(
    user_answer="Supervised Learning",
    correct_answer="Supervied Learning",
    question_type="mcq"
)

print(f"Test 1 (should be correct): {result}")


# Test MCQ - wrong
result = evaluator.forward(
    user_answer="Deep learning",
    correct_answer="Supervised learning",
    question_type="mcq"
)

print(f"Test 2 (should be incorrect): {result}")

# Test with different case
result = evaluator.forward(
    user_answer="SUPERVISED LEARNING",
    correct_answer="supervised learning",
    question_type="mcq"
)
print(f"Test 3 (should be correct): {result}")