import os,socket,time,threading

class http(object):
    def __init__(self, HOST, PORT):
        # 创建Socket对象
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口复用
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定IP端口
        self.server_socket.bind((HOST, PORT))
        # 设置监听
        self.server_socket.listen(128)
        # 信息输出
        print('[I {}] [HTTP] Serving HTTP on port {} ...'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), PORT))

    def run(self):
        while True:
            # 等待客户端连接
            client_socket, ip_port = self.server_socket.accept()
            threading.Thread(target=self.task, args=(client_socket,), daemon=True).start()

    def task(self, client_socket):
        # 接收数据
        recv_data = client_socket.recv(1024).decode('utf-8')
        # 拆分换行符便于检索
        info = recv_data.split('\n')
        
        right = False

        for i in range(len(info)):
            if (info[i].find('POST') == 0) or (info[i].find('GET') == 0):
                # 拆分 POST 和 地址
                post = info[i].split(' ')
                parameter = post[1].lstrip('/')
                if parameter == 'stat.txt':
                    right = True

        data = "Server Healthy."
        if right:
            http_response = "HTTP/1.1 200 OK" + '\r\n\r\n' + data
        else:
            http_response = "HTTP/1.1 403 Forbidden" + '\r\n'
        
        client_socket.send(http_response.encode('utf-8'))

        # 断开与客户端连接
        client_socket.close()

    def __del__(self):
        # 当服务端程序结束时停止服务器服务
        self.server_socket.close()

def main(HOST, PORT):
    http(HOST, int(PORT)).run()