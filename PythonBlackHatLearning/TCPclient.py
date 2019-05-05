import socket

target_host = '144.202.120.116'
target_port = 6999

for i in range(0, 1000):
    # 建立一个socket对象,参数AF说明我们将使用标准ipv4地址或host，SOCK说明这将是一个TCP客户端
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接客户端
    client.connect((target_host, target_port))
    # 发送一些数据，发送一条信息，python3只接收btye流
    print('我已经发送你的信息{}'.format(i))
    client.send('GET / HTTP/1.1\r\nHost: 144.202.120.116\r\nConnection:keep-alive\r\n\r\n'.encode('utf-8'))
    # 输出接收的信息
    response = client.recv(4096).decode()
    print('我已经收到服务端的返回的信息')
    print(response)

