#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   conftest.py
# @Function     :   pytest框架测试配置

import os
import sys
import uuid
from typing import Union

from chainmaker.utils.evm_utils import calc_evm_contract_name
from tests.utils.cropto_config_utils import CryptoConfigUtils
TESTS_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(TESTS_DIR)

sys.path.insert(0, PROJECT_ROOT)

import pytest

from chainmaker.chain_client import ChainClient
from chainmaker.user import User
from chainmaker.utils import file_utils, common


def pytest_addoption(parser):
    """添加ini配置项"""
    parser.addoption('--sdk-config', action='store', help='sdk_config.yml path')
    parser.addini('sdk_config', help='sdk_config.yml path')


@pytest.fixture
def config_dir():
    """返回配置目录路径 tests/config"""
    return os.path.abspath(os.path.join(TESTS_DIR, 'resources'))


@pytest.fixture
def sdk_config_path(request, config_dir):
    """返回sdk_config.yml文件路径"""
    sdk_config = request.config.getoption('--sdk-config') or request.config.getini('sdk_config')
    return sdk_config if sdk_config.startswith('/') else os.path.abspath(os.path.join(config_dir, sdk_config))


@pytest.fixture
def sdk_config_path2(config_dir):
    """返回sdk_config.yml文件路径"""
    return os.path.abspath(os.path.join(config_dir, './sdk_config2.yml'))


@pytest.fixture()
def crypto_config_path(config_dir):
    """crypto-config配置路径"""
    return os.path.join(config_dir, 'crypto-config')


@pytest.fixture()
def testdata_dir():
    return os.path.join(TESTS_DIR, 'resources')


def load_users(users_conf_file: str) -> Union[dict, list]:
    """
    从用户配置文件中加载用户对象列表
    :param users_conf_file: 用户配置文件
    eg: user.yml内容
    admin1:
      org_id: "wx-org1.chainmaker.org"
      user_key_file_path: "crypto-config/wx-org1.chainmaker.org/user/admin1/admin1.tls.key"
      user_crt_file_path: "crypto-config/wx-org1.chainmaker.org/user/admin1/admin1.tls.crt"
      user_sign_key_file_path: "crypto-config/wx-org1.chainmaker.org/user/admin1/admin1.sign.key"
      user_sign_crt_file_path: "crypto-config/wx-org1.chainmaker.org/user/admin1/admin1.sign.crt"
    ...
    或
    - org_id: "wx-org1.chainmaker.org"
      user_key_file_path: "crypto-config/wx-org1.chainmaker.org/user/admin1/admin1.tls.key"
      user_crt_file_path: "crypto-config/wx-org1.chainmaker.org/user/admin1/admin1.tls.crt"
      user_sign_key_file_path: "crypto-config/wx-org1.chainmaker.org/user/admin1/admin1.sign.key"
      user_sign_crt_file_path: "crypto-config/wx-org1.chainmaker.org/user/admin1/admin1.sign.crt"
    ...
    :return: 用户对象字典或用户对象列表
    """
    data = file_utils.load_yaml(users_conf_file)
    if isinstance(data, dict):
        return {key: User.from_conf(**data[key]) for key in data}
    return [User.from_conf(**item) for item in data]


@pytest.fixture
def users(config_dir):
    """根据config/users.yml生成用户对象列表"""
    users_config = os.path.join(config_dir, 'users.yml')
    with file_utils.switch_dir(config_dir):
        return load_users(users_config)


# @pytest.fixture()
# def cc(sdk_config_path, create_endorsers):
#     """长安链客户端, 增加发送带背书带请求方法 send_manage_request"""
#     # os.chdir(os.path.dirname(sdk_config_path))
#
#     with file_utils.switch_dir(os.path.dirname(sdk_config_path)):
#         cc = ChainClient.from_conf(sdk_config_path)
#
#         # 发送带背书请求
#         cc.send_manage_request = lambda payload, with_sync_result=True: \
#             cc.send_request(payload, endorsers=create_endorsers(payload), with_sync_result=with_sync_result)
#         yield cc
#         cc.stop()
@pytest.fixture()
def cc(crypto_config_path):
    cc = CryptoConfigUtils(crypto_config_path).create_default_chain_client()
    # return cc
    yield cc
    cc.stop()


@pytest.fixture()
def multi_sign_tx_id(cc, testdata_dir):
    byte_code_path = os.path.join(testdata_dir, 'byte_codes', 'rust-asset-2.0.0.wasm')
    code = file_utils.load_byte_code(byte_code_path)
    
    params = {'SYS_CONTRACT_NAME': 'CONTRACT_MANAGE',
              'SYS_METHOD': 'INIT_CONTRACT',
              'CONTRACT_NAME': create_contract_asset,
              'CONTRACT_VERSION': '1.0',
              'CONTRACT_BYTECODE': code,
              'CONTRACT_RUNTIME_TYPE': 'WASMER'
              }
    multi_sign_req_payload = cc.create_multi_sign_req_payload(params)
    res = cc.multi_sign_contract_req(multi_sign_req_payload, with_sync_result=True)
    return res.tx_id


@pytest.fixture
def cc2(sdk_config_path2, create_endorsers):  # chain_client via node1
    """节点2+用户2 长安链客户端"""
    os.chdir(os.path.dirname(sdk_config_path2))
    cc2 = ChainClient.from_conf(sdk_config_path2, node_index=1)
    # 发送带背书请求
    cc2.send_manage_request = lambda payload, with_sync_result=True: \
        cc.send_request(payload, endorsers=create_endorsers(payload), with_sync_result=with_sync_result)
    return cc2


@pytest.fixture
def node_client(request, sdk_config_path):
    """通过指定节点连接的长安链客户端 工厂"""
    
    def _node_client(node_index: int):
        os.chdir(request.config.rootdir)
        return ChainClient.from_conf(sdk_config_path, node_index=node_index)
    
    return _node_client


@pytest.fixture
def create_endorsers(users):
    """创建背书Fixture工厂"""
    
    def _create_endorsers(payload):
        """创建背书"""
        payload_bytes = payload.SerializeToString()
        endorsers = [user.endorse(payload_bytes) for user_name, user in users.items() if user_name.startswith('admin')]
        return endorsers
    
    return _create_endorsers


@pytest.fixture
def create_endorser(users):
    """创建背书Fixture工厂"""
    
    def _create_endorser(payload):
        """创建背书"""
        payload_bytes = payload.SerializeToString()
        endorser = [user.endorse(payload_bytes) for user_name, user in users.items() if user_name.startswith('admin')]
        return endorser
    
    return _create_endorser


@pytest.fixture()
def create_contract_counter_go(cc, testdata_dir):
    # contract_name = 'counter_go'
    contract_name = str(uuid.uuid4()).replace('-', '')
    params = {}
    byte_code_path = os.path.join(testdata_dir, 'byte_codes', 'rust-counter-2.0.0.wasm')
    payload = cc.create_contract_create_payload(contract_name, '1.0', byte_code_path, 'WASMER', params)
    # 携带背书发送请求
    res = cc.send_manage_request(payload)
    message = res.contract_result.message
    if 'contract exist' in message:
        print(f'合约{contract_name}已安装')
    else:
        assert res.code == 0, res.contract_result.message
        print(f'合约{contract_name}安装成功')
    return contract_name


@pytest.fixture()
def create_contract_name():
    return str(uuid.uuid4()).replace('-', '')


@pytest.fixture()
def create_contract_fact(cc, testdata_dir):
    chainconfig = cc.get_chain_config()
    if chainconfig.account_config.enable_gas is True:
        pytest.skip('不支持启用gas')
    
    params = {}
    # contract_name = str(uuid.uuid4()).replace('-', '')
    contract_name = 'fact'
    byte_code_path = os.path.join(testdata_dir, 'byte_codes', 'rust-fact-2.0.0.wasm')
    payload = cc.create_contract_create_payload(contract_name, '1.0', byte_code_path, 'WASMER', params)
    # 携带背书发送请求
    
    res = cc.send_manage_request(payload)
    message = res.contract_result.message
    if 'contract exist' in message:
        print(f'合约{contract_name}已安装')
    else:
        assert res.code == 0, res.contract_result.message
        print(f'合约{contract_name}安装成功')
    return contract_name


@pytest.fixture()
def create_frozen_contract(cc, testdata_dir):
    chainconfig = cc.get_chain_config()
    if chainconfig.account_config.enable_gas is True:
        pytest.skip('不支持启用gas')
    params = {}
    contract_name = str(uuid.uuid4()).replace('-', '')
    print('随机合约名称', contract_name)
    byte_code_path = os.path.join(testdata_dir, 'byte_codes', 'rust-fact-2.0.0.wasm')
    payload = cc.create_contract_create_payload(contract_name, '1.0', byte_code_path, 'WASMER', params)
    # 携带背书发送请求
    res = cc.send_manage_request(payload)
    message = res.contract_result.message
    if 'contract exist' in message:
        print(f'合约{contract_name}已安装')
    else:
        assert res.code == 0, res.contract_result.message
        print(f'合约{contract_name}安装成功')
    
    payload = cc.create_contract_freeze_payload(contract_name)
    res = cc.send_manage_request(payload)
    print('冻结合约响应', res)
    return contract_name


@pytest.fixture()
def send_tx(cc, create_contract_fact):
    """发送N笔交易"""
    
    def invoke_fact_save(count=1, with_sync_result=True):
        contract_name = 'fact'
        method = 'save'
        params = {"file_name": "name007", "file_hash": "ab3456df5799b87c77e7f88", "time": "6543234"}
        results = []
        for i in range(count):
            res = cc.invoke_contract(contract_name, method, params, with_sync_result=with_sync_result)
            results.append(res)
        return results
    
    return invoke_fact_save


@pytest.fixture()
def create_contract_asset(cc, testdata_dir, random_contract_name):
    chainconfig = cc.get_chain_config()
    if chainconfig.account_config.enable_gas is True:
        pytest.skip('不支持启用gas')
    contract_name = random_contract_name
    # contract_name = 'asset'
    params = {"issue_limit": "100000000", "total_supply": "100000000"}
    byte_code_path = os.path.join(testdata_dir, 'byte_codes', 'rust-asset-2.0.0.wasm')
    payload = cc.create_contract_create_payload(contract_name, '1.0', byte_code_path, 'WASMER', params)
    # 携带背书发送请求
    res = cc.send_manage_request(payload)
    message = res.contract_result.message
    if 'contract exist' in message:
        print(f'合约{contract_name}已安装')
    else:
        assert res.code == 0, res.contract_result.message
        print(f'合约{contract_name}安装成功')
    return contract_name


@pytest.fixture()
def create_contract_balance001(cc, testdata_dir):
    chainconfig = cc.get_chain_config()
    if chainconfig.account_config.enable_gas is True:
        pytest.skip('不支持启用gas')
    contract_name = calc_evm_contract_name('balance001')
    byte_code_path = os.path.join(testdata_dir, 'byte_codes', 'ledger_balance.bin')
    payload = cc.create_contract_create_payload(contract_name, '1.0', byte_code_path, 'EVM', None)
    print(payload)
    res = cc.send_manage_request(payload)
    message = res.contract_result.message
    if 'contract exist' in message:
        print('合约balance001已安装')
    else:
        assert res.code == 0, res.contract_result.message
        print('合约balance001安装成功')


@pytest.fixture()
def create_counter_evm(cc, testdata_dir):
    origin_contract_name = str(uuid.uuid4()).replace('-', '')
    contract_name = calc_evm_contract_name(origin_contract_name)
    byte_code_path = os.path.join(testdata_dir, 'byte_codes', 'counter_evm.wasm')
    payload = cc.create_contract_create_payload(contract_name, '1.0', byte_code_path, 'EVM', None)
    res = cc.send_manage_request(payload)
    message = res.contract_result.message
    if 'contract exist' in message:
        print(f'合约{contract_name}已安装')
    else:
        assert res.code == 0, res.contract_result.message
        print(f'合约{contract_name}安装成功')
    return contract_name


@pytest.fixture()
def last_block_tx_id(cc: ChainClient, create_contract_fact):
    """获取最新区块的交易id"""
    res = cc.get_last_block()
    tx_id = res.block.txs[0].payload.tx_id
    print(f'tx_id: {tx_id}')
    return tx_id


@pytest.fixture()
def last_block_hash(cc: ChainClient):
    """获取最新区块hash值"""
    res = cc.get_last_block()
    block_hash = res.block.header.block_hash.hex()  # 要转为hex
    print('block_hash:', block_hash)
    return block_hash


@pytest.fixture()
def random_contract_name():
    return common.gen_rand_contract_name()


@pytest.fixture()
def random_alias():
    return str(uuid.uuid4()).replace('-', '_')
