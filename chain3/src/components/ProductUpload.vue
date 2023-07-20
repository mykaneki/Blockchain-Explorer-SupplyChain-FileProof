<!--
    产品信息上传
-->
<template>
  <el-form :model="form" label-width="120px">




    <el-form-item label="product name">
      <el-input v-model="form.name" />
    </el-form-item>









    <el-form-item>
      <el-button type="primary" @click="onSubmit">提交</el-button>

    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import axios from "axios";

// do not use same name with ref
const form = reactive({
  name: '',



})

const onSubmit = () => {
  if (form.name.length ==0){
    alert('输入不能为空')
    return
  }
  const formData=new FormData();
  formData.append('productName', form.name)
  axios({
    method:"post",
    url:"http://119.91.212.68:5000/postProductMsg",
    data:formData,
    headers: {
      'Content-Type': 'multipart/form-data',
    },

  }).then(res=>{
        alert('成功提交')
      }

  )
}
</script>
