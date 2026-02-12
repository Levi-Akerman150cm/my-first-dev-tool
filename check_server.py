import os

# 这里的 IP 你可以随意换成你公司的网关或者公网 DNS
target_ip = "82.197.58.162"

print(f"正在检查 {target_ip} 的连通性...")

# 执行 ping 命令
# -c 1 表示只发一个包，适合快速检测
exit_code = os.system(f"ping -c 1 {target_ip}")

if exit_code == 0:
    print("✅ 服务器在线！运维同学可以喝杯咖啡。")
else:
    print("❌ 警报：服务器掉线了！")  
