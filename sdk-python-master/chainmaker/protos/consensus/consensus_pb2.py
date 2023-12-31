# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: consensus/consensus.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chainmaker.protos.common import block_pb2 as common_dot_block__pb2
from chainmaker.protos.common import rwset_pb2 as common_dot_rwset__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63onsensus/consensus.proto\x12\tconsensus\x1a\x12\x63ommon/block.proto\x1a\x12\x63ommon/rwset.proto\"\x8a\x02\n\x0cVerifyResult\x12%\n\x0everified_block\x18\x01 \x01(\x0b\x32\r.common.Block\x12*\n\x04\x63ode\x18\x02 \x01(\x0e\x32\x1c.consensus.VerifyResult.Code\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\x39\n\ntxs_rw_set\x18\x04 \x03(\x0b\x32%.consensus.VerifyResult.TxsRwSetEntry\x1a@\n\rTxsRwSetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.common.TxRWSet:\x02\x38\x01\"\x1d\n\x04\x43ode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\"\xab\x01\n\rProposalBlock\x12\x1c\n\x05\x62lock\x18\x01 \x01(\x0b\x32\r.common.Block\x12:\n\ntxs_rw_set\x18\x02 \x03(\x0b\x32&.consensus.ProposalBlock.TxsRwSetEntry\x1a@\n\rTxsRwSetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.common.TxRWSet:\x02\x38\x01\"y\n\x18\x42lockHeaderConsensusArgs\x12\x16\n\x0e\x63onsensus_type\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x03 \x01(\x04\x12\r\n\x05level\x18\x04 \x01(\x04\x12\'\n\x0e\x63onsensus_data\x18\x05 \x01(\x0b\x32\x0f.common.TxRWSet\"2\n\x10GovernanceMember\x12\x0f\n\x07node_id\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x03\"\x92\x05\n\x12GovernanceContract\x12\x10\n\x08\x65poch_id\x18\x01 \x01(\x04\x12&\n\x04type\x18\x02 \x01(\x0e\x32\x18.consensus.ConsensusType\x12\x15\n\rcur_max_index\x18\x03 \x01(\x03\x12\x1b\n\x13skip_timeout_commit\x18\x04 \x01(\x08\x12\x17\n\x0f\x63onfig_sequence\x18\x06 \x01(\x04\x12\t\n\x01n\x18\x07 \x01(\x04\x12\x19\n\x11min_quorum_for_qc\x18\x08 \x01(\x04\x12\x12\n\ncached_len\x18\t \x01(\x04\x12\x1a\n\x12next_switch_height\x18\n \x01(\x04\x12\x15\n\rtransit_block\x18\x0b \x01(\x04\x12\x1b\n\x13\x62lock_num_per_epoch\x18\x0c \x01(\x04\x12\x15\n\rvalidator_num\x18\r \x01(\x04\x12\x1a\n\x12node_propose_round\x18\x0e \x01(\x04\x12,\n\x07members\x18\x0f \x03(\x0b\x32\x1b.consensus.GovernanceMember\x12/\n\nvalidators\x18\x10 \x03(\x0b\x32\x1b.consensus.GovernanceMember\x12\x34\n\x0fnext_validators\x18\x11 \x03(\x0b\x32\x1b.consensus.GovernanceMember\x12\x1e\n\x16last_min_quorum_for_qc\x18\x12 \x01(\x04\x12!\n\x19maxbft_round_timeout_mill\x18\x13 \x01(\x04\x12*\n\"maxbft_round_timeout_interval_mill\x18\x14 \x01(\x04\x12\x34\n\x0flast_validators\x18\x15 \x03(\x0b\x32\x1b.consensus.GovernanceMember*V\n\rConsensusType\x12\x08\n\x04SOLO\x10\x00\x12\x08\n\x04TBFT\x10\x01\x12\x08\n\x04MBFT\x10\x02\x12\n\n\x06MAXBFT\x10\x03\x12\x08\n\x04RAFT\x10\x04\x12\x08\n\x04\x44POS\x10\x05\x12\x07\n\x03POW\x10\nBK\n\x1borg.chainmaker.pb.consensusZ,chainmaker.org/chainmaker/pb-go/v2/consensusb\x06proto3')

_CONSENSUSTYPE = DESCRIPTOR.enum_types_by_name['ConsensusType']
ConsensusType = enum_type_wrapper.EnumTypeWrapper(_CONSENSUSTYPE)
SOLO = 0
TBFT = 1
MBFT = 2
MAXBFT = 3
RAFT = 4
DPOS = 5
POW = 10


_VERIFYRESULT = DESCRIPTOR.message_types_by_name['VerifyResult']
_VERIFYRESULT_TXSRWSETENTRY = _VERIFYRESULT.nested_types_by_name['TxsRwSetEntry']
_PROPOSALBLOCK = DESCRIPTOR.message_types_by_name['ProposalBlock']
_PROPOSALBLOCK_TXSRWSETENTRY = _PROPOSALBLOCK.nested_types_by_name['TxsRwSetEntry']
_BLOCKHEADERCONSENSUSARGS = DESCRIPTOR.message_types_by_name['BlockHeaderConsensusArgs']
_GOVERNANCEMEMBER = DESCRIPTOR.message_types_by_name['GovernanceMember']
_GOVERNANCECONTRACT = DESCRIPTOR.message_types_by_name['GovernanceContract']
_VERIFYRESULT_CODE = _VERIFYRESULT.enum_types_by_name['Code']
VerifyResult = _reflection.GeneratedProtocolMessageType('VerifyResult', (_message.Message,), {

  'TxsRwSetEntry' : _reflection.GeneratedProtocolMessageType('TxsRwSetEntry', (_message.Message,), {
    'DESCRIPTOR' : _VERIFYRESULT_TXSRWSETENTRY,
    '__module__' : 'consensus.consensus_pb2'
    # @@protoc_insertion_point(class_scope:consensus.VerifyResult.TxsRwSetEntry)
    })
  ,
  'DESCRIPTOR' : _VERIFYRESULT,
  '__module__' : 'consensus.consensus_pb2'
  # @@protoc_insertion_point(class_scope:consensus.VerifyResult)
  })
_sym_db.RegisterMessage(VerifyResult)
_sym_db.RegisterMessage(VerifyResult.TxsRwSetEntry)

ProposalBlock = _reflection.GeneratedProtocolMessageType('ProposalBlock', (_message.Message,), {

  'TxsRwSetEntry' : _reflection.GeneratedProtocolMessageType('TxsRwSetEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROPOSALBLOCK_TXSRWSETENTRY,
    '__module__' : 'consensus.consensus_pb2'
    # @@protoc_insertion_point(class_scope:consensus.ProposalBlock.TxsRwSetEntry)
    })
  ,
  'DESCRIPTOR' : _PROPOSALBLOCK,
  '__module__' : 'consensus.consensus_pb2'
  # @@protoc_insertion_point(class_scope:consensus.ProposalBlock)
  })
_sym_db.RegisterMessage(ProposalBlock)
_sym_db.RegisterMessage(ProposalBlock.TxsRwSetEntry)

BlockHeaderConsensusArgs = _reflection.GeneratedProtocolMessageType('BlockHeaderConsensusArgs', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKHEADERCONSENSUSARGS,
  '__module__' : 'consensus.consensus_pb2'
  # @@protoc_insertion_point(class_scope:consensus.BlockHeaderConsensusArgs)
  })
_sym_db.RegisterMessage(BlockHeaderConsensusArgs)

GovernanceMember = _reflection.GeneratedProtocolMessageType('GovernanceMember', (_message.Message,), {
  'DESCRIPTOR' : _GOVERNANCEMEMBER,
  '__module__' : 'consensus.consensus_pb2'
  # @@protoc_insertion_point(class_scope:consensus.GovernanceMember)
  })
_sym_db.RegisterMessage(GovernanceMember)

GovernanceContract = _reflection.GeneratedProtocolMessageType('GovernanceContract', (_message.Message,), {
  'DESCRIPTOR' : _GOVERNANCECONTRACT,
  '__module__' : 'consensus.consensus_pb2'
  # @@protoc_insertion_point(class_scope:consensus.GovernanceContract)
  })
_sym_db.RegisterMessage(GovernanceContract)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033org.chainmaker.pb.consensusZ,chainmaker.org/chainmaker/pb-go/v2/consensus'
  _VERIFYRESULT_TXSRWSETENTRY._options = None
  _VERIFYRESULT_TXSRWSETENTRY._serialized_options = b'8\001'
  _PROPOSALBLOCK_TXSRWSETENTRY._options = None
  _PROPOSALBLOCK_TXSRWSETENTRY._serialized_options = b'8\001'
  _CONSENSUSTYPE._serialized_start=1359
  _CONSENSUSTYPE._serialized_end=1445
  _VERIFYRESULT._serialized_start=81
  _VERIFYRESULT._serialized_end=347
  _VERIFYRESULT_TXSRWSETENTRY._serialized_start=252
  _VERIFYRESULT_TXSRWSETENTRY._serialized_end=316
  _VERIFYRESULT_CODE._serialized_start=318
  _VERIFYRESULT_CODE._serialized_end=347
  _PROPOSALBLOCK._serialized_start=350
  _PROPOSALBLOCK._serialized_end=521
  _PROPOSALBLOCK_TXSRWSETENTRY._serialized_start=252
  _PROPOSALBLOCK_TXSRWSETENTRY._serialized_end=316
  _BLOCKHEADERCONSENSUSARGS._serialized_start=523
  _BLOCKHEADERCONSENSUSARGS._serialized_end=644
  _GOVERNANCEMEMBER._serialized_start=646
  _GOVERNANCEMEMBER._serialized_end=696
  _GOVERNANCECONTRACT._serialized_start=699
  _GOVERNANCECONTRACT._serialized_end=1357
# @@protoc_insertion_point(module_scope)
