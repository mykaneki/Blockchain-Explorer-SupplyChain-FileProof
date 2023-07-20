<!--
    文件信息展示列表

-->
<template>
  <el-descriptions title="文件信息" :column="3" border>
    <el-descriptions-item
        label="file name"
        label-align="right"
        align="center"
        label-class-name="my-label"
        class-name="my-content"
        width="150px"
    >{{ file_name }}</el-descriptions-item
    >
    <el-descriptions-item label="file hash" label-align="right" align="center"
    >{{file_hash}}</el-descriptions-item
    >
    <el-descriptions-item label="time" label-align="right" align="center"
    >{{time}}</el-descriptions-item
    >
    <el-descriptions-item label="gas used" label-align="right" align="center">
      <el-tag size="small">{{gas_used}}</el-tag>
    </el-descriptions-item>
    <el-descriptions-item label="tx id" label-align="right" align="center"
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
    time:String,
    gas_used:String,
    tx_id:String
  }
}
</script>

<style scoped>

</style>
