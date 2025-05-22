

class Logger:
    def __init__(self):
      print("Logger object created" )

    def __del__(self):
      print("Logger object destructed" ) 

log=Logger()
del log        