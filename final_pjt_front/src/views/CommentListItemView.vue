<template>
    <div>
      <!-- <h5>{{ comment.id }}</h5> -->
      <p>{{ comment.content }}</p>
      <hr>
    </div>
  </template>
  
  <script setup>
  
  const props = defineProps({
  comment: Object
})
  </script>
  