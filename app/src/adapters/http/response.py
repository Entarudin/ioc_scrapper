import json


class Response:
    def __init__(self, body: str, status: int, headers: dict):
        self.status = status
        self.headers = headers
        self.body = body

    def to_json(self):
        try:
            return json.loads(self.body)
        except Exception:
            raise ValueError("Response is not valid JSON")

    def to_text(self) -> str:
        return self.body
