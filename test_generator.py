from tools.question_generator import QuestionGeneratorTool
from models import Question

# Create the tool
generator = QuestionGeneratorTool()

# Test with simple content
content = "Machine learning is a subset of AI. It uses data to learn patterns. Supervised learning uses labeled data. Unsupervised learning finds hidden patterns."

# Generate 2 MCQ questions
result = generator.forward(
    content=content,
    num_questions=2,
    question_type="multiple_choice"
)

# Parse into Question objects
questions = Question.from_json(result)

# Print each question
for i, q in enumerate(questions, 1):
    print(f"Question {i}: {q.question_text}")
    print(f"Answer: {q.correct_answer}")
    print(f"Options: {q.options}")
    print()