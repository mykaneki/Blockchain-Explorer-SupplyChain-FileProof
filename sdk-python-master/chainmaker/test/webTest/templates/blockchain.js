window.onload = function() {
    // 向伺服器發起請求獲取區塊鏈信息
    fetch('http://119.91.212.68:5000/qq')
        .then(response => response.text())
        .then(data => {
            // 解析區塊鏈信息
            console.error(typeof data)
            var chainInfo = JSON.parse(data);

            // 更新區塊高度
            var blockHeightElement = document.getElementById('block-height');
            blockHeightElement.innerHTML = '区块高度: ' + chainInfo.block_height;

            // 更新節點列表
            var nodeListElement = document.getElementById('node-list');
            nodeListElement.innerHTML = '<h2>节点列表</h2>';

            for (var i = 0; i < chainInfo.node_list.length; i++) {
                var node = chainInfo.node_list[i];
                var nodeElement = document.createElement('div');
                nodeElement.innerHTML = '<strong>节点ID:</strong> ' + node.node_id + '<br>' +
                                        '<strong>节点地址:</strong> ' + node.node_address + '<br>' +

                nodeListElement.appendChild(nodeElement);
            }
        })
        .catch(error => console.error(error));
};
