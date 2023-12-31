#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   evm_utils.py
# @Function     :   EVM合约名称、合约方法及合约参数转换

from eth_abi import encode_abi  # pip install eth-abi
from sha3 import keccak_256  # pip install pysha3


def keccak_256_encrypt(data: str) -> str:
    """keccak 256加密"""
    hex = keccak_256()
    hex.update(data.encode('utf-8'))
    return hex.hexdigest()


def calc_evm_contract_name(contract_name: str) -> str:
    """
    转换EVM合约名称
    :param contract_name: 原始合约名称
    :return: 转换后的合约名称
    """
    return keccak_256_encrypt(contract_name)[24:]


def calc_evm_method_params(method: str, params: list) -> tuple:
    """
    转换EVM合约方法及参数
    :param method: 合约方法
    :param params: 参数列表 eg. [{"uint256": "10000"}, {"address": "0xa166c92f4c8118905ad984919dc683a7bdb295c1"}]
    :return: 转换后的方法及参数
    """
    input_types, input_values = [], []
    for item in params:
        for key, value in item.items():
            input_types.append(key)
            input_values.append(int(value) if 'int' in key else value)
    
    sig = '%s(%s)' % (method, ','.join(input_types))
    method_id = keccak_256_encrypt(sig)[:8]
    data = method_id + encode_abi(tuple(input_types), tuple(input_values)).hex()
    return method_id, dict(data=data)
