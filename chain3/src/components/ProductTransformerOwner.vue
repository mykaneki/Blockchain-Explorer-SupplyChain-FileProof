<!--
    转移权限
-->
<template>
  <el-form :model="form" label-width="120px">
    <el-form-item label="product id">
      <el-input v-model="form.id" />
    </el-form-item>



    <el-form-item label="new owner">
      <el-input v-model="form.newOwner" />
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
  newOwner: '',
  id: ''


})

const onSubmit = () => {
  if (form.newOwner.length !=40||form.id.length==0){
    alert('输入不能为空')
    return
  }
  const formData=new FormData();
  formData.append('newOwner', form.newOwner)
  formData.append('productId',form.id)
  axios({
    method:"post",
    url:"http://119.91.212.68:5000/transformerOwner",
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
