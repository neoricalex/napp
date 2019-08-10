import subprocess
subprocess.run(["ls", "-l"])
#p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#for line in iter(p.stdout.readline, ''): 
#    print(line),
#retval = p.wait()