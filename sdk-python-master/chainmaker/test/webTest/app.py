'''
服务器主程序
'''
from flask import Flask, render_template, request
from chainmaker.chain_client import ChainClient
import json
import os
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域访问
cc = ChainClient.from_conf('./testdata/sdk_config.yml')  # 证书配置文件地址


# res为字符串，该方法处理字符串，提取字符串中的数据转化成json格式
def contractResult2json(res):
    file_hash_start = res.find('file_hash')
    file_name_start = res.find('file_name')
    time_start = res.find('time')
    gas_used_start = res.find('gas_used')
    tx_id_start = res.find('tx_id')
    file_hash = res[file_hash_start + 14:file_name_start - 5]
    file_name = res[file_name_start + 14:time_start - 5]
    time = res[time_start + 7:gas_used_start - 5]
    gas_used = res[gas_used_start + 10:tx_id_start - 3]
    tx_id = res[tx_id_start + 8:-1]
    message = json.dumps(
        {'file_hash': file_hash, 'file_name': file_name, 'time': time, 'gas_used': gas_used, 'tx_id': tx_id})
    return message


@app.get('/qq')  # 获取区块链信息接口
def get_message():
    res1 = cc.get_chain_info()  # 从长安链中获取数据
    message = {}  # 字典保存长安链获取到的信息
    res1 = str(res1)
    chainHeight = res1.split('\n')[0].split(' ')[1]  # 高度
    nodeList = []  # 节点列表
    message['block_height'] = chainHeight
    nodes = res1.split('\n')
    for i in range(len(nodes)):
        if nodes[i].startswith('node_list {'):
            tmp = {"node_id": nodes[i + 1].split(': ')[1], "node_address": nodes[i + 2].split(': ')[1]}
            nodeList.append(tmp)
    message["node_list"] = nodeList
    print('--------------------')
    message = json.dumps(message)
    print(message)
    return message


@app.get('/findFileNameByHash')  # 通过哈希值找文件名接口
def get_file_name_by_hash():
    hashValue = request.args.get('hash')
    res1 = cc.invoke_contract('fact', 'find_by_file_hash', {"file_hash": hashValue}, with_sync_result=True)
    res1 = str(res1)
    message = contractResult2json(res1)
    print(message)
    return message


@app.get('/getProductMsgById')  # 查询产品信息接口
def get_product_msg():
    productId = request.args.get('productId')
    print(productId)
    output = subprocess.check_output(
        'sudo /home/ubuntu/chainmaker-go/tools/cmc/cmc client contract user invoke --contract-name=SupplyChain --method=getProduct --sdk-conf-path=./testdata/sdk_config.yml --params="[{\\"productId\\": \\"' + productId + '\\"}]" --sync-result=true --abi-file-path=/home/ubuntu/sol/SupplyChain.abi',
        shell=True, text=True)
    result = json.loads(output)
    return result


@app.post('/postProductMsg')  # 上传产品接口
def post_product_msg():
    productName = request.form.get('productName')
    print(productName)
    output = subprocess.check_output(
        'sudo /home/ubuntu/chainmaker-go/tools/cmc/cmc client contract user invoke --contract-name=SupplyChain --method=addProduct --sdk-conf-path=./testdata/sdk_config.yml --params="[{\\"name\\": \\"' + productName + '\\"}]" --sync-result=true --abi-file-path=/home/ubuntu/sol/SupplyChain.abi',
        shell=True, text=True)
    result = json.loads(output)
    return result


@app.post('/transformerOwner')  # 转移拥有者接口
def transformer_owner():
    productId = request.form.get('productId')
    newOwner = request.form.get('newOwner')
    print(productId)
    print(newOwner)
    output = subprocess.check_output(
        'sudo /home/ubuntu/chainmaker-go/tools/cmc/cmc client contract user invoke --contract-name=SupplyChain --method=transferOwnership --sdk-conf-path=./testdata/sdk_config.yml --params="[{\\"productId\\": \\"' + productId + '\\",\\"newOwner\\": \\"' + newOwner + '\\"}]" --sync-result=true --abi-file-path=/home/ubuntu/sol/SupplyChain.abi',
        shell=True, text=True)
    result = json.loads(output)

    return result


@app.post('/setProductAvailability')  # 设置产品可用性接口
def setProductAvailability():
    productId = request.form.get('productId')
    isAvailable = request.form.get('isAvailable')
    output = subprocess.check_output(
        'sudo /home/ubuntu/chainmaker-go/tools/cmc/cmc client contract user invoke --contract-name=SupplyChain --method=setProductAvailability --sdk-conf-path=./testdata/sdk_config.yml --params="[{\\"productId\\": \\"' + productId + '\\",\\"isAvailable\\": \\"' + isAvailable + '\\"}]" --sync-result=true --abi-file-path=/home/ubuntu/sol/SupplyChain.abi',
        shell=True, text=True)
    result = json.loads(output)
    return result


@app.post('/fileMessageUpload')  # 上传文件信息接口
def post_file_message_upload():
    file_name = request.form.get('fileName')
    file_hash = request.form.get('fileHash')
    time = request.form.get('time')
    res1 = cc.invoke_contract('fact', 'save', {"file_name": file_name, "file_hash": file_hash, "time": time},
                              with_sync_result=True)
    res1 = str(res1)
    print(res1)
    return res1


# 测试页面
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/function')
def function():
    return render_template('function.html')


@app.route('/blockchain.html')
def blockchainhtml():
    return render_template('blockchain.html')


@app.route('/blockchain.css')
def blockchaincss():
    return render_template('blockchain.css')


@app.route('/blockchain.js')
def blockchainjs():
    return render_template('blockchain.js')


@app.route('/fileUpload.html')
def fiileUpload():
    return render_template('fileUpload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
