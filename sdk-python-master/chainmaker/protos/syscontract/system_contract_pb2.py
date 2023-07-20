# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syscontract/system_contract.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!syscontract/system_contract.proto\x12\x0bsyscontract*\x9e\x02\n\x0eSystemContract\x12\x10\n\x0c\x43HAIN_CONFIG\x10\x00\x12\x0f\n\x0b\x43HAIN_QUERY\x10\x01\x12\x0f\n\x0b\x43\x45RT_MANAGE\x10\x02\x12\x0e\n\nGOVERNANCE\x10\x03\x12\x0e\n\nMULTI_SIGN\x10\x04\x12\x13\n\x0f\x43ONTRACT_MANAGE\x10\x05\x12\x13\n\x0fPRIVATE_COMPUTE\x10\x06\x12\x0e\n\nDPOS_ERC20\x10\x07\x12\x0e\n\nDPOS_STAKE\x10\x08\x12\x14\n\x10SUBSCRIBE_MANAGE\x10\t\x12\x12\n\x0e\x41RCHIVE_MANAGE\x10\n\x12\x15\n\x11\x43ROSS_TRANSACTION\x10\x0b\x12\x11\n\rPUBKEY_MANAGE\x10\x0c\x12\x13\n\x0f\x41\x43\x43OUNT_MANAGER\x10\r\x12\x05\n\x01T\x10\x63\x42O\n\x1dorg.chainmaker.pb.syscontractZ.chainmaker.org/chainmaker/pb-go/v2/syscontractb\x06proto3')

_SYSTEMCONTRACT = DESCRIPTOR.enum_types_by_name['SystemContract']
SystemContract = enum_type_wrapper.EnumTypeWrapper(_SYSTEMCONTRACT)
CHAIN_CONFIG = 0
CHAIN_QUERY = 1
CERT_MANAGE = 2
GOVERNANCE = 3
MULTI_SIGN = 4
CONTRACT_MANAGE = 5
PRIVATE_COMPUTE = 6
DPOS_ERC20 = 7
DPOS_STAKE = 8
SUBSCRIBE_MANAGE = 9
ARCHIVE_MANAGE = 10
CROSS_TRANSACTION = 11
PUBKEY_MANAGE = 12
ACCOUNT_MANAGER = 13
T = 99


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035org.chainmaker.pb.syscontractZ.chainmaker.org/chainmaker/pb-go/v2/syscontract'
  _SYSTEMCONTRACT._serialized_start=51
  _SYSTEMCONTRACT._serialized_end=337
# @@protoc_insertion_point(module_scope)