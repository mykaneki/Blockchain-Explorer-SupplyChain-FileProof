# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syscontract/pubkey_manage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsyscontract/pubkey_manage.proto\x12\x0bsyscontract*K\n\x14PubkeyManageFunction\x12\x0e\n\nPUBKEY_ADD\x10\x00\x12\x11\n\rPUBKEY_DELETE\x10\x01\x12\x10\n\x0cPUBKEY_QUERY\x10\x02\x42O\n\x1dorg.chainmaker.pb.syscontractZ.chainmaker.org/chainmaker/pb-go/v2/syscontractb\x06proto3')

_PUBKEYMANAGEFUNCTION = DESCRIPTOR.enum_types_by_name['PubkeyManageFunction']
PubkeyManageFunction = enum_type_wrapper.EnumTypeWrapper(_PUBKEYMANAGEFUNCTION)
PUBKEY_ADD = 0
PUBKEY_DELETE = 1
PUBKEY_QUERY = 2


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035org.chainmaker.pb.syscontractZ.chainmaker.org/chainmaker/pb-go/v2/syscontract'
  _PUBKEYMANAGEFUNCTION._serialized_start=48
  _PUBKEYMANAGEFUNCTION._serialized_end=123
# @@protoc_insertion_point(module_scope)