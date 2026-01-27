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



