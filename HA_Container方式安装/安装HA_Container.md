# 安装HA Container

官网教程[https://www.home-assistant.io/installation/linux#install-home-assistant-container](https://www.home-assistant.io/installation/linux#install-home-assistant-container)

## 设置HA专用用户
```shell
sudo useradd -rm HA
sudo usermod -L HA
sudo usermod -aG HA $(logname)
# 有时权限刷新不及时，执行下方命令刷新当前shell环境
exec su - $USER
```
该专用账户不可登陆

未来的目录结构大体如下
```text
/home/HA
├── compose.yml               # 所有服务的容器定义
├── config/                   # Home Assistant 的核心配置目录
│   ├── configuration.yaml
│   ├── secrets.yaml
│   └── ...                   # 其他 HA 相关配置文件
├── nodered/                  # Node-RED 数据持久化目录
│   └── data/
├── mosquitto/                # Mosquitto MQTT Broker 配置目录
│   ├── mosquitto.conf
│   └── data/
├── esphome/                  # ESPHome 项目文件夹
│   └── your-device-name.yaml # 每个设备一个 YAML 文件
└── backups/                  # 可选：用于存放配置备份
```

## 拉取文件
```shell
sudo docker pull ghcr.io/home-assistant/home-assistant:stable
```
如果是从其他地方拉的，可以改tag
```shell
sudo docker tag 某某网站/homeassistant/home-assistant:stable ghcr.io/home-assistant/home-assistant:stable
```
被改的tag名称可以通过下方命令查
```shell
sudo docker images
```
删除tag命令是
```shell
docker rmi ghcr.io/home-assistant/home-assistant:stable
```

## 生成docker compose文件
```shell
sudo touch /home/HA/compose.yaml
sudo vim /home/HA/compose.yaml
```
在`/home/HA/compose.yaml`中写入以下内容
```yaml
services:
  homeassistant:
    container_name: homeassistant
    image: "ghcr.io/home-assistant/home-assistant:stable"
    volumes:
      - /home/HA/config:/config
      - /etc/localtime:/etc/localtime:ro
      - /run/dbus:/run/dbus:ro
    restart: unless-stopped
    privileged: true
    network_mode: host
```
使用`id HA`命令查询HA的UID和GID，并将其写入到/home/HA/.env里
```text
HA_UID = 查询到的UID
HA_GID = 查询到的GID
```

## 设置开机自启
创建一个systemd服务文件
```shell
sudo vim /etc/systemd/system/HomeAssistant.service
```
写入下方内容
```text
[Unit]
Description=HA Container
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/home/HA
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
TimeoutStartSec=0
StartLimitIntervalSec=60
StartLimitBurst=3

[Install]
WantedBy=multi-user.target
```
重新加载systemd配置并启用服务
```shell
sudo systemctl daemon-reload
sudo systemctl enable HomeAssistant.service
```
启动服务
```shell
sudo systemctl start HomeAssistant.service
```

## 登录HA
访问`http://服务器IP:8123`，根据自己情况选择新建还是还原备份

## 未来更新HA
```shell
cd /home/HA
# Step 1: 拉取最新的 stable 镜像，如果显示"Image is up to date"说明不用更新
sudo docker pull ghcr.io/home-assistant/home-assistant:stable
# 更新容器
sudo docker compose stop homeassistant
sudo docker compose rm -f homeassistant
sudo docker compose up -d homeassistant
```
如果要更新所有镜像，那么直接
```shell
sudo docker compose pull
sudo docker compose down
sudo docker compose up -d
```