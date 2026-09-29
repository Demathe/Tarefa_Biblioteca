import subprocess

def lt():
    if sys.plataform == 'win32':
        subprocess.run(['cmd', '/c', 'cls'])   
    else: 
        subprocess.run(["clear"])

