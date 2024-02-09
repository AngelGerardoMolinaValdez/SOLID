from recorders.recorder import Recorder

class FileRecorder(Recorder):
    def __init__(self, path: str) -> None:
        self.path = path

    def create(self, data: dict) -> None:
        print(f"Saving: {data} in {self.path}.")
