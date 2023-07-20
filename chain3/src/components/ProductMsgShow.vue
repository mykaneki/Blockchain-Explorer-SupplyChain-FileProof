<!--
    产品信息展示列表
-->
<template>
  <el-descriptions title="产品信息" :column="3" border>
    <el-descriptions-item
        label="产品id"
        label-align="right"
        align="center"
        label-class-name="my-label"
        class-name="my-content"
        width="150px"
    >{{ file_name }}</el-descriptions-item
    >
    <el-descriptions-item label="产品可用性" label-align="right" align="center"
    >{{file_hash}}</el-descriptions-item
    >

    <el-descriptions-item label="拥有者" label-align="right" align="center">
      <el-tag size="small">{{gas_used}}</el-tag>
    </el-descriptions-item>
    <el-descriptions-item label="产品名" label-align="right" align="center"
    >{{tx_id}}</el-descriptions-item
    >
  </el-descriptions>
</template>

<script>
export default {
  name: "FileMsgShow",

  props: {
    file_name:String,
    file_hash:String,
    gas_used:String,
    tx_id:String
  }
}
</script>

<style scoped>

</style>
