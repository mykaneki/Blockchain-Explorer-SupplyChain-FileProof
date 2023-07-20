#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   crypto_config_utils.py
# @Function     :   crypto_config实用方法，获取对应的授权模式，获取节点nodeid, 获取用户对象、创建背书等
import os
from pathlib import Path
# from functools import cached_property  # python3.6没有

from chainmaker.keys import AuthType
from chainmaker.user import User
from chainmaker.chain_client import ChainClient
from tests.utils.common import TESTS_DIR

CRYPTO_CONFIG_PATH = os.path.join(TESTS_DIR, 'resources', 'crypto-config')
ARCHIVE_CONFIG = {'dest': 'root:passw0rd:localhost:3306', 'secret_key': 'passw0rd', 'type': 'mysql'}


class CryptoConfigUtils:
    def __init__(self, crypto_config_path: str):
        assert os.path.isdir(crypto_config_path), f'目录不存在：{crypto_config_path}'
        self.path = Path(crypto_config_path)
        self._auth_type = None
    
    @property
    def auth_type(self):
        if self._auth_type is None:
            if 'node1' in os.listdir(self.path):
                self._auth_type = AuthType.Public
            org1_dir = os.path.join(self.path, 'wx-org1.chainmaker.org')
            if 'admin' in os.listdir(org1_dir):
                self._auth_type = AuthType.PermissionedWithKey
            self._auth_type = AuthType.PermissionedWithCert
        return self._auth_type
    
    @property
    def users(self):
        users = []
        if self.auth_type == AuthType.PermissionedWithCert:
            for org_dir in self.path.iterdir():
                org_id = org_dir.name
                org_short_id = org_id.lstrip('wx-').rstrip('.chainmaker.org')
                for user_dir in (org_dir / 'user').iterdir():
                    user_name = user_dir.name
                    user_id = "%s_%s" % (org_short_id, user_dir.name)
                    user_role = user_name.strip('1')
                    user = User.from_conf(org_id,
                                          user_sign_key_file_path=str(user_dir / f'{user_name}.sign.key'),
                                          user_sign_crt_file_path=str(user_dir / f'{user_name}.sign.crt')
                                          )
                    user.user_id = user_id
                    user.name = user_name
                    user.role = user_role
                    users.append(user)
        return users
    
    def get_public_node_id(self, node: str):
        """
        获取公钥模式node节点的nodeid
        :param node: node名称, eg: node1
        :return: nodeid内容（节点地址）
        """
        assert self.auth_type == AuthType.Public, '仅支持Public模式'
        node_id_file = self.path / node / f'{node}.nodeid'
        with open(node_id_file) as f:
            return f.read().strip()
        
    def get_node_id(self, node='consensus1', org_id=None)->str:
        """
        获取非用药模式指定节点nodeid
        :param node: 节点名称
            eg. 公钥模式 node1
                非公钥模式 consensus1, common1
        :return:
        """
        if self.auth_type == AuthType.Public:
            node_id_file = self.path / node / f'{node}.nodeid'
        else:
            node_id_file = self.path / org_id / 'node' / node / f'{node}.nodeid'
        with open(node_id_file) as f:
            return f.read().strip()

    def get_org_crt(self, org_id: str)->str:
        """获取组织证书内容"""
        assert self.auth_type != AuthType.Public, '获取组织ca证书不支持Public模式'
        org_crt_path = self.path / org_id / 'ca' / 'ca.crt'
        with open(org_crt_path) as f:
            return f.read()
    
    def get_user(self, user_dir: str, org_id: str=None)->User:
        """
        从cropto-config中用户相对路径获取用户对象
        :param relative_user_path:
        :return:
        """
        user_path = os.path.abspath(os.path.join(self.path, user_dir))
        if self.get_auth_type() == AuthType.PermissionedWithCert:
            assert isinstance(org_id, str)
            user_sign_key_file_path = f"./crypto-config/{org_id}/user/admin1/admin1.sign.key",
            user_sign_crt_file_path = f"./crypto-config/{org_id}/user/admin1/admin1.sign.crt",
        
    def create_default_sdk_config(self, chain_id='chain1', host='127.0.0.1', start_port=12301)->dict:
        """
        使用标准crypto-config目录创建一个标准的sdk_config配置
        :param chain_id: 链ID
        :param host: 链服务地址
        :param start_port: rpc起始端口号
        :return: 返回sdk_config字典，同yaml.safe_load(open('sdk_config.yml'))
        """
        crypto_config_path = self.path

        orgs = [org_id for org_id in os.listdir(crypto_config_path) if org_id.startswith('wx')]
        orgs.sort()

        if self.auth_type == AuthType.Public:
            nodes = [org_id for org_id in os.listdir(crypto_config_path) if org_id.startswith('node')][:4]

            chain_client = {
                'chain_id': chain_id,
                'user_sign_key_file_path': f"{self.path}/node1/admin/admin1/admin1.key",
                'crypto': {'hash': 'SHA256'},
                'auth_type': 'public',
                'nodes': [{
                    'node_addr': '%s:%d' % (host, start_port + index),
                    'conn_cnt': 1,
                } for index, node in enumerate(nodes)],
                'archive': ARCHIVE_CONFIG
            }
        elif self.auth_type == AuthType.PermissionedWithKey:
            chain_client = {
                'chain_id': chain_id,
                'org_id': "wx-org1.chainmaker.org",
                'user_sign_key_file_path': f"{self.path}/wx-org1.chainmaker.org/admin/admin.key",
                'crypto': {'hash': 'SHA256'},
                'auth_type': 'permissionedWithKey',
                'nodes': [{
                    'node_addr': '%s:%d' % (host, start_port + index),
                    'conn_cnt': 1
                } for index, org_id in enumerate(orgs)],
                'archive': ARCHIVE_CONFIG
            }

        else:
            chain_client = {'chain_id': chain_id, 'org_id': 'wx-org1.chainmaker.org',
                            'user_crt_file_path': f'{self.path}/wx-org1.chainmaker.org/user/client1/client1.tls.crt',
                            'user_key_file_path': f'{self.path}/wx-org1.chainmaker.org/user/client1/client1.tls.key',
                            'user_sign_crt_file_path': f'{self.path}/wx-org1.chainmaker.org/user/client1/client1.sign.crt',
                            'user_sign_key_file_path': f'{self.path}/wx-org1.chainmaker.org/user/client1/client1.sign.key',
                            'nodes': [
                                {'enable_tls': True,
                                 'node_addr': '%s:%d' % (host, start_port + index),
                                 'conn_cnt': 1,
                                 'tls_host_name': 'chainmaker.org',
                                 'trust_root_paths': ['%s/%s/ca' % (crypto_config_path, org_id)]}
                                for index, org_id in enumerate(orgs)],
                            'archive': ARCHIVE_CONFIG
                            }

        sdk_config = {'chain_client': chain_client}
        return sdk_config
    
    def create_default_endorse_users(self, endorsers_cnt=4) -> list:
        """
        当config.yml中未配置背书时，创建默认背书用户
        :param auth_type: 授权类型 cert 证书模式 / pk public模式 /  pwk Key模式
        """
        # 创建公钥模式默认背书
        dirs = [dir_name for dir_name in sorted(os.listdir(self.path)) if dir_name.startswith('wx') or dir_name.startswith('node')]
        assert endorsers_cnt <= len(dirs), f'背书数量{endorsers_cnt}应少于crypto-config中目录数'
        if self.auth_type == AuthType.Public:
            users_conf = [
                {'user_sign_key_file_path': f"{self.path}/{node}/admin/admin{index+1}/admin{index+1}.key", 'auth_type': 'public'}
                for index, node in enumerate(dirs[:endorsers_cnt + 1])
            ]
        # 创建Key模式默认背书
        elif self.auth_type == AuthType.PermissionedWithKey:
            users_conf = [{
                    'org_id': org_id,
                    'user_sign_key_file_path': f"{self.path}/{org_id}/admin/admin.key",
                    'auth_type': 'permissionedWithKey'
                } for org_id in dirs[:endorsers_cnt + 1]
            ]
        # 创建证书模式默认背书
        else:
            users_conf = [
                {
                    'org_id': org_id,
                    'user_sign_key_file_path': f"{self.path}/{org_id}/user/admin1/admin1.sign.key",
                    'user_sign_crt_file_path': f"{self.path}/{org_id}/user/admin1/admin1.sign.crt",
                }  for org_id in dirs[:endorsers_cnt + 1]
            ]
        return [User.from_conf(**item) for item in users_conf]

    def create_default_chain_client(self, chain_id='chain1', host='127.0.0.1', start_port=12301, endorsers_cnt=4):
        """
        创建带默认背书用户的链客户端
        :param chain_id:
        :param host:
        :param start_port:
        :param endorsers_cnt:
        :return:
        """
        sdk_config = self.create_default_sdk_config(chain_id, host, start_port)
        endorse_users = self.create_default_endorse_users(endorsers_cnt)
        cc = ChainClient.from_conf(sdk_config)
        cc.endorse_users = endorse_users
        return cc


CURRENT_AUTH_TYPE = CryptoConfigUtils(CRYPTO_CONFIG_PATH).auth_type


if __name__ == '__main__':
    print(CryptoConfigUtils(CRYPTO_CONFIG_PATH).users)
