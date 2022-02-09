from src import depends
class definition:
    def ping(code):
        if code == 'ping':
            print("\npong \U0001F606 \n")
        else:
            print("\nping \U0001F606 \n")
        hosts = input("Enter ip address or website to ping : \n")
        numbers = input("Enter how many times to ping : \n") 
        command = ['ping','-c',numbers,hosts]
        print(depends.subprocess.call(command))
        print("We have found ip addresses with open ports that you may like to connect: \n")
        print(depends.subprocess.run(['dig','+short',hosts]))
    def cls():
        if depends.platform.system() == 'Windows':
            depends.os.system("cls")
        else:
            depends.os.system("clear")
    def cool_mode():
         print("If u want to use multiple commands try them in a single line only like ('cd /tmp; ls') on linux.")
         while True:
             a = input("")
             if a == "break" or a == "stop":
                break
             depends.os.system(a)
    def cool(code):
        command = code.replace("cool","")
        depends.colored.magenta(depends.os.system(command))
    def local(hostip,hostname):
         print("Your Local ip address is: "+hostip)
         print("Your Desktop name is: "+hostname)
    def drunk():
        depends.define.definition.cls()
        print("Sleep or drunk have a good dose of quick nap \U0001f6cc")
        depends.etc.countdown(int(600))
    def package(codes):
        command = codes.replace("package","")
        depends.colored.cyan(depends.etc.distro(command))
    def times():
        utc = depends.time.strftime("%z")
        zone = depends.time.strftime("%Z")
        now = depends.datetime.now().strftime(f"%d %b, %Y || %I:%M:%S %p || {zone} zone with utc offset of {utc}")
        print(now)
    def cursive():
        depends.cursives.fonts.main()
        print("You know something, that we are very cool.")
    def ssh(codes):
        depends.os.system(codes)