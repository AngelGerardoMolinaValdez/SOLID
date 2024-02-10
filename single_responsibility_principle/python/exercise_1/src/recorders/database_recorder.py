from recorders.recorder import Recorder

class DataBaseRecorder(Recorder):
    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string

    def create(self, data: dict) -> None:
        print(f"Saving: {data} in {self.connection_string}.")
