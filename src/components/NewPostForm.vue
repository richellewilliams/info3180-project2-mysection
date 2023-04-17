<template>
    <div class="about container">
         <h2 class="pb-4">New Post</h2>
         <form @submit.prevent="saveMovie" id="movieForm">
             <div class="form-group">
                 <div class=" pb-4">
                     <label for="poster" class="form-label">Photo</label>
                     <input type="file" name="poster" class="btn btn-lg w-100"/> <!--change the word from choose to browse-->
                 </div>

                 <div class="form-group pb-4">
                     <label for="caption" class="form-label">Caption</label>
                     <textarea type="text" name="caption" class="form-control"></textarea>
                 </div>
 
                 <button class="btn btn-primary" type="submit">Register</button>
             </div>
         </form>
     </div>
 </template>
 
 <script setup>
 import { ref, onMounted } from "vue";
 let csrf_token = ref("");
 
 function getCsrfToken() { 
     fetch('/api/v1/csrf-token')
     .then((response) => response.json())
     .then((data) => {
         console.log(data);
         csrf_token.value = data.csrf_token;
     })
 }
 
 onMounted(() => {
     getCsrfToken();
 });
 
 function saveMovie() {
 
     fetch("/api/v1/register", {
         method: 'POST',
         body: form_data,
         headers: {
             'X-CSRFToken': csrf_token.value
         }
     })
     .then(function (response) {
         return response.json();
     })
     .then(function (data) {
         console.log(data);
     })
     .catch(function (error) {
         console.log(error);
     });
 };
 </script>