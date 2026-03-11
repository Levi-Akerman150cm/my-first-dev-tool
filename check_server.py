import os
import socket
import requests # 引入发送 HTTP 请求的库
import json

def send_alert(msg):
    # 填入你刚才复制的钉钉机器人 URL
    webhook_url = os.environ.get('DINGTALK_WEBHOOK')
    # 增加这个判断：如果没拿到 URL，打印提示并退出函数
    if not webhook_url:
        print("🚨 错误：环境变量 DINGTALK_WEBHOOK 为空，请检查 Github Action 配置！")
        return    
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": f"【监控告警】{msg}" # 必须包含你设置的关键词
        }
    }
    # 发送 POST 请求
    requests.post(webhook_url, data=json.dumps(data), headers=headers)
   
def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((ip, port))
        return True
    except Exception:
        return False
    finally:
        s.close()

target_ip = "212.62.96.14"
target_port = 443 

if check_port(target_ip, target_port):
    print(f"✅ {target_ip} 正常")
else:
    print(f"❌ {target_ip} 异常，正在发送告警...")
    send_alert(f"ECS 服务器 {target_ip} 的 Nginx 服务挂掉了，请火速排查！")
