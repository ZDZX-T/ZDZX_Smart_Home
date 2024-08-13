"""
分享流的时候为了验证删除隐私信息后的流加载是否正常，需要将流再次导入Node-RED
但是因为id们和已有的重复了，所以可能会掩盖一些问题
为了避免id重复，我写了这个脚本，可以将所有的id值+1，这样就避免与之前的重复了
<肯定>会有遗漏的更改点，请自行添加或提交issue

会自动删除server节点
会自动删除结点server、区域、设备、实体的值
"""
import json
from os.path import split, splitext, join, dirname


def string_hex_plus_1(string):
    ret = hex((int(string, 16) + 1) % 0x10000000000000000)[2:]
    if len(ret) != 16:
        ret = '0'*(16-len(ret)) + ret
    return ret


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        return json_data


if __name__ == '__main__':
    path = input('请将要批量改id的json文件拖到此处')
    new_file = join(dirname(path), splitext(split(path)[1])[0] + '_new.json')
    data = read_json_file(path)
    new_data = []
    for i in data:
        if i['type'] == 'server':  # 跳过server节点，即删除
            continue

        target = 'id'
        if target in i:
            i[target] = string_hex_plus_1(i[target])

        target = 'z'
        if target in i:
            i[target] = string_hex_plus_1(i[target])

        target = 'entityConfig'
        if target in i:
            i[target] = string_hex_plus_1(i[target])

        target = 'wires'
        if target in i:
            for j in range(len(i[target])):
                for k in range(len(i[target][j])):
                    i[target][j][k] = string_hex_plus_1(i[target][j][k])

        target = 'links'
        if target in i:
            for j in range(len(i[target])):
                i[target][j] = string_hex_plus_1(i[target][j])

        target = 'server'
        if target in i:
            i[target] = ''

        target = 'areaId'
        if target in i:
            i[target] = []

        target = 'deviceId'
        if target in i:
            i[target] = []

        target = 'entityId'
        if target in i:
            i[target] = []

        new_data.append(i)

    with open(new_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)
    print('更改后的文件已存储在{}'.format(new_file))
