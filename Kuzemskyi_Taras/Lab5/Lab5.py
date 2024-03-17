class car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
        self.started = False

    def start(self):
        self.started = True
        print(f"{self.mark} {self.model} was started.")

    def stop(self):
        self.started = False
        print(f"{self.mark} {self.model} was stopped.")

    def output(self):
        status = "started" if self.started else "stopped"
        print(f"{self.mark} {self.model} ({self.year}), Status: {status}")