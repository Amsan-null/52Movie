<template>
    <div>
        <h1>로그인</h1>
        <form @submit.prevent="LogIn">
            <label for="id">아이디: </label>
            <input type="text" id="userid" v-model.trim="userid"><br>
            <label for="id">비밀번호: </label>
            <input type="password" id="password" v-model.trim="password"><br>
            <input type="submit" value="로그인">
        </form>
    </div>
</template>

<script setup>

</script>

<style scoped>

</style>