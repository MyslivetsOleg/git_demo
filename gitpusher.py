import subprocess
import re
import time

proc = subprocess.Popen('git config --list', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, err = proc.communicate() 

repos = re.findall(r'remote.*url.*',out.decode())
refs = []
for repo in repos:    
    refs.append(str(repo).split('=')[1])

print (refs)

for ref in refs:
    gitpush = subprocess.Popen('git push '+str(ref), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = gitpush.communicate()
    time.sleep(5)
    print (out.decode())

print("[+] Pushing done!")