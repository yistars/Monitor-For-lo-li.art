# By Bing_Yanchi
import yaml,os,socket,time
from threading import Thread
from queue import Queue
import send,server

class main(object):
    #def __init__(self, send_url, send_time, server_enable, server_host, server_port):
    def __init__(self, send_url, send_time):
        '''
        if server_enable:
            self.run_server(server_host,server_port)
        else:
            server_port = 0
        '''
        #self.run_send(send_url, send_time, server_port)
        self.run_send(send_url, send_time)

    #def run_send(self, send_url, send_time, server_port):
    def run_send(self, send_url, send_time):
        #self.th_send = Thread(target=send.main, args=(send_url, send_time, server_port))
        self.th_send = Thread(target=send.main, args=(send_url, send_time))
        self.th_send.start()
    '''
    def run_server(self, server_host, server_port):
        self.th_server = Thread(target=server.main, args=(server_host,server_port))
        self.th_server.start()
    '''

class config(object):
    def __init__(self):
        self.config = os.path.abspath(os.path.dirname(__file__)) + '\\'+ 'config.yml'

    def create_config(self):
        with open(self.config, 'w') as f:
            #raw_data = [{'Send':{'url':'https://status.lo-li.art/update.php','time':10},'Server':{'enable': True,'host':'0.0.0.0','port':9999}}]
            raw_data = [{'Send':{'url':'https://status.lo-li.art/update.php','time':10}}]
            with open(self.config, 'w') as f:
                data = yaml.dump(raw_data, f)

    def read_config(self):
        with open(self.config) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        global public_data
        public_data = data[0]

public_data = {}
q = Queue()

if __name__ == "__main__":
    print('[I {}] [main] Checking file integrity...'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),))
    
    config_path = os.path.abspath(os.path.dirname(__file__)) + '\\'+ 'config.yml'
    # 若配置文件不存在，则创建空白配置文件
    if (os.path.exists(config_path)) == False:
        config().create_config()
    config().read_config()

    print('[I {}] [main] Checking file success. Monitoring has started.'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),))

    #main(public_data['Send']['url'], public_data['Send']['time'], public_data['Server']['enable'], public_data['Server']['host'], public_data['Server']['port'])
    main(public_data['Send']['url'], public_data['Send']['time'])