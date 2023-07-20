# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chainmaker/protos/api/rpc_node.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from chainmaker.protos.common import request_pb2 as chainmaker_dot_protos_dot_common_dot_request__pb2
from chainmaker.protos.common import result_pb2 as chainmaker_dot_protos_dot_common_dot_result__pb2
from chainmaker.protos.config import local_config_pb2 as chainmaker_dot_protos_dot_config_dot_local__config__pb2
from chainmaker.protos.config import log_config_pb2 as chainmaker_dot_protos_dot_config_dot_log__config__pb2
from chainmaker.protos.config import \
    chainmaker_server_pb2 as chainmaker_dot_protos_dot_config_dot_chainmaker__server__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='chainmaker/protos/api/rpc_node.proto',
    package='api',
    syntax='proto3',
    serialized_options=b'\n\025org.chainmaker.pb.apiZ&chainmaker.org/chainmaker/pb-go/v2/api',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n$chainmaker/protos/api/rpc_node.proto\x12\x03\x61pi\x1a&chainmaker/protos/common/request.proto\x1a%chainmaker/protos/common/result.proto\x1a+chainmaker/protos/config/local_config.proto\x1a)chainmaker/protos/config/log_config.proto\x1a\x30\x63hainmaker/protos/config/chainmaker_server.proto2\xef\x03\n\x07RpcNode\x12\x36\n\x0bSendRequest\x12\x11.common.TxRequest\x1a\x12.common.TxResponse\"\x00\x12;\n\tSubscribe\x12\x11.common.TxRequest\x1a\x17.common.SubscribeResult\"\x00\x30\x01\x12N\n\x11UpdateDebugConfig\x12\x1a.config.DebugConfigRequest\x1a\x1b.config.DebugConfigResponse\"\x00\x12O\n\x16RefreshLogLevelsConfig\x12\x18.config.LogLevelsRequest\x1a\x19.config.LogLevelsResponse\"\x00\x12]\n\x14GetChainMakerVersion\x12 .config.ChainMakerVersionRequest\x1a!.config.ChainMakerVersionResponse\"\x00\x12o\n\x18\x43heckNewBlockChainConfig\x12\'.config.CheckNewBlockChainConfigRequest\x1a(.config.CheckNewBlockChainConfigResponse\"\x00\x42?\n\x15org.chainmaker.pb.apiZ&chainmaker.org/chainmaker/pb-go/v2/apib\x06proto3'
    ,
    dependencies=[chainmaker_dot_protos_dot_common_dot_request__pb2.DESCRIPTOR,
                  chainmaker_dot_protos_dot_common_dot_result__pb2.DESCRIPTOR,
                  chainmaker_dot_protos_dot_config_dot_local__config__pb2.DESCRIPTOR,
                  chainmaker_dot_protos_dot_config_dot_log__config__pb2.DESCRIPTOR,
                  chainmaker_dot_protos_dot_config_dot_chainmaker__server__pb2.DESCRIPTOR, ])

_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DESCRIPTOR._options = None

_RPCNODE = _descriptor.ServiceDescriptor(
    name='RpcNode',
    full_name='api.RpcNode',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=263,
    serialized_end=758,
    methods=[
        _descriptor.MethodDescriptor(
            name='SendRequest',
            full_name='api.RpcNode.SendRequest',
            index=0,
            containing_service=None,
            input_type=chainmaker_dot_protos_dot_common_dot_request__pb2._TXREQUEST,
            output_type=chainmaker_dot_protos_dot_common_dot_result__pb2._TXRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='Subscribe',
            full_name='api.RpcNode.Subscribe',
            index=1,
            containing_service=None,
            input_type=chainmaker_dot_protos_dot_common_dot_request__pb2._TXREQUEST,
            output_type=chainmaker_dot_protos_dot_common_dot_result__pb2._SUBSCRIBERESULT,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='UpdateDebugConfig',
            full_name='api.RpcNode.UpdateDebugConfig',
            index=2,
            containing_service=None,
            input_type=chainmaker_dot_protos_dot_config_dot_local__config__pb2._DEBUGCONFIGREQUEST,
            output_type=chainmaker_dot_protos_dot_config_dot_local__config__pb2._DEBUGCONFIGRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='RefreshLogLevelsConfig',
            full_name='api.RpcNode.RefreshLogLevelsConfig',
            index=3,
            containing_service=None,
            input_type=chainmaker_dot_protos_dot_config_dot_log__config__pb2._LOGLEVELSREQUEST,
            output_type=chainmaker_dot_protos_dot_config_dot_log__config__pb2._LOGLEVELSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='GetChainMakerVersion',
            full_name='api.RpcNode.GetChainMakerVersion',
            index=4,
            containing_service=None,
            input_type=chainmaker_dot_protos_dot_config_dot_chainmaker__server__pb2._CHAINMAKERVERSIONREQUEST,
            output_type=chainmaker_dot_protos_dot_config_dot_chainmaker__server__pb2._CHAINMAKERVERSIONRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='CheckNewBlockChainConfig',
            full_name='api.RpcNode.CheckNewBlockChainConfig',
            index=5,
            containing_service=None,
            input_type=chainmaker_dot_protos_dot_config_dot_local__config__pb2._CHECKNEWBLOCKCHAINCONFIGREQUEST,
            output_type=chainmaker_dot_protos_dot_config_dot_local__config__pb2._CHECKNEWBLOCKCHAINCONFIGRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_RPCNODE)

DESCRIPTOR.services_by_name['RpcNode'] = _RPCNODE

# @@protoc_insertion_point(module_scope)