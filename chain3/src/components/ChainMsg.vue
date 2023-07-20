<!--
    区块链信息
-->

<template>

  节点信息
  <ChainMsgForm2 :table-data="tableData"/>

  区块链高度:{{chainHeight}}
</template>

<script>
import axios from "axios";
import ChainMsgForm2 from "@/components/ChainMsgForm2";

export default {
  name: "ChainMsg",
  components: {ChainMsgForm2},
  data(){
    return{
      chainHeight:'',
      chainNode:[],
      tableData:[{node_id:"dsa",node_address:"dsadas"}]
    }

  },
  created() {//获取区块链信息
    axios({
      method:"get",
      url:"http://119.91.212.68:5000/qq"
    }).then(res=>{
          var data=res.data
          this.tableData=data.node_list
          this.chainHeight=data.block_height
        }

    )

  }

}

</script>

<style scoped>

</style>
