from recorders.recorder import Recorder

class LogRecorder:
    def record(self, recorder: Recorder, message: dict) -> None:
        recorder.create(message)
