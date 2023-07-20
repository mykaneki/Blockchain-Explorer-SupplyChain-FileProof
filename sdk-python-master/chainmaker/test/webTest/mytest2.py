from chainmaker.chain_client import ChainClient

# ./testdata/sdk_config.yml 中私钥/证书等如果使用相对路径应相对于当前运行起始目录

def contractResult2json(res):
    file_hash_start=res.find('file_hash')
    file_name_start=res.find('file_name')
    time_start=res.find('time')
    gas_used_start=res.find('gas_used')
    tx_id_start=res.find('tx_id')
    file_hash=res[file_hash_start+14:file_name_start-5]
    file_name=res[file_name_start+14:time_start-5]
    time=res[time_start+7:gas_used_start-5]
    gas_used=res[gas_used_start+10:tx_id_start-3]
    tx_id=res[tx_id_start+8:-1]
    print(tx_id)
cc = ChainClient.from_conf('./testdata/sdk_config.yml')
print(cc.get_chainmaker_server_version())
print(cc.get_current_block_height())
res1 = cc.invoke_contract('fact', 'find_by_file_hash', {"file_hash":"ab3456df5799b87c77e7f88"},
                          with_sync_result=True)

res1=str(res1)
contractResult2json(res1)
print(res1)

print('----------------------------')
res2=cc.get_chain_info();
print(res2)
print(type(res2))

