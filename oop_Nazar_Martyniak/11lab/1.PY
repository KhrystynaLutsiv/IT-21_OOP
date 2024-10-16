import os
import datetime

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_file = 'application.log'
            cls._instance._initialize_log_file()
        return cls._instance

    def _initialize_log_file(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write("Log File Created: {}\n".format(datetime.datetime.now()))

    def log(self, message):
        with open(self.log_file, 'a') as f:
            f.write("[{}] {}\n".format(datetime.datetime.now(), message))


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    print(logger1 is logger2)  # Виведе: True

    logger1.log("This is the first log message.")
    logger2.log("This is the second log message.")

    with open('application.log', 'r') as f:
        print(f.read())
