from tools.document_parser import DocumentParserTool

parser = DocumentParserTool()

content = parser.forward("test_notes.txt")

print(content)