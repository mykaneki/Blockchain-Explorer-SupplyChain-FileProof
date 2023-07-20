<!--
    产品信息提交
-->

<template>
  <el-form :model="form" label-width="120px">
    <el-form-item label="product id">
      <el-input v-model="form.id" />
    </el-form-item>



    <el-form-item label="product name">
      <el-input v-model="form.name" />
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
  id: ''


})

const onSubmit = () => {

  alert(form.name+form.id)
}
</script>
