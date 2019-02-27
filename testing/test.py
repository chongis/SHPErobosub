print("Test On")
import subprocess

p1 = subprocess.Popen(['ls','./'],stdout = subprocess.PIPE)

output= p1.communicate()[0] # (stdout , stderr)
print(output.decode("utf-8"))

s = subprocess.Popen(["python3","<","server.py"])

c = subprocess.Popen(["python3","<","client.py"],stdout=subprocess.PIPE)

print(p1.communicate()[0].decode("utf-8"))
