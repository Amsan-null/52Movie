<template>
    <div>
        <h5>당신을 위한 영화추천</h5>
        <h1>이런 영화들은 어때요?</h1>
    </div>
    <h3 v-if="my_users_like_movies.length > 0"> </h3>

        <div v-for = "(movie, idx) in my_users_like_movies"
        :key="idx">
    </div>
</template>

<script setup>



</script>

<style scoped>

</style>