import socket

def check_port(ip, port):
    # 创建一个 TCP 套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置超时时间为 3 秒
    s.settimeout(3)
    try:
        # 尝试连接
        s.connect((ip, port))
        return True
    except Exception:
        return False
    finally:
        s.close()

target_ip = "8.8.8.8"
target_port = 53 # DNS 服务的标准端口

print(f"🚀 正在检测 {target_ip}:{target_port} 的可达性...")

if check_port(target_ip, target_port):
    print(f"✅ 成功！{target_ip} 响应了我们的连接请求。")
else:
    print(f"❌ 失败！{target_ip} 拒绝连接或超时。")
