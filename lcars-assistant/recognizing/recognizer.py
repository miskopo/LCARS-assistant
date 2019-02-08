import speech_recognition as sr


class Recognizer(sr.Recognizer):
    def __init__(self):
        super().__init__()
        self.recognize = self.recognize_sphinx

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

