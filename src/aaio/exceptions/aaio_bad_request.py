class AAIOBadRequest(BaseException):
    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(f"AAIO returns code {code} with \"{message}\"")
