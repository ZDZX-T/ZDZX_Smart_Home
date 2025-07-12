# 安装Node-RED

官方指导[https://nodered.org/docs/getting-started/docker#docker-stack--docker-compose](https://nodered.org/docs/getting-started/docker#docker-stack--docker-compose)

## 拉取文件
```shell
sudo docker pull nodered/node-red:latest
```

## 更新compose.yaml文件内容
追加以下内容
```yaml
  node-red:
    container_name: node-red
    image: nodered/node-red:latest
    volumes:
      - /home/HA/node-red/data:/data
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "1880:1880"
    restart: unless-stopped
    user: "${HA_UID}:${HA_GID}"
```

## 修改node-red目录权限
```shell
sudo mkdir -p /home/HA/node-red/data
sudo chown -R HA:HA /home/HA/node-red
```

## 启动Node-RED
```shell
sudo docker compose up -d
```

## 将Node-RED集成到HA
在HA的`设置->仪表盘->添加仪表盘->网页`写上Node-RED的网址，点击下一步  
名称填Node-RED，图标搜sitemap，然后第三个网址用默认的node-red即可

## 安装Node-RED插件
Node-RED界面`右上角三条杠->设置->控制板->安装`，搜索安装以下插件（可选）
1. **node-red-contrib-home-assistant-websocket**
2. node-red-node-base64
3. node-red-node-email
4. node-red-contrib-time-range-switch
5. node-red-contrib-cast
6. node-red-contrib-counter
7. node-red-contrib-interval-length
8. node-red-contrib-persistent-fsm
9. node-red-contrib-sunevents
10. node-red-node-ping
11. node-red-node-random
12. node-red-node-smooth
13. node-red-node-suncalc

## 添加Home Assistant server节点
### 获取HA令牌
1. 在HA中点击自己左下角的头像
2. 在上方选择`安全`页签
3. 在最后的长期访问令牌处点击`创建令牌`，名称叫Node-RED，点击确定后复制Access token
### 配置server节点
1. 在Node-RED中从侧边栏home assistant entities组拖一个button到流程中
2. 双击button节点，点击Entity Config右侧的加号
3. 点击Server右侧的加号
4. 基本URL填入你Home Assistant主页的链接，访问令牌填入刚才在HA创建的令牌，然后点击添加即可