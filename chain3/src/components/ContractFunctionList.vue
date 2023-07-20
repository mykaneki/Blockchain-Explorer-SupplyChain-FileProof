<!--
    合约应用列表
-->
<template>
  <el-col :span="24" style="width: 100%">

    <el-menu
        active-text-color="#ffd04b"
        background-color="#545c64"
        class="el-menu-vertical-demo"

        default-active="2"
        text-color="#fff"
        @open="handleOpen"
        @close="handleClose"
    >
      <el-sub-menu index="1">
        <template #title>
          <el-icon><location /></el-icon>
          <span>文件存证</span>
        </template>
        <el-menu-item-group >
          <el-menu-item index="1-1" @click="fileMsgUpload">上传文件信息</el-menu-item>
          <el-menu-item index="1-2" @click="fileMsgShow">搜索文件</el-menu-item>
        </el-menu-item-group>


      </el-sub-menu>
      <el-sub-menu index="2">
        <template #title>
          <el-icon><location /></el-icon>
          <span>供应链管理</span>
        </template>
        <el-menu-item-group >
          <el-menu-item index="2-1" @click="productUpload">添加商品</el-menu-item>
          <el-menu-item index="2-2" @click="productSearch">查询商品</el-menu-item>
          <el-menu-item index="2-2" @click="productSetAvailability">改变状态</el-menu-item>
          <el-menu-item index="2-2" @click="productTransformerOwner">转移拥有者</el-menu-item>
        </el-menu-item-group>

      </el-sub-menu>

    </el-menu>
  </el-col>
</template>

<script>
export default {
  name: "ContractFunctionList",
  methods:{
    fileMsgUpload(){
      this.$emit('fileMsgUpload')
    },
    fileMsgShow(){
      this.$emit('fileMsgShow')
    },
    productUpload(){
      this.$emit('productUpload')
    },
    productSearch(){
      this.$emit('productSearch')
    },
    productSetAvailability(){
      this.$emit('productSetAvailability')
    },
    productTransformerOwner(){
      this.$emit('productTransformerOwner')
    }
  }
}
</script>

<style scoped>

</style>
