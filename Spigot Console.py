from pathlib import Path
import subprocess
from subprocess import Popen
import shutil
import os
import sys
from time import sleep as wait
try:
  import requests
except ImportError:
  print("Trying to Install required module: requests\n")
  subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
import requests
dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)
print("Welcome to the spigot server client! The current working directory is %s "% dir)
if Path("BuildTools\BuildTools.jar").is_file():
    print("BuildTools Detected")
else:
  try:
    os.mkdir("BuildTools")
  except:
    dir = dir
  url = 'https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar'
  r = requests.get(url, allow_redirects=True)
  os.chdir('BuildTools')
  open('BuildTools.jar', 'wb').write(r.content)
  os.chdir(dir)
  print("Succesfully Downloaded BuildTools")
def ask():
  server = str(input("Input Server Name: "))
  if server == "":
    print("The server must have a name. Try again.")
    server = ask()
  else:
    return server
server = ask()
if Path(server).is_dir():
    os.chdir(server)
    f = open("eula.txt","w")
    f.write("eula=true")
    f.close()
    print("Opening server now. Connect to this server at the ip \"127.0.0.1\" or \"localhost\"")
    subprocess.call(str('java -jar -Xmx2048M -Xms2048M \"spigot.jar\"'), shell=True)
else :
    print("Not found..... creating")
    version = str(input("Input Server Version: "))
    os.mkdir(server)
    if Path("BuildTools\spigot-%s.jar" % version).is_file():
        shutil.copy("BuildTools\spigot-%s.jar " % version, "%s\spigot.jar" % server)
    else :
        os.chdir("BuildTools")
        os.system("java -Xmx1024M -Xms1024M -jar BuildTools.jar --rev %s" % version)
        os.chdir(dir)
        shutil.copy("BuildTools\spigot-%s.jar " % version, "%s\spigot.jar" % server)
    os.chdir(str(server))
    f = open("eula.txt","w")
    f.write("eula=true")
    f.close()
    print("Opening server now. Connect to this server at the ip \"127.0.0.1\" or \"localhost\"")
    wait(1)
    subprocess.call(str('java -jar -Xmx2048M -Xms2048M \"spigot.jar\"'), shell=True)
