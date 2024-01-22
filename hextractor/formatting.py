class FormatText:
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'    
    HEADER = '\033[95m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def okblue(cls, text: str) -> str:
        return f'{FormatText.OK_BLUE}{text}{FormatText.END_C}'

    @classmethod
    def okcyan(cls, text: str) -> str:
        return f'{FormatText.OK_CYAN}{text}{FormatText.END_C}'

    @classmethod
    def okgreen(cls, text: str) -> str:
        return f'{FormatText.OK_GREEN}{text}{FormatText.END_C}'

    @classmethod
    def fail(cls, text: str) -> str:
        return f'{FormatText.FAIL}{text}{FormatText.END_C}'

    @classmethod
    def warning(cls, text: str) -> str:
        return f'{FormatText.WARNING}{text}{FormatText.END_C}'

    @classmethod
    def bold(cls, text: str) -> str:
        return f'{FormatText.BOLD}{text}{FormatText.END_C}'
