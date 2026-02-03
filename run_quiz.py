from tools.document_parser import DocumentParserTool
from tools.question_generator import QuestionGeneratorTool
from tools.answer_evaluator import AnswerEvaluatorTool
from models import Question

# Create tools
parser = DocumentParserTool()
generator = QuestionGeneratorTool()
evaluator = AnswerEvaluatorTool()

# Step 1: Get file from user
file_path = input("Enter path to your lecture notes: ")

# Step 2: Parse the document
print("\nReading document...")
content = parser.forward(file_path)
print(f"Read {len(content)} characters.")

# Step 3: Generate questions
num_q = int(input("How many questions? "))
print("\nGenerating questions...")
json_result = generator.forward(content, num_q, "multiple_choice")
questions = Question.from_json(json_result)
print(f"Generated {len(questions)} questions.\n")

# Step 4: Run the quiz
score = 0

for i, q in enumerate(questions, 1):
    print(f"--- Question {i}/{len(questions)} ---")
    print(q.question_text)
    
    # Show options for MCQ
    for j, option in enumerate(q.options):
        print(f"  {j + 1}. {option}")
    
    # Get user answer
    user_input = input("\nYour answer (enter number): ")
    
    # Convert number to actual answer
    try:
        answer_index = int(user_input) - 1
        user_answer = q.options[answer_index]
    except:
        user_answer = user_input
    
    # Evaluate
    result = evaluator.forward(user_answer, q.correct_answer, "mcq")
    
    if result == "correct":
        print("✓ Correct!\n")
        score += 1
    else:
        print(f"✗ Wrong. The answer was: {q.correct_answer}")
        print(f"Explanation: {q.explanation}\n")

# Step 5: Show final score
print(f"--- Quiz Complete ---")
print(f"Score: {score}/{len(questions)}")