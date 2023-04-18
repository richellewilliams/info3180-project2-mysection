<template>
    <div class="body">
        <div class="about container">
            <h5>New Post</h5>

            <div class="form-container">
                <form @submit.prevent="savePost" id="postForm">
                    <div class="form-group">
                        <div class=" pb-4">
                            <label for="photo" class="form-label">Photo</label>
                            <input type="file" name="photo" class="form-control"/>
                        </div>

                        <div class="form-group pb-4">
                            <label for="caption" class="form-label">Caption</label>
                            <textarea type="text" name="caption" class="form-control"></textarea>
                        </div>
        
                        <button class="btn" type="submit">Register</button>
                    </div>
                </form>
            </div>
            
        </div>
    </div>
    
</template>
 
<script setup>
import { ref, onMounted } from "vue";
let jwt_token = ref("");
 
function getJwtToken() { 
    fetch('/api/v1/jwt-token')
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        jwt_token.value = data.jwt_token;
     })
 }
 
onMounted(() => {
    getJwtToken();
});
 
function savePost() {
    let postForm = document.getElementById('postForm');
    let form_data = new FormData(postForm);

    fetch("/api/v1/users/<int:user_id>/posts", {
        method: 'POST',
        body: form_data,
        headers: {
            'Authorization': 'Bearer ' + jwt_token.value
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

<style>
    .body {
        padding: 80px 500px 0px 500px;
    }
    
    .form-container {
        border-color: #d8d5cd;
        border-style: solid;
        border-radius: 5px;
        padding: 43px 40px 25px 40px;
    }

    textarea { 
        height: 100px;
        resize: none;
    } 

    .btn {
        background-color: #7ed321;
        color: white;
        padding: 5px 136px;
    }

    .btn:hover {
        background-color: #7ed321;
        color: white;
    }
</style>