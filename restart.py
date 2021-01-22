import subprocess, time

filename = 'D:\\3.14ton\\prjcts\\Zno_bruh.py'
while True:
    time.sleep(2)
    p = subprocess.Popen('python '+filename, shell=True).wait()
    if p != 0:
        continue
    else:
        break
