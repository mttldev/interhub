IDENTIFIER, CHARACTER, DIALOGUE, FILENAME, LINE_NUMBER, RENPY_SCRIPT = range(5)

class Statement:
    def __init__(self, content: str) -> None:
        self.raw_content = content
        self.content = self.raw_content.split("\t")
        self.identifier = self.content[IDENTIFIER]
        self.character = self.content[CHARACTER]
        self.dialogue = self.content[DIALOGUE]
        self.filename = self.content[FILENAME]
        self.line_number = self.content[LINE_NUMBER]
        self.renpy_script = self.content[RENPY_SCRIPT]
