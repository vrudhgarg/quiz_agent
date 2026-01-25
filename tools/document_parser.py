from smolagents import Tool
from pathlib import Path
import pymupdf
from docx import Document
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

        if suffix in [".txt", ".md"]:
            return path.read_text(encoding="utf8")

        if suffix in [".pdf"]:
            return self._parse_pdf(path)
        
        if suffix in [".docx"]:
            return self._parse_docx(path)

        # TODO: Add parsing logic for each format
        return f"TODO: parse {suffix} file"

    def _parse_pdf(self, path: Path) -> str:
        "Extracts text from PDF using pymupdf"
        text_parts = []
        with pymupdf.open(path) as doc:
            for page in doc:
                text_parts.append(page.get_text())

        return "\n".join(text_parts)

    def _parse_docx(self, path : Path) -> str:
        """ Extracts text from DOCX using python-docx """
        doc = Document(path)
        return "\n".join([para.text for para in doc.paragraphs])
        
