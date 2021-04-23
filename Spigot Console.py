from pathlib import Path
import subprocess
import requests
from subprocess import Popen
import shutil
import os
dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)
print("Welcome to the spigot server client! The current working directory is %s "% dir)
if Path("BuildTools\BuildTools.jar").is_file():
    print("BuildTools Detected")
else:
    os.mkdir("BuildTools")
    url = 'https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar'
    r = requests.get(url, allow_redirects=True)
    os.chdir('BuildTools')
    open('BuildTools.jar', 'wb').write(r.content)
    os.chdir(dir)
    print("Succesfully Downloaded BuildTools")
server = str(input("Input Server Name: "))
if Path(server).is_dir():
    os.chdir(server)
    f = open("eula.txt","w")
    f.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#Fri Apr 23 17:21:05 BST 2021\neula=true")
    f.close()
    subprocess.call(str('java -jar -Xmx2048M \"spigot.jar\"'), shell=True)
else :
    print("Not found..... creating")
    version = str(input("Input Server Version: "))
    os.mkdir(server)
    if Path("BuildTools\spigot-%s.jar" % version).is_file():
        shutil.copy("BuildTools\spigot-%s.jar " % version, "%s\spigot.jar" % server)
    else :
        os.chdir("BuildTools")
        os.system("java -Xmx1024M -jar BuildTools.jar --rev %s" % version)
        os.chdir(dir)
        shutil.copy("BuildTools\spigot-%s.jar " % version, "%s\spigot.jar" % server)
    os.chdir(str(server))
    f = open("eula.txt","w")
    f.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#Fri Apr 23 17:21:05 BST 2021\neula=true")
    f.close()
    Popen(str('java -jar -Xmx2048M spigot.jar'), shell=True)      