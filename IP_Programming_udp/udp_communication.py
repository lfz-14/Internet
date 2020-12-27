import socket


def main():
    '''
    udp聊天器，使用同一个套接字既能发送又能接收数据
    '''
    # 创建udp的套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 获取对方的ip/port
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的port:"))

    # 从键盘获取数据
    send_data = input("请输入要发送的数据： ")

    # ...这里是使用套接字的功能（省略）...
    # udp_socket.sendto("hahahah", 对方的ip和端口号：元组)
    # udp_socket.sendto(send_data.encode("utf-8"), ("59.68.5.145", 8080)) # 发送的数据类型必须是字节类型
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

    # 5. 不用的时候，关闭套接字

    # 接收回送过来的数据
    recv_data = udp_socket.recvfrom(1024)
    # 套接字是一个可以同时 收发数据
    print(recv_data)

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
