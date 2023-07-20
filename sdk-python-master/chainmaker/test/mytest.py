from chainmaker.chain_client import ChainClient
from chainmaker.node import Node
from chainmaker.user import User
from chainmaker.utils import file_utils

user = User('wx-org1.chainmaker.org',
            sign_key_bytes=file_utils.read_file_bytes(
                './testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.tls.key'),
            sign_cert_bytes=file_utils.read_file_bytes(
                './testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.tls.crt'),
            tls_key_bytes=file_utils.read_file_bytes(
                './testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.sign.key'),
            tls_cert_bytes=file_utils.read_file_bytes(
                './testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.sign.crt')
            )

node = Node(
    node_addr='192.168.20.151:12301',
    conn_cnt=1,
    enable_tls=True,
    trust_cas=[
        file_utils.read_file_bytes('./testdata/crypto-config/wx-org1.chainmaker.org/ca/ca.crt'),
        file_utils.read_file_bytes('./testdata/crypto-config/wx-org2.chainmaker.org/ca/ca.crt')
    ],
    tls_host_name='chainmaker.org'
)

cc = ChainClient(chain_id='chain1', user=user, nodes=[node])
print(cc.get_chainmaker_server_version())
print(cc.get_chain_info())