# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syscontract/cert_manage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsyscontract/cert_manage.proto\x12\x0bsyscontract*\xd7\x01\n\x12\x43\x65rtManageFunction\x12\x0c\n\x08\x43\x45RT_ADD\x10\x00\x12\x10\n\x0c\x43\x45RTS_DELETE\x10\x01\x12\x0f\n\x0b\x43\x45RTS_QUERY\x10\x02\x12\x10\n\x0c\x43\x45RTS_FREEZE\x10\x03\x12\x12\n\x0e\x43\x45RTS_UNFREEZE\x10\x04\x12\x10\n\x0c\x43\x45RTS_REVOKE\x10\x05\x12\x12\n\x0e\x43\x45RT_ALIAS_ADD\x10\x06\x12\x15\n\x11\x43\x45RT_ALIAS_UPDATE\x10\x07\x12\x16\n\x12\x43\x45RTS_ALIAS_DELETE\x10\x08\x12\x15\n\x11\x43\x45RTS_ALIAS_QUERY\x10\tBO\n\x1dorg.chainmaker.pb.syscontractZ.chainmaker.org/chainmaker/pb-go/v2/syscontractb\x06proto3')

_CERTMANAGEFUNCTION = DESCRIPTOR.enum_types_by_name['CertManageFunction']
CertManageFunction = enum_type_wrapper.EnumTypeWrapper(_CERTMANAGEFUNCTION)
CERT_ADD = 0
CERTS_DELETE = 1
CERTS_QUERY = 2
CERTS_FREEZE = 3
CERTS_UNFREEZE = 4
CERTS_REVOKE = 5
CERT_ALIAS_ADD = 6
CERT_ALIAS_UPDATE = 7
CERTS_ALIAS_DELETE = 8
CERTS_ALIAS_QUERY = 9


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035org.chainmaker.pb.syscontractZ.chainmaker.org/chainmaker/pb-go/v2/syscontract'
  _CERTMANAGEFUNCTION._serialized_start=47
  _CERTMANAGEFUNCTION._serialized_end=262
# @@protoc_insertion_point(module_scope)
