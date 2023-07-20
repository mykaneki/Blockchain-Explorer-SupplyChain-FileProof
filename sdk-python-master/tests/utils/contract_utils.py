#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   contract_utils.py
# @Function     :   常用合约操作封装
from chainmaker.keys import RuntimeType
from chainmaker.utils.result_utils import check_response


class BaseContract:
    runtime_type = RuntimeType.WASMER
    create_params: dict = {}
    
    def __init__(self, cc, contract_name, byte_code_path):
        self.cc = cc
        self.contract_name = contract_name
        self.byte_code_path = byte_code_path
        
    def __str__(self):
        return self.contract_name
        
    def get_contract_info(self):
        return self.cc.get_contract_info(self.contract_name)
        
    def create(self):
        payload = self.cc.create_contract_create_payload(self.contract_name, '1.0', self.byte_code_path,
                                                         self.runtime_type, self.create_params)
        res = self.cc.send_manage_request(payload)
        check_response(res)
        return res
    
    def upgrade(self, upgrade_byte_code_path, version='2.0'):
        payload = self.cc.create_contract_upgrade_payload(self.contract_name, version, upgrade_byte_code_path,
                                                          self.runtime_type, self.create_params)
        res = self.cc.send_manage_request(payload)
        check_response(res)
        return res
    
    def freeze(self):
        payload = self.cc.create_contract_freeze_payload(self.contract_name)
        res = self.cc.send_manage_request(payload)
        check_response(res)
        return res
    
    def unfreeze(self):
        payload = self.cc.create_contract_unfreeze_payload(self.contract_name)
        res = self.cc.send_manage_request(payload)
        check_response(res)
        return res
    
    def revoke(self):
        payload = self.cc.create_contract_revoke_payload(self.contract_name)
        res = self.cc.send_manage_request(payload)
        check_response(res)
        return res
    
    def query(self, method, params=None):
        return self.cc.query_contract(self.contract_name, method, params)
    
    def invoke(self, method, params=None):
        return self.cc.invoke_contract(self.contract_name, method, params, with_sync_result=True)

    def run_life_cycle(self, invoke_method, invoke_params=None, query_method=None, query_parmas=None,
                       upgrade_byte_code_path=None):
        """合约生命周期"""
        if query_method is None:
            query_method = invoke_method
            query_parmas = invoke_params
            
        upgrade_byte_code_path = upgrade_byte_code_path or self.byte_code_path
        self.create()
        self.invoke(invoke_method, invoke_params)
        self.upgrade(upgrade_byte_code_path)
        self.query(query_method, query_parmas)
        self.freeze()
        self.unfreeze()
        self.invoke(invoke_method, invoke_params)
        self.revoke()

class CounterEvm(BaseContract):
    """counter_evm.wasm"""
    runtime_type = RuntimeType.EVM
    
    def calc_json(self, func_name: str, data1: int, data2: int, data3: int, data4: int):
        """查询结果"""
        params = [{'string': func_name}, {'uint256': data1}, {'uint256': data2}, {'uint256': data3}, {'uint256': data4}]
        return self.invoke('calc_json', params)
    
    def calc_result(self):
        """增加计数"""
        params = []
        return self.query('updateBalance', params)
    
    def call_num(self):
        params = []
        return self.query('updateMyBalance', params)


class LedgerBalance(BaseContract):
    """ledger_balance.bin"""
    runtime_type = RuntimeType.EVM
    
    def balances(self, address: str):
        """查询结果"""
        params = [{'address': address}]
        return self.invoke('balances', params)
    
    def updateBalance(self, amount: int, address: str):
        """增加计数"""
        params = [{'uint256': amount}, {'address': address}]
        return self.invoke('updateBalance', params)
    
    def updateMyBalance(self, amount: int):
        params = [{'uint256': amount}]
        return self.invoke('updateMyBalance', params)
    
    def transfer(self, address: str, amount: int):
        """转帐"""
        params = [{'address': address}, {'uint256': amount}]
        return self.invoke('transfer', params)


class RustAsset(BaseContract):
    """rust-asset-2.0.0.wasm"""
    create_params = {"issue_limit": "100000000","total_supply": "100000000"}
    
    def register(self) -> bytes:
        """注册当前用户并返回账户地址"""
        res = self.invoke('register')
        addr = res.contract_result.result
        return addr
    
    def query_address(self) -> bytes:
        res = self.query('query_address')
        addr = res.contract_result.result
        return addr
    
    def query_other_address(self, pub_key: str):
        params = {
            'pub_key': pub_key
        }
        res = self.query('query_other_address', params)
        addr = res.contract_result.result
        return addr
    
    def issue_amount(self, to: str, amount: str) -> None:
        """为指定账户发放额度"""
        params = {
            "to": to,
            "amount": str(amount)
        }
        res = self.invoke("issue_amount", params)
        assert 0 == res.contract_result.code, res.contract_result
    
    def approve(self, spender: str, amount: str) -> None:
        """授权花钱的人一定数额"""
        params = {
            "spender": spender,
            "amount": str(amount)
        }
        res = self.invoke('approve', params)
        assert 0 == res.contract_result.code, res.contract_result
    
    def transfer(self, to: str, amount: str):
        """转帐到指定账户"""
        params = {
            "to": to,
            "amount": str(amount)
        }
        res = self.invoke("transfer", params)
        assert b"ok" == res.contract_result.result
    
    def transfer_from(self, _from: str, to: str, amount: str):
        """代转账"""
        params = {
            "from": _from,
            "to": to,
            "amount": str(amount)
        }
        res = self.invoke('transfer_from', params)
        assert b"ok" == res.contract_result.result
    
    def balance_of(self, addr):  # todo check
        """获取指定账户余额"""
        params = {
            "owner": addr,
        }
        res = self.query("balance_of", params)
        balance = int(res.contract_result.result)
        return balance
    
    @property
    def total_supply(self):
        """当前合约总金额"""
        res = self.query("total_supply")
        amount = int(res.contract_result.result)
        return amount
    
    @property
    def issued_amount(self) -> int:
        """当前合约已发金额"""
        res = self.query("issued_amount")
        amount = int(res.contract_result.result)
        return amount
    
    @property
    def allowance(self) -> int:
        """获取授权限额"""
        res = self.query("allowance")
        amount = int(res.contract_result.result)
        return amount


class CounterRust(BaseContract):
    """counter_evm.wasm"""
    
    def calc_json(self, func_name, data1, data2, data3, data4):
        invoke_method = "calc_json"
        invoke_params = {"func_name": func_name, "data1": str(data1), "data2": str(data2), "data3": str(data3),
                         "data4": str(data4)}
        return self.invoke(invoke_method, invoke_params)
    
    def call_contract_self(self):
        invoke_method = "call_contract_self"
        invoke_params = {}
        return self.invoke(invoke_method, invoke_params)
    
    def call_memory(self, allocate_size: int):
        invoke_params = {"allocate_size": allocate_size}
        invoke_method = "call_memory"
        return self.invoke(invoke_method, invoke_params)
    
    
class RustCounter(BaseContract):
    """rust-counter-2.0.0.wasm"""

    def query_result(self):
        """查询结果"""
        return self.query('query')

    def increase(self):
        """增加计数"""
        return self.invoke('increase')


class RustFact(BaseContract):
    """rust-fact-2.0.0.wasm"""
    
    def save(self, file_hash: str, file_name: str, time: str):
        """查询结果"""
        params = {'file_hash': file_hash, 'file_name': file_name, 'time': time}
        return self.invoke('save', params)
    
    def find_by_file_hash(self, file_hash: str):
        """增加计数"""
        params = {'file_hash': file_hash}
        return self.invoke('find_by_file_hash', params)


class IteratorGo(BaseContract):
    """iterator-go-2.wasm"""
    runtime_type = RuntimeType.GASM
    
    def kv_iteartor_get(self, start_key: str, start_field: str, limit_key: str, limit_field: str, func_name: str):
        """
        
        :param start_key:
        :param start_field:
        :param limit_key:
        :param limit_field:
        :param func_name: NewIteratorWithField / NewIterator / NewIteratorPrefixWithKeyField / NewIteratorPrefixWithKey
        :return:
        """
        params ={"start_key": start_key,
                 "start_field": start_field,
                 "limit_key": limit_key,
                 "limit_field": limit_field,
                 "func_name": func_name}
        return self.invoke('kv_iteartor_get', params)
    
    
class ContractCalc(BaseContract):
    """contract_calc.7z"""
    runtime_type = RuntimeType.DOCKER_GO
    
    def invoke_contract(self, method: str, arg1: int, arg2: int):
        """
        调用合约invoke_contract方法
        :param method: add / sub / mul / div
        :param arg1:
        :param arg2:
        :return:
        """
        params = {"method": method, "arg1": str(arg1), "arg2": str(arg2)}
        return self.invoke('invoke_contract', params)
