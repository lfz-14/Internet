import socket


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定一个本地信息
    localaddr = ("", 7788)  # 必须绑定自己电脑的ip以及port,其他的不行
    udp_socket.bind(localaddr)
    # 3.接收数据
    recv_data = udp_socket.recvfrom(1024)
    # recv_data 存储的是一个元组（接收到的数据，（发送方的ip, port））
    recv_msg = recv_data[0]  # 存储接收的数据
    send_addr = recv_data[1]  # 存储发送方的地址信息
    # 4.打印接收到的数据
    # print(recv_data)
    # print("%s:%s" % (str(send_addr), recv_msg.decode("utf-8")))  # windows中编码格式是gbk
    print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))
    # 5.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()

# 运行结果：
# (b'12465', ('59.68.5.145', 8080)) 元组的第一个数据：发送方发送的数据，
