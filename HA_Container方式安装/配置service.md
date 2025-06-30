# 配置service
**本章节为本人的操作备忘录，不需要请跳过**  
service目录`/etc/systemd/system`  
创建service服务后更新systemctl、设置开机自启的指令
```shell
sudo systemctl daemon-reload
sudo systemctl enable xxx.service
```
配置文件带注释的，不加说明“无需修改”则默认需要根据实际情况修改内容

<!-- TOC -->
* [配置service](#配置service)
  * [frp](#frp)
    * [安全ssh](#安全ssh)
      * [服务器侧](#服务器侧)
      * [被访问侧](#被访问侧)
      * [访问侧](#访问侧)
    * [带登录验证的网页映射](#带登录验证的网页映射)
      * [服务器侧](#服务器侧-1)
      * [客户端侧](#客户端侧)
<!-- TOC -->


## frp
基于v0.62.1
### 安全ssh
#### 服务器侧
frps配置
```toml
# frps.toml
bindPort = 12345  # 服务端监听端口
auth.token = "p@ssw0rd"  # 鉴权配置
```
service配置
```text
[Unit]
Description = frp server
After = network.target syslog.target
Wants = network.target

[Service]
Type = simple
# 启动frps的命令，需修改内容
ExecStart = /path/to/frps -c /path/to/toml
Restart = on-failure
RestartSec = 60

[Install]
WantedBy = multi-user.target
```
#### 被访问侧
frpc配置
```toml
# frpc.toml
serverAddr = "x.x.x.x"  # 服务器IP
serverPort = 12345  # 服务器监听端口
auth.token = "p@ssw0rd"  # 鉴权配置

[[proxies]]
name = "Raspberry_Pi_ssh"
type = "stcp"
localPort = 22  # 本地ssh端口，还有个localIP参数可不设，默认127.0.0.1
secretKey = "abcdefg"  # 只有与此处设置的 secretKey 一致的用户才能访问此服务
```
service配置
```text
[Unit]
Description = frp client
After = network.target syslog.target
Wants = network.target

[Service]
Type = simple
ExecStart = /path/to/frpc -c /path/to/toml
Restart = on-failure
RestartSec = 60

[Install]
WantedBy = multi-user.target
```
#### 访问侧
frpc配置
```toml
# frpc.toml
serverAddr = "x.x.x.x"  # 服务器IP
serverPort = 12345  # 服务器监听端口
auth.token = "p@ssw0rd"  # 鉴权配置

[[visitors]]
name = "Raspberry_Pi_ssh_visitor"
type = "stcp"
serverName = "Raspberry_Pi_ssh"
secretKey = "abcdefg"  # 设置为与被访问者secretKey配置一致
bindAddr = '127.0.0.1'  # 绑定到的IP
bindPort = 8022  # 绑定到的端口，结合IP，在本机访问127.0.0.1:8022等同于访问被访问者给定端口
```
### 带登录验证的网页映射
#### 服务器侧
frps配置
```toml
bindPort = 1357  # 服务端监听端口
vhostHTTPPort = 2468  # 访问者访问端口，即映射到的端口
auth.token = "p@ssw0rd"  # 鉴权配置
```
service配置
```text
[Unit]
Description = Nginx
After = network.target syslog.target
Wants = network.target

[Service]
Type = simple
# 启动frps的命令，需修改内容
ExecStart = /path/to/frps -c /path/to/toml

[Install]
WantedBy = multi-user.target
```
#### 客户端侧
frpc配置
```toml
serverAddr = "x.x.x.x"  # 服务器IP
serverPort = 1357  # 服务端监听端口
auth.token = "p@ssw0rd"  # 鉴权配置

[[proxies]]
name = "Nginx"
type = "http"
localIP = "192.168.3.30"  # 局域网Nginx IP
localPort = 8123  # 局域网Nginx port
customdomains = ["x.x.x.x"]  # 服务器IP，这样省得设置hosts
httpUser = "admin"  # 访问鉴权 用户名
httpPassword = "admin"  # 访问鉴权 密码
```
在此之后，需要在HomeAssistant的`/config/configuration.yaml`添加以下内容
```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 127.0.0.1
    - 192.168.3.30  # 根据实际HomeAssistant局域网IP更改
```
  
service配置
```text
[Unit]
Description = frp HASS client
After = network.target syslog.target
Wants = network.target

[Service]
Type = simple
ExecStart = /path/to/frpc -c /path/to/toml
Restart = on-failure
RestartSec = 60

[Install]
WantedBy = multi-user.target
```