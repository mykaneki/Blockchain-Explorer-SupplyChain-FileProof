<!--
    产品可用性
-->
<template>
  <el-form :model="form" label-width="220px">
    <el-form-item label="product id">
      <el-input v-model="form.id" />
    </el-form-item>



    <el-form-item label="Product Availability">
      <el-select v-model="form.availability" placeholder="please select availability">
        <el-option label="true" value="true" />
        <el-option label="false" value="false" />
      </el-select>
    </el-form-item>









    <el-form-item>
      <el-button type="primary" @click="onSubmit">Submit</el-button>

    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import axios from "axios";

// do not use same name with ref
const form = reactive({
  availability: '',
  id: ''


})

const onSubmit = () => {
  if (form.availability.length ==0||form.id.length==0){
    alert('输入不能为空')
    return
  }
  const formData=new FormData()
  formData.append('productId',form.id)
  formData.append('isAvailable',form.availability)

  axios({
    method:"post",
    url:"http://119.91.212.68:5000/setProductAvailability",
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
