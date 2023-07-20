<template>





  <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
    <el-tab-pane label="主页" name="first"><hello-world msg="dsad"/></el-tab-pane>
    <el-tab-pane label="区块链信息" name="second"><ChainMsg/></el-tab-pane>
    <el-tab-pane label="合约应用" name="third"><ContractFunction /></el-tab-pane>

  </el-tabs>
</template>
<script lang="ts" setup>
import { ref } from 'vue'
import type { TabsPaneContext } from 'element-plus'
import HelloWorld from "@/components/HelloWorld.vue";
import ContractFunction from "@/components/ContractFunction.vue";
import FileMsgSearch from "@/components/FileMsgSearch.vue"
import ChainMsg from "@/components/ChainMsg.vue"
import Functions from "@/components/ContractFunction.vue";


const activeName = ref('first')

const handleClick = (tab: TabsPaneContext, event: Event) => {
  console.log(tab, event)
}
</script>
<style>

.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 16px;
  font-weight: 600;
}
</style>
