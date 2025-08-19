from sys import *
from sys import argv
import subprocess

#import subprocess

#print(version)
#print(platform)
#print(argv[1], argv[2] +"!")

#print(executable)

#print("Точка выхода")
#exit('0')
#subprocess.run("python --version")
#subprocess.call("python --version")

#code = subprocess.call(["python", "p1.py"])
#subprocess.call("python", "p1.py")
#print("p1.py вернул", code)

#path.append("C:/")
#print(path)

#subprocess.call("calc")

if platform == "win32":
    subprocess.call("calc")
elif platform.startswith("linux"):
    subprocess.call("gnome-calculator")
    subprocess.Popen(["ls -l"])

