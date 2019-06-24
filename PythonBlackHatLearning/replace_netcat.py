import sys
import socket
import getopt
import threading
import subprocess

# 定义一些全局变量
listen = False
command = False
upload = False
execute = ''
target = ''
upload_destination = ''
port = 0


def usage():
    print('BHP Net Tool')
    print('Usage: bhpnet.py -t target_host -p port')
    print('-l --listen  -listen on [host]:[port] for incoming connections')
    print('-e --execute=file_to_run - execute the given file upon receiving a connection')
    print('-c --command - initialize a command shell')
    print('-u --upload=destination - upon receiving connection upload a file and write to [destination]')
    print('Examples: ')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -c')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\')
