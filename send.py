# By Bing_Yanchi
import socket,psutil,requests,time

cpu,memory = 0,0
def getMemCpu():
    global cpu,memory
    data = psutil.virtual_memory()
    total = data.total #总内存,单位为byte
    free = data.available #可以内存
    memory = int(round(data.percent))
    cpu = int(round(psutil.cpu_percent(interval=1)))

#def main(url, send_time, server_port):
def main(url, send_time):
    while True:
        getMemCpu()
        servername = socket.gethostname()
        #d = {'type':'update', 'servername':servername, 'cpu':cpu, 'mem':memory, 'port':server_port}
        d = {'type':'update', 'servername':servername, 'cpu':cpu, 'mem':memory}
        r = requests.get(url, params=d)
        time.sleep(send_time)
