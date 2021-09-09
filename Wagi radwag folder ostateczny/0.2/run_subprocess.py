import subprocess


def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print (proc_stdout)

subprocess.call('python gui0.2.py "13-Waga lewa piecowa|COM10|COM15|0|0"', shell = True)

#subprocess_cmd('python gui0.2.py "'+'"13-Waga lewa piecowa|COM10|COM15|0|0"')

