from contextlib import ContextDecorator
import datetime

class LogFile(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.log_file = open(self.filename, 'a')
        self.start_time = datetime.datetime.now()
        self.log_file.write(f"Start: {self.start_time}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = datetime.datetime.now()
        run_time = end_time - self.start_time
        if exc_type is None:
            self.log_file.write(f"Run: {run_time}\n")
        else:
            self.log_file.write(f"Run: {run_time} | An error occured: {exc_value}\n")
        self.log_file.close()
        return False
    
@LogFile("my_trace.log")
def some_func():
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        raise e
    
some_func()