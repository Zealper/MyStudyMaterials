#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import threading

# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('144.202.120.116',6999)) #绑定要监听的端口
server.listen(5) #开始监听 表示可以使用五个链接排队
while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print(conn,addr)
    while True:
        try:
            data = conn.recv(1024)  #接收数据
            print('recive:',data.decode()) #打印接收到的数据
            conn.send(data.upper()) #然后再发送数据
        except ConnectionResetError as e:
            print('关闭了正在占线的链接！')
            break
    conn.close()

# bind_ip = '144.202.120.116'
# bind_port = 6999
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((bind_ip, bind_port))
# server.listen(5)
# print('Listening on : {}:{}'.format(bind_ip, bind_port))
#
#
# # 这是处理客户线程
# def handle_client(client_socket):
#     # 打印出客户端发送得到内容
#     request = client_socket.recv(1024)
#     print('Received : {}'.format(request))
#     # 返回一个数据包
#     client_socket.send('ACK!')
#     client_socket.close()
#
#
# while True:
#     client, addr = server.accept()
#     print('Accepted connection from: {}:{}'.format(addr[0], addr[1]))
# # 挂起客户端线程，处理传入的数据
# client_handler = threading.Thread(target=handle_client, args=(client,))
# client_handler.start()
