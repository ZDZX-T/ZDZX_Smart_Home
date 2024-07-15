#### 获取位置
* 请求属性  

| 描述 | 值                |
|----|------------------|
| 方法 | GET              |
| 路径 | /wechat/location |

* 请求查询参数  

| 参数名           | 释义  | 样例                                   | 备注     |
|---------------|-----|--------------------------------------|--------|
| caridentifier | 车架号 | XXXXXXXXXXXXXXXXX                    | 根据实际填写 |
| timeStamp     | 时间戳 | 1721059643055                        | 根据实际生成 |
| random        | 随机值 | 0de802b2-ad6e-372b-0793-5d29879625d4 | 自己随机生成 |
| longitude     | 经度  | 0                                    | 填0即可   |
| latitude      | 纬度  | 0                                    | 填0即可   |
