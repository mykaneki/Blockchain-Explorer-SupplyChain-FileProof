# ChainMaker-Python-SDK

长安链Python SDK

## 特性
目前python-sdk 除了**不支持private_compute**、**hibe**及**国密通信**外，支持go-sdk所有接口，
支持列表如下：
- 链查询（系统合约）apis/system_contract.py
- 链配置管理 apis/chain_config.py
- 用户合约管理 apis/user_contract.py
- 证书管理 apis/cert_manage.py
- 公钥管理 apis/pubkey_manage.py
- Gas管理 apis/gas_manage.py
- 证书别名管理 apis/cert_alias_manage.py
- 归档 apis/archive.py
- 多签 apis/multisign_contract.py
- 订阅 apis/subscribe.py

> 详细接口及使用方式可以查看 apis/base_client.py

另外
- 支持PermissionedWithCert、PermissionedWithKey、Public三种模式
- PermissionedWithCert模式下，支持启用证书哈希（短证书）、支持证书别名
- 支持RSA、EC加密，及SHA256哈希算法
- 支持EVM合约名称、方法、参数转换 utils/evm_utils.calc_evm_contarct_name calc_evm_method_params
- 支持EVM账户地址生成、至信链地址生成 utils/crypto_utils.get_evm_address_from_public_key get_zx_address_from_public_key
- 支持crl吊销文件生成 utils/crypto_utils/create_crl_bytes
- 支持归档及恢复逻辑 utils/archive_utils.ArchiveUtils
- 支持日志 cc.logger 默认只输出到控制台,不输出到文件
- 支持链接池 cc.pool
- 支持同步获取交易结果 cc.send_request_with_sync_result(payload, endorsers, with_sync_result=True)

## 环境依赖

**Python**

版本为Python3.6或以上
下载地址：https://www.python.org/downloads/
若已安装，请通过命令查看版本：

```
$  python3 --version
Python 3.8.2
```

## 下载安装

```shell
$ pip3 install git+https://git.chainmaker.org.cn/chainmaker/sdk-python.git
```

> TODO: 发布到PyPi `pip3 install chainmaker`

## 示例代码

### 创建节点

> 注️：需要拷贝目标链chainmaker-go/build/crypto-config到脚本所在目录

```python
from chainmaker.node import Node

# 创建节点
node = Node(
    node_addr='127.0.0.1:12301',
    conn_cnt=10,
    enable_tls=True,
    cas=['./testdata/crypto-config/wx-org1.chainmaker.org/ca', './testdata/crypto-config/wx-org2.chainmaker.org/ca'],
    tls_host_name='chainmaker.org'
)
```

### 以参数形式创建ChainClient

> 更多内容请参考：`tests/test_chain_client.py`
>
> 注：示例中证书采用路径方式去设置，也可以使用证书内容去设置，具体请参考`createClientWithCaCerts`方法

```python
from chainmaker.chain_client import ChainClient
from chainmaker.node import Node
from chainmaker.user import User
from chainmaker.utils import file_utils
    
user = User('wx-org1.chainmaker.org',
            sign_key_bytes=file_utils.read_file_bytes('./testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.tls.key'),
            sign_cert_bytes=file_utils.read_file_bytes('./testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.tls.crt'),
            tls_key_bytes=file_utils.read_file_bytes('./testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.sign.key'),
            tls_cert_bytes=file_utils.read_file_bytes('./testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.sign.crt')
            )

node = Node(
    node_addr='127.0.0.1:12301',
    conn_cnt=1,
    enable_tls=True,
    trust_cas=[
        file_utils.read_file_bytes('./testdata/crypto-config/wx-org1.chainmaker.org/ca/ca.crt'),
        file_utils.read_file_bytes('./testdata/crypto-config/wx-org2.chainmaker.org/ca/ca.crt')
    ],
    tls_host_name='chainmaker.org'
)

cc = ChainClient(chain_id='chain1', user=user, nodes=[node])
print(cc.get_chainmaker_server_version())
```

### 以配置文件形式创建ChainClient

> 注：参数形式和配置文件形式两个可以同时使用，同时配置时，以参数传入为准

```python
from chainmaker.chain_client import ChainClient

# ./testdata/sdk_config.yml 中私钥/证书等如果使用相对路径应相对于当前运行起始目录
cc = ChainClient.from_conf('./testdata/sdk_config.yml')
```

> [配置文件 sdk_config.yml 格式参考](https://docs.chainmaker.org.cn/operation/配置文件一览.html#sdk-config-yml)

### 创建合约

```python
from google.protobuf import json_format
from chainmaker.chain_client import ChainClient
from chainmaker.utils.evm_utils import calc_evm_contract_name
from chainmaker.keys import RuntimeType

endorsers_config = [{'org_id': 'wx-org1.chainmaker.org',
                  'user_sign_crt_file_path': './testdata/crypto-config/wx-org1.chainmaker.org/user/admin1/admin1.sign.crt',
                  'user_sign_key_file_path': './testdata/crypto-config/wx-org1.chainmaker.org/user/admin1/admin1.sign.key'},
                  {'org_id': 'wx-org2.chainmaker.org',
                  'user_sign_crt_file_path': './testdata/crypto-config/wx-org2.chainmaker.org/user/admin1/admin1.sign.crt',
                  'user_sign_key_file_path': './testdata/crypto-config/wx-org2.chainmaker.org/user/admin1/admin1.sign.key'},
                  {'org_id': 'wx-org3.chainmaker.org',
                  'user_sign_crt_file_path': './testdata/crypto-config/wx-org3.chainmaker.org/user/admin1/admin1.sign.crt',
                  'user_sign_key_file_path': './testdata/crypto-config/wx-org3.chainmaker.org/user/admin1/admin1.sign.key'},
                  ]

cc = ChainClient.from_conf('./testdata/sdk_config.yml')

def create_contract(contract_name: str, version: str, byte_code_path: str, runtime_type: RuntimeType, params: dict = None, 
                    with_sync_result=True) -> dict:
    """创建合约"""
    # 创建请求payload
    payload = cc.create_contract_create_payload(contract_name, version, byte_code_path, runtime_type, params)
    # 创建背书
    endorsers = cc.create_endorsers(payload, endorsers_config)
    # 携带背书发送请求
    res = cc.send_request_with_sync_result(payload, with_sync_result=with_sync_result, endorsers=endorsers)
    # 交易响应结构体转为字典格式
    return json_format.MessageToDict(res)

# 创建WASM合约，本地合约文件./testdata/claim-wasm-demo/rust-fact-2.0.0.wasm应存在
result1 = create_contract('fact', '1.0', './testdata/claim-wasm-demo/rust-fact-2.0.0.wasm', RuntimeType.WASMER, {})
print(result1)

# 创建EVM合约，本地合约文件./testdata/balance-evm-demo/ledger_balance.bin应存在

contract_name = calc_evm_contract_name('balance001')
result2 = create_contract(contract_name, '1.0', './testdata/balance-evm-demo/ledger_balance.bin', RuntimeType.EVM)
print(result2)
```

### 调用合约

```python
from google.protobuf import json_format
from chainmaker.chain_client import ChainClient
from chainmaker.utils.evm_utils import calc_evm_contract_name, calc_evm_method_params

# 创建客户端
cc = ChainClient.from_conf('./testdata/sdk_config.yml')

# 调用WASM合约
res1 = cc.invoke_contract('fact', 'save', {"file_name":"name007","file_hash":"ab3456df5799b87c77e7f88","time":"6543234"},
                          with_sync_result=True)
# 交易响应结构体转为字典格式
print(json_format.MessageToDict(res1))

# 调用EVM合约
evm_contract_name = calc_evm_contract_name('balance001')
evm_method, evm_params = calc_evm_method_params('updateBalance', [{"uint256": "10000"}, {"address": "0xa166c92f4c8118905ad984919dc683a7bdb295c1"}])
res2 = cc.invoke_contract(evm_contract_name, evm_method, evm_params, with_sync_result=True)
# 交易响应结构体转为字典格式
print(json_format.MessageToDict(res2))
```

### 更多示例和用法

> 更多示例和用法，请参考单元测试用例

| 功能     | 单测代码                      |
| -------- | ----------------------------- |
| 用户合约 | `tests/test_user_contract.py`   |
| 系统合约 | `tests/test_system_contract.py` |
| 链配置   | `tests/test_chain_config.py`    |
| 证书管理 | `tests/test_cert_manage.py`     |
| 消息订阅 | `tests/test_user_contract.py`       |

## 接口说明

提供Go、Java、JS、Python多语言SDK。

各语言版本需要覆盖的接口有：

## 接口清单

- [x] 已实现 ✅ 测试通过

### 1 用户合约接口

- [x] 1.1 生成合约创建待签名Payload cc.create_contract_create_payload ✅
- [x] 1.2 生成合约升级待签名Payload cc.create_contract_upgrade_payload ✅
- [x] 1.3 生成合约冻结待签名Payload cc.create_contract_freeze_payload ✅
- [x] 1.4 生成合约解冻待签名Payload cc.create_contract_unfreeze_payload ✅
- [x] 1.5 生成合约吊销待签名Payload cc.create_contract_revoke_payload ✅
- [x] 1.6 签名合约管理Payload cc.sign_contract_manage_payload ✅
- [ ] 1.7 合约管理Payload签名收集&合并
- [x] 1.8 发送合约管理请求（创建、更新、冻结、解冻、吊销）cc.send_contract_manage_request ✅
- [x] 1.9 调用合约 cc.invoke_contract ✅
- [x] 1.10 查询合约 cc.query_contract ✅
- [x] 1.11 获取交易请求体 cc.get_tx_request ✅
- [x] 1.12 发送交易请求体 cc.send_tx_request ✅

### 2 系统合约接口

- [x] 2.1 根据交易ID获取交易信息 cc.get_tx_by_tx_id ✅
- [x] 2.2 根据区块高度获取区块信息 cc.get_block_by_height ✅
- [x] 2.3 根据区块哈希获取区块信息 cc.get_block_by_hash
- [x] 2.4 根据交易ID获取区块信息 cc.get_block_by_tx_id ✅
- [x] 2.5 获取最新的配置块信息 cc.get_last_config_block ✅
- [x] 2.6 获取最新区块信息 cc.get_last_block ✅
- [x] 2.7 获取链信息 cc.get_chain_info ✅
- [x] *2.8* 获取链配置 cc.get_chain_config ✅
- [x] *2.9* 获取节点加入的链列表 cc.get_node_chain_list ✅
- [x] *2.10* 根据区块高度获取完整区块信息 cc.get_full_block_by_height ✅
- [x] *2.11* 根据交易ID获取区块高度 cc.get_block_height_by_tx_id ✅
- [x] *2.12* 根据区块哈希获取区块高度 cc.get_block_height_by_hash
- [x] *2.13* 获取已归档的区块高度 cc.get_archived_block_height ✅
- [x] *2.14* ~~根据交易ID或区块hash获取区块高度 cc.get_block_height~~ ✅  # TODO 转为私有方法 _get_block_height
- [x] *2.15* 获取当前区块高度 cc.get_current_block_height ✅
- [x] *2.16* 根据区块高度获取区块头信息 cc.get_block_header_by_height ✅
- [x] *2.17* 调用系统合约 cc.invoke_system_contract
- [x] *2.18* 查询系统合约 cc.query_system_contract

### 3 链配置接口

- [x] 3.1 获取链配置 cc.get_chain_config ✅
- [x] 3.2 根据区块高度获取链配置 cc.get_chain_config_by_block_height ✅
- [x] 3.3 获取链配置序号 cc.get_chain_config_sequence ✅
- [ ] 3.4 签名链配置更新Payload cc.sign_chain_config_payload ✅
- [ ] 3.5 链配置更新Payload签名收集&合并
- [ ] 3.6 发送链配置更新请求
- [x] 3.7 生成链配置Core模块更新待签名Payload cc.create_chain_config_core_update_payload ✅
- [x] 3.7 生成链配置Block模块更新待签名Payload cc.create_chain_config_block_update_payload ✅
- [x] 3.8 生成链配置信任组织根证书添加待签名Payload cc.create_chain_config_trust_root_add_payload ✅
- [x] 3.9 生成链配置信任组织根证书更新待签名Payload cc.create_chain_config_trust_root_update_payload ✅
- [x] 3.10 生成链配置信任组织根证书删除待签名Payload cc.create_chain_config_trust_root_delete_payload ✅
- [x] 3.11 生成链配置权限配置添加待签名Payload cc.create_chain_config_permission_add_payload ✅
- [x] 3.12 生成链配置权限配置更新待签名Payload cc.create_chain_config_permission_update_payload ✅
- [x] 3.13 生成链配置权限配置删除待签名Payload cc.create_chain_config_permission_delete_payload ✅
- [x] 3.14 生成链配置共识节点地址添加待签名Payload cc.create_chain_config_consensus_node_id_add_payload ✅
- [x] 3.15 生成链配置共识节点地址更新待签名Payload cc.create_chain_config_consensus_node_id_update_payload ✅
- [x] 3.16 生成链配置共识节点地址删除待签名Payload cc.create_chain_config_consensus_node_id_delete_payload ✅
- [x] 3.17 生成链配置共识节点组织添加待签名Payload cc.create_chain_config_consensus_node_org_add_payload ✅
- [x] 3.18 生成链配置共识节点组织更新待签名Payload cc.create_chain_config_consensus_node_org_update_payload ✅
- [x] 3.19 生成链配置共识节点组织删除待签名Payload cc.create_chain_config_consensus_node_org_delete_payload ✅
- [x] 3.20 生成链配置共识扩展字段添加待签名Payload cc.create_chain_config_consensus_ext_add_payload ✅
- [x] 3.21 生成链配置共识扩展字段更新待签名Payload cc.create_chain_config_consensus_ext_update_payload ✅
- [x] 3.22 生成链配置共识扩展字段删除待签名Payload cc.create_chain_config_consensus_ext_delete_payload ✅
- [ ] 3.23 生成链配置第三方证书信息添加待签名Payload cc.create_chain_config_trust_member_add_payload
- [ ] 3.24 ~~生成链配置更新第三方证书信息Payload cc.create_chain_config_trust_member_update_payload~~
- [ ] 3.25 生成链配置第三方证书信息删除待签名Payload cc.create_chain_config_trust_member_delete_payload

### 4 证书管理接口

- [x] 4.1 添加证书 cc.add_cert ✅
- [x] 4.2 删除证书 cc.delete_cert ✅
- [x] 4.3 查询证书 cc.query_cert ✅
- [x] 4.4 获取证书哈希值 cc.get_cert_hash ✅
- [x] 4.5 生成证书管理待签名Payload cc.create_cert_manage_payload ✅
- [x] 4.6 生成证书冻结待签名Payload cc.create_cert_manage_frozen_payload ✅
- [x] 4.7 生成证书解冻待签名Payload cc.create_cert_manage_unfrozen_payload ✅
- [x] 4.8 生成证书吊销待签名Payload cc.create_cert_manage_revocation_payload ✅
- [x] 4.9 签名证书管理Payload cc.sign_cert_manage_payload ✅
- [ ] 4.10 证书管理Payload签名收集&合并
- [x] 4.11 发送证书管理请求 cc.send_cert_manage_request ✅

### 5 在线多签接口

- [x] 5.1 待签payload签名
- [x] 5.2 多签请求
- [x] 5.3 多签投票
- [x] 5.4 投票获取

### 6 消息订阅接口

- [x] 6.1 区块订阅 cc.subscribe_block
- [x] 6.2 交易订阅 cc.subscribe_tx
- [x] 6.3 多合一订阅 cc.subscribe

### 7 证书压缩

- [x] 7.1 启用压缩证书功能 cc.enable_cert_hash
- [x] 7.2 停用压缩证书功能 cc.disable_cert_hash

### 8 工具类

- [ ] 8.1 将EasyCodec编码解码成map
- [ ] 8.2 根据X.509证书路径得到EVM地址
- [ ] 8.3 根据X.509证书内容得到EVM地址

### 9 层级属性加密类接口

- [ ] 9.1 生成层级属性参数初始化交易待签名Payload
- [ ] 9.2 生成层级属性加密交易待签名Payload，加密参数已知
- [ ] 9.3 生成层级属性加密交易待签名Payload，参数由链上获取得出
- [ ] 9.5 已知交易id，根据私钥解密密文交易

### 10 系统类接口

- [x] 10.1 SDK停止接口 ✅
- [x] 10.2 获取链版本 ✅

### 11 公钥管理

> 仅适用于 permissionedWithKey 模式

- [x] 11.1 生成公钥添加待签名Payload cc.create_pubkey_add_payload ✅
- [x] 11.1 生成公钥删除待签名Payload cc.create_pubkey_del_payload ✅
- [x] 11.1 生成公钥获取待签名Payload cc.create_pubkey_query_payload ✅
- [x] 11.1 发送公钥管理请求 cc.send_pubkey_manage_request ✅

### 12 Gas 计费管理

> 仅使用于 Pubic 模式

- [x] 12.1 获取Gas管理员地址 cc.get_gas_admin ✅
- [x] 12.2 获取Gas账户余额 cc.get_gas_balance ✅
- [x] 12.3 获取Gas账户状态 cc.get_gas_account_status ✅
- [x] 12.4 生成设置Gas管理员地址待签名Payload cc.create_set_gas_admin_payload ✅
- [x] 12.5 生成Gas充值待签名Payload cc.create_recharge_gas_payload ✅
- [x] 12.6 生成Gas退款待签名Payload cc.create_refund_gas_payload ✅
- [x] 12.7 生成Gas冻结待签名Payload cc.create_frozen_gas_account_payload ✅
- [x] 12.8 生成Gas解冻待签名Payload cc.create_unfrozen_gas_account_payload ✅
- [x] 12.9 发送Gas管理请求  cc.send_gas_manage_request
- [x] 12.10 附加Gas限制 cc.attach_gas_limit

## TODO

- [ ] 支持国密
## 参考

- [chainmaker-docs](https://docs.chainmaker.org.cn/index.html)
- [gRPC Python](https://grpc.github.io/grpc/python)
- [grpcio](https://grpc.io/docs/languages/python/quickstart/)
- [cryptography](https://cryptography.io/)
- [eth-abi](https://eth-abi.readthedocs.io/en/latest/)
- [asn1](https://github.com/andrivet/python-asn1/blob/master/tests/test_asn1.py)

