from smolagents import Tool

class AnswerEvaluatorTool(Tool):
    # Tool identifer
    name = "answer_evaluator"

    # Agents reads the following to know when to use the tool
    description = "Evaluates if a user's answer is correct by comparing it with the correct answer."

    # What argument this tool accepts
    inputs = {
        "user_answer" : {
            "type": "string",
            "description": "The answer provided by the user"
        },
        "correct_answer" : {
            "type": "string",
            "description": "The correct answer to compare against"

        },
        "question_type": {
            "type": "string",
            "description": "Type of question: 'mcq', 'true_false', or 'short_answer'"

        }
    }

    # What this tool returns
    output_string = "string"

    def forward(self, user_answer : str, correct_answer : str, question_type: str) -> str:
        ''' Evaluates the user answer'''

        # Basic cleaning for the answer
        user_clean = user_answer.strip().lower()
        correct_clean = correct_answer.strip().lower()

        # MCQ and True/False: simple string matching
        if question_type in ["mcq", "multiple_choice", "true_false"]:
            if user_clean == correct_clean:
                return "correct"
            
            else:
                return "incorrect"

        
        return "TODO: evaluate short answer"

