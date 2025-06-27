# 安装Mosquitto

## 拉取文件
```shell
sudo docker pull library/eclipse-mosquitto:latest
```

## 创建配置文件
```shell
sudo mkdir -p /home/HA/mosquitto/data
sudo mkdir -p /home/HA/mosquitto/log
sudo touch /home/HA/mosquitto/mosquitto.conf
sudo touch /home/HA/mosquitto/pwfile.example
sudo chown -R HA:HA /home/HA/mosquitto
sudo chmod 0700 /home/HA/mosquitto/pwfile.example
```
在`/home/HA/mosquitto/mosquitto.conf`内填充如下内容
```text
# mosquitto.conf
listener 1883

# 启用 WebSocket 支持（可选）
listener 9001
protocol websockets

# 持久化设置（可选）
persistence true
persistence_location /mosquitto/data/

# 日志设置（可选）
log_dest file /mosquitto/log/mosquitto.log

# 禁用匿名登录，等在modquitto内创建了pwfile.example再取消注释
# allow_anonymous false
# password_file /mosquitto/config/pwfile.example
```

## 更新compose.yaml文件内容
追加以下内容
```yaml
  mosquitto:
    image: library/eclipse-mosquitto:latest
    container_name: mosquitto
    ports:
      - "1883:1883"
      - "9001:9001"
    volumes:
      - /home/HA/mosquitto/pwfile.example:/mosquitto/config/pwfile.example
      - /home/HA/mosquitto/mosquitto.conf:/mosquitto/config/mosquitto.conf
      - /home/HA/mosquitto/data:/mosquitto/data
      - /home/HA/mosquitto/log:/mosquitto/log
    restart: unless-stopped
    user: "${HA_UID}:${HA_GID}"
```

## 启动Mosquitto
```shell
sudo docker compose up -d
```

## 设置密码
进入mosquitto docker
```shell
sudo docker exec -it mosquitto sh
```
添加mosquitto用户名密码
```shell
mosquitto_passwd -c /mosquitto/config/pwfile.example 用户名
```
返回宿主机
```shell
exit
```
停止mosquitto
```shell
sudo docker compose down mosquitto
```
取消mosquitto.conf文件里的禁用匿名登录注释
```shell
sudo vim /home/HA/mosquitto/mosquitto.conf
```
重启mosquitto
```shell
sudo docker compose up -d
```