from tools.question_generator import QuestionGeneratorTool

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

print(result)