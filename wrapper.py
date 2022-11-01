import ssl
import socket
import re
import multiprocessing

class HTTP:
    def get_req(self, host, path, port=80, ssl=False):
        if ssl:
            socket_ = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        else:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_.connect((host, port))
            socket_.send(
            f"GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n".encode('utf-8')
            )
            data = socket_.recv(4096)
        if socket_.fileno() != -1:
            socket_.close()
        return data


    def post_req(self, host, path, data, port=80, ssl=False):
        if ssl:
            socket_ = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        else:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.connect((host, port))
        socket_.send(
            f"POST {path} HTTP/1.0\r\nHost: {host}\r\nContent-Length: {len(data)}\r\n\r\n{data}".encode('utf-8')
        )
        data = socket_.recv(4096)
        if socket_.fileno() != -1:
            socket_.close()
        return data


    def put_req(self, host, path, data, port=80, ssl=False):
        if ssl:
            socket_ = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        else:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.connect((host, port))
        socket_.send(
            f"PUT {path} HTTP/1.0\r\nHost: {host}\r\nContent-Length: {len(data)}\r\n\r\n{data}".encode('utf-8')
        )
        data = socket_.recv(4096)
        if socket_.fileno() != -1:
            socket_.close()
        return data


    def request(self, method, host, path, data='', port=80, ssl=False):
        if ssl:
            socket_ = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        else:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.connect((host, port))
        if data:
            socket_.send(
                f"{method.upper()} {path} HTTP/1.0\r\nHost: {host}\r\nContent-Length: {len(data)}\r\n\r\n{data}".encode('utf-8')
            )
        else:
            socket_.send(
                f"{method.upper()} {path} HTTP/1.0\r\nHost: {host}\r\n\r\n".encode('utf-8')
            )
        data = socket_.recv(4096)
        if socket_.fileno() != -1:
            socket_.close()
        return data


    def request_multiprocess(self, method, host, path, data='', port=80, ssl=False, process_count=1000):
        p = multiprocessing.Pool(process_count)
        results = []
        for _ in range(process_count):
            results.append(p.apply_async(method, args=[host, path, data, port, ssl]))
        p.close()
        p.join()
        return results
