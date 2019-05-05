import socket

target_host = 'www.baidu.com'
target_port = 80

# 建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 发送一些数据
print('我已经发送了信息')
client.sendto('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection:keep-alive\r\n\r\n'.encode('utf-8'), (target_host, target_port))
# 接收一些数据
data, addr = client.recvfrom(4096)
print('我已经收到了信息')
print(data.decode())
