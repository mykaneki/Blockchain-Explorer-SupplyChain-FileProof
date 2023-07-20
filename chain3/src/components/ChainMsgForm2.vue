<template>
  <el-table :data="tableData" style="width: 100%" max-height="250">
    <el-table-column fixed prop="node_id" label="node_id" width="1000" />
    <el-table-column prop="node_address" label="node_address" width="1000" />


  </el-table>

</template>

<script>


export default {
  name: "ChainMsgForm2",

  props:{
    tableData:Array
  }
}
</script>

<style scoped>

</style>
