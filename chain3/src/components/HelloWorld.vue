<!--
    主页
-->
<template>
  <div class="centered-content">
    <div class="image-container">
      <div class="image-wrapper">
        <img src="../assets/logo.png" alt="Logo" />
      </div>
      <p class="text">区块链浏览器</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "FileMsgShow",
}
</script>

<style scoped>
.centered-content {

  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.image-container {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.image-wrapper {
  margin-bottom: 10px;
}

.image-container img {
  max-width: 100%;
  height: auto;
}

.text {
  font-size: 40px;
}
</style>
