<!--
    搜索产品页面
-->

<template>
  <div class="searchInput">
    <h1 style="margin-bottom: 20px">输入产品id:</h1>
    <el-input v-model="hashValue" placeholder="Please input" />

    <p  class="numRight">    </p>



    <el-button type="primary" @click="sendHashVaule" :icon="Search" style="margin-bottom: 100px">Search</el-button>
  </div>

  <ProductMsgShow :file_name="file_name" :file_hash="available" :tx_id="tx_id" :gas_used="affiliated_person"  />

</template>

<script>
import ProductMsgShow from "@/components/ProductMsgShow";
import axios from "axios";

export default {
  name: "FileMsgSearch",
  components: { ProductMsgShow},
  data(){
    return{
      numRight:true,
      hashValue:'',
      file_name:'',
      file_hash:'',
      available:'',
      affiliated_person:'',
      tx_id:'',
      test:''
    }
  },
  methods:{
    sendHashVaule(){

      var url="http://119.91.212.68:5000/getProductMsgById?productId="+this.hashValue
      this.numRight=true
      axios({
        method:"get",
        url:url
      }).then(res=>{//获取响应的数据，赋值变量
            var data=res.data
            var result=data.contract_result.result;
            var resultData=result.split(' ')
            this.file_name=resultData[0].split('[')[1]
            this.tx_id=''
            var len=resultData.length
            for(var i=0;i< len-3;i++){
              this.tx_id=this.tx_id+resultData[1+i]+' '
        }

            this.available=resultData[len-1].split(']')[0]
            //this.file_hash=data.contract_result.file_hash


            this.affiliated_person=resultData[len-2]
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
