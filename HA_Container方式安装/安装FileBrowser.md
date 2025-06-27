# 安装FileBrowser

## 拉取文件
```shell
sudo docker pull filebrowser/filebrowser:latest
```

## 更新compose.yaml文件内容
追加以下内容
```yaml
  filebrowser:
    container_name: filebrowser
    image: filebrowser/filebrowser:latest
    ports:
      - "50123:80" # 访问端口可以根据需要调整
    volumes:
      - /home/HA:/srv
      - /home/HA/filebrowser:/etc/filebrowser
    command: ["-d", "/etc/filebrowser/database.db"]
    restart: unless-stopped
```

## 启动FileBrowser
```shell
sudo docker compose up -d
```

## 查看密码
```shell
sudo docker logs filebrowser
```
有一行*Generated random admin password for quick setup:*，后面就是默认密码

## 将FileBrowser集成到HA
在HA的`设置->仪表盘->添加仪表盘->网页`写上FileBrowser的网址，点击下一步  
名称填FileBrowser，图标搜file

## 更改界面为中文
进入FileBrowser网页后，在`Settings->Profile Settings->Language`选中文然后点击`Update`即可