from smolagents import Tool
from pathlib import Path

class DocumentParserTool(Tool):
    # Unique identifier - agent uses this name to call the tool
    name = "document_parser"
    # Agent reads this to understand when/how to use the tool
    description = "Parses a document file and extracts its text content. Supports PDF, DOCX, TXT, and MD files."

    # Defines what arguments the tool accepts
    # Agent uses this to know what to pass in
    inputs = {
        "file_path": {
            "type": "string",
            "description": "Path to the document file"
        }
    }
    # What this tool returns (string, number, etc.)
    output_type = "string"

    def forward(self, file_path: str) -> str:
        """
        Main method that runs when agent calls this tool.
        Takes file_path, returns extracted text.
        """
        # Convert string path to Path object for easier handling
        path = Path(file_path)

        # Check if file exists before trying to parse
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        # Get file extension (e.g., ".pdf", ".txt")
        suffix = path.suffix.lower()

        # TODO: Add parsing logic for each format
        return f"TODO: parse {suffix} file"