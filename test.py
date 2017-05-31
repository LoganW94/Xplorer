import os
import subprocess

usr_home = os.environ.get("HOME")
print(usr_home)

path = os.path.join(usr_home, "Documents")
print(path)
#subprocess.Popen(r'explorer /select, "%s" ' & path)

