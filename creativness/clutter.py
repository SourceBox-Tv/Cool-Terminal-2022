from src import depends
# tab completion 
#readline.parse_and_bind('tab: complete') 
# history file 
histfile = depends.os.path.join(depends.os.environ['HOME'], '.pythonhistory') 
try: 
    depends.readline.read_history_file(histfile) 
except IOError: 
    pass 
depends.atexit.register(depends.readline.write_history_file, histfile) 
del  histfile, depends.readline, depends.rlcompleter

