import socket


def main():
    # 1. 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 获取服务器的ip, port
    dest_ip = input("请输入服务器ip: ")
    dest_port = int(input("请输入服务器port: "))

    # 3. 链接服务器
    tcp_socket.connect((dest_ip, dest_port))

    # 4. 获取需要下载的文件名
    download_file_name = input("请输入要下载的文件名： ")

    # 5. 将文件名字发送到服务器
    tcp_socket.send(download_file_name.encode("utf-8"))
    # print('接收到的数据为：', recv_data.decode("utf-8"))

    # 6. 接收文件中的数据,接收1KB的数据
    recv_data = tcp_socket.recv(1024)  # 1024--->1K   1024*1024--->1k*1024=1M  1024*1024*1024--->1G

    # 7. 保存接收到的数据到一个文件中，如果接收到数据再创建文件，否则不创建
    if recv_data:
        with open("[接收]" + download_file_name, "wb") as f:
            f.write(recv_data)

    # 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()