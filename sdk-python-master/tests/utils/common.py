#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   common.py
# @Function     :   常用方法
import random
import os

from chainmaker.chain_client import ChainClient


TESTS_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.dirname(TESTS_DIR)

def get_last_block_tx_id(cc: ChainClient):
    """获取最新区块的交易id"""
    block_info = cc.get_last_block()
    tx_id = block_info.block.txs[0].payload.multi_sign_tx_id
    print(f'tx_id: {tx_id}')
    return tx_id


def get_last_block_hash(cc: ChainClient):
    """获取最新区块hash值"""
    block_info = cc.get_last_block()
    block_hash = block_info.block.header.block_hash.hex()  # 要转为hex
    print('block_hash:', block_hash)
    return block_hash


def get_last_block_height(cc: ChainClient):
    return cc.get_current_block_height()


def get_random_block_height(cc: ChainClient):
    current_height = cc.get_current_block_height()
    random_block_height = random.choice(list(range(0, current_height + 1)))
    print(f'block_height: {random_block_height}')
    return random_block_height


def get_random_block(cc: ChainClient):
    random_block_height = get_random_block_height(cc)
    block_info = cc.get_block_by_height(random_block_height)
    return block_info


def get_valid_tx_id(cc: ChainClient):
    block_info = get_random_block(cc)
    tx_id = block_info.block.txs[0].payload.multi_sign_tx_id
    print(f'tx_id: {tx_id}')
    return tx_id


def get_valid_block_hash(cc: ChainClient):
    block_info = get_random_block(cc)
    block_hash = block_info.block.header.block_hash.hex()
    print('block_hash:', block_hash)
    return block_hash
