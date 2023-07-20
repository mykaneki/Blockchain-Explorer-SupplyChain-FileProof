<!--
    文件搜索
-->
<template>
  <div class="searchInput">
  <h1 style="margin-bottom: 20px">输入搜索文件hash值:</h1>
    <el-input v-model="hashValue" placeholder="Please input" />
  <p v-if="!numRight" class="numRight">请输入23个字符</p>
  <p v-if="numRight" class="numRight">    </p>



  <el-button type="primary" @click="sendHashVaule" :icon="Search" style="margin-bottom: 100px">Search</el-button>
  </div>

  <FileMsgShow :file_name="file_name" :file_hash="file_hash" :tx_id="tx_id" :gas_used="gas_used" :time="time" />

</template>

<script>
import FileMsgShow from "@/components/FileMsgShow";
import axios from "axios";

export default {
  name: "FileMsgSearch",
  components: { FileMsgShow},
  data(){
    return{
      numRight:true,
      hashValue:'',
      file_name:'',
      file_hash:'',
      time:'',
      gas_used:'',
      tx_id:'',
      test:''
    }
  },
  methods:{
    sendHashVaule(){
      if (this.hashValue.length!=23){
        this.numRight=false

        return
      }
      var url="http://119.91.212.68:5000/findFileNameByHash?hash="+this.hashValue
      this.numRight=true
      axios({
        method:"get",
        url:url
      }).then(res=>{
        var data=res.data
        this.file_name=data.file_name
        this.file_hash=data.file_hash
        this.time=data.time
        this.tx_id=data.tx_id
        this.time=data.time
        this.gas_used=data.gas_used
      }

      )

    }
  }
}
</script>

<style scoped>
   .numRight{
     color: red;
     height: 29px;
   }
   el-input{
     width: 90%;
   }
   .searchInput{
     border: lightgray dashed;
     padding: 30px;
     margin-bottom: 30px;
     padding-bottom:0 ;
   }

</style>
