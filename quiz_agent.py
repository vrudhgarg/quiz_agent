from smolagents import CodeAgent, LiteLLMModel
from tools.document_parser import DocumentParserTool
from tools.question_generator import QuestionGeneratorTool
from tools.answer_evaluator import AnswerEvaluatorTool

# Create the local LLM model
model = LiteLLMModel(model_id = "ollama/qwen2.5:7b")

parser = DocumentParserTool()
generator = QuestionGeneratorTool()
evaluator = AnswerEvaluatorTool()

# Create the agent with all tools
agent = CodeAgent(
    tools = [parser, generator, evaluator],
    model = model
)

# Test: Generate quiz from our test file
result = agent.run("Read the file test_notes.txt and generate 2 multiple choice questions from it.")
print(result)