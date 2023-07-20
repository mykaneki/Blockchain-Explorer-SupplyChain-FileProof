<!--
    合约应用页面
-->
<template>
  <div class="common-layout">
    <el-container>
      <el-aside ><div class="list"><ContractFunctionList @fileMsgUpload="fileMsgUpload" @fileMsgShow="fileMsgShow" @productUpload="productUpload" @productSearch="productSearch" @productSetAvailability="productSetAvailability" @productTransformerOwner="productTransformerOwner"/></div></el-aside>
      <el-main>
        <FileMsgSearch v-if="choice==='fileMsgSearch'"/>
        <FileMsgForm v-if="choice==='fileMsgUpload'"/>
        <ProductUpload v-if="choice==='productUpload'"/>
        <ProductSearch v-if="choice==='productSearch'"/>
        <ProductAvailability v-if="choice==='productSetAvailability'"/>
        <ProductTransformerOwner v-if="choice==='productTransformerOwner'"/>

      </el-main>
    </el-container>
  </div>
</template>

<script>
import ContractFunctionList from "@/components/ContractFunctionList";

import FileMsgSearch from "@/components/FileMsgSearch";
import FileMsgForm from "@/components/FileMsgForm";
import ProductUpload from "@/components/ProductUpload";
import ProductSearch from "@/components/ProductSearch";
import ProductAvailability from "@/components/ProductAvailability";
import ProductTransformerOwner from "@/components/ProductTransformerOwner";
export default {
  name: "ContractFunction",
  components: {
    ProductTransformerOwner,
    ProductAvailability, ProductSearch, ProductUpload, FileMsgForm, FileMsgSearch,  ContractFunctionList },
  methods:{
    fileMsgUpload(){
      this.choice='fileMsgUpload'
    },
    fileMsgShow(){
      this.choice='fileMsgSearch'
    },
    productUpload(){
      this.choice='productUpload'
    },
    productSearch(){
      this.choice='productSearch'
    },
    productSetAvailability(){
      this.choice='productSetAvailability'
    },
    productTransformerOwner(){
      this.choice='productTransformerOwner'
    }

  },
  data(){
    return{
      choice:'fileMsgUpload'
    }
  }
};
</script>

<style scoped>
.common-layout {
  position: fixed;
  top: 50px;
  left: 0;
  height: 100vh;
  width: 100vw; /* 修改这里的宽度为 viewport 的宽度 */

}

.el-container {
  display: flex; /* 使用 Flexbox 布局 */
}

.el-aside {
  flex: 0 0 250px; /* 设置 el-aside 的固定宽度为 500px */

}

.el-main {
  flex: 1; /* 让 el-main 占据剩余空间 */

}
.list{
  height: 100vw;
  background-color: #545c64;
}
</style>
