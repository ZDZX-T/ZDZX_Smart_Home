# 安装ESPHome

官方指导[https://esphome.io/guides/getting_started_command_line](https://esphome.io/guides/getting_started_command_line)

## 拉取文件
```shell
sudo docker pull ghcr.io/esphome/esphome
```

## 更新compose.yaml文件内容
追加以下内容，注意最后的environment部分，可以设置也可以去掉
```yaml
  esphome:
    container_name: esphome
    image: ghcr.io/esphome/esphome
    volumes:
      - /home/HA/esphome:/config
      - /etc/localtime:/etc/localtime:ro
    network_mode: host  # 因为需要发现网络设备，所以网络模式是host
    # ports:
    #   - "6052:6052"  # Web UI
    #   - "6053:6053"  # API
    restart: unless-stopped
    user: "${HA_UID}:${HA_GID}"  # 可选
    # privileged: true  # 需要刷写固件可以改成挂载具体设备
    # environment:  # 可选
    #   - USERNAME=test
    #   - PASSWORD=ChangeMe
```

## 修改esphome目录权限
```shell
sudo mkdir -p /home/HA/esphome && sudo chown -R HA:HA /home/HA/esphome
```

## 启动ESPHome
```shell
sudo docker compose up -d
```

## 将ESPHome集成到HA
在HA的`设置->仪表盘->添加仪表盘->网页`写上ESPHome的网址，点击下一步  
名称填ESPHome，图标搜chip，然后第三个网址用默认的dashboard-esphome即可