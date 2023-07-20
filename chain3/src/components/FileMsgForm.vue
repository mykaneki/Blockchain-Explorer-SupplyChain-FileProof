<!--
    文件信息提交
-->
<template>
  <el-form :model="form" label-width="120px">
    <el-form-item label="File name">
      <el-input v-model="form.name" />
    </el-form-item>



      <el-form-item label="Hash value">
        <el-input v-model="form.hash" />
      </el-form-item>

    <el-form-item label="time">
      <el-input v-model="form.time" />
    </el-form-item>







    <el-form-item>
      <el-button type="primary" @click="onSubmit">Create</el-button>

    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'

// do not use same name with ref
const form = reactive({
  name: '',
  hash: '',
  time: '',

})

const onSubmit = () => {
  if(form.hash.length!=23){
    alert("请输入23个字符的hash值")
    return
  }
  alert(form.name+form.hash+form.time)
}
</script>

















