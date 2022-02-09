from platform import platform
from src import depends



hostname = depends.socket.gethostname()
hostip = depends.socket.gethostbyname(hostname)

depends.cursives.fonts.main()

def main():
    while True:
        code = input("?: ")
        if code == 'ping' or code == 'pong':
            depends.define.definition.ping(code)
        elif code == 'cls' or code == 'clear' or code == 'fin':
            depends.define.definition.cls()
        elif code == 'cool mode':
            depends.define.definition.cool_mode()
        elif 'cool' in code:
            depends.define.definition.cool(code)
        elif code == 'local' or code == 'ipconfig' or code == 'ifconfig' or code=='ip':
            depends.define.definition.local(hostip,hostname)
        elif code == 'sleep' or code == 'drunk':
            depends.define.definition.drunk()
        elif 'package' in code:
            depends.define.definition.package(code)
        elif code == 'python':
            depends.subprocess.call("python")
        elif code == 'time' or code == 'date':
            depends.define.definition.times()
        elif code == 'terminal' :
            depends.define.definition.cursive()
        elif code == 'ssh ' or code =='ssh':
            depends.define.definition.ssh(code)
        else:
            depends.puts(depends.colored.red("Try again I really don't know about this one"))
            #depends.os.system(code)