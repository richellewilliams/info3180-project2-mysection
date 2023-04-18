<template>
    <div class="body">
        <div class="about container">
            <h5>Register</h5>

            <div class="form-container">
                <form @submit.prevent="saveUser" id="userForm">
                    <div class="form-group">
                        <div class="form-group pb-4">
                            <label for="username" class="form-label">Username</label>
                            <input type="text" name="username" class="form-control"/>
                        </div>
                            
                        <div class="form-group pb-4">
                            <label for="password" class="form-label">Password</label>
                            <input type="password" name="password" class="form-control"/>
                        </div>

                        <div class="form-group pb-4">
                            <label for="firstname" class="form-label">Firstname</label>
                            <input type="text" name="firstname" class="form-control"/>
                        </div>

                        <div class="form-group pb-4">
                            <label for="lastname" class="form-label">Lastname</label>
                            <input type="text" name="lastname" class="form-control"/>
                        </div>

                        <div class="form-group pb-4">
                            <label for="email" class="form-label">Email</label>
                            <input type="text" name="email" class="form-control"/>
                        </div>

                        <div class="form-group pb-4">
                            <label for="location" class="form-label">Location</label>
                            <input type="text" name="location" class="form-control"/>
                        </div>

                        <div class="form-group pb-4">
                            <label for="biography" class="form-label">Biography</label>
                            <textarea type="text" name="biography" class="form-control"></textarea>
                        </div>

                        <div class=" pb-4">
                            <label for="profile_photo" class="form-label">Photo</label>
                            <input type="file" name="profile_photo" class="form-control"/>
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

function saveUser() {
    let userForm = document.getElementById('userForm');
    let form_data = new FormData(userForm);

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

<style>
    .body {
        padding: 90px 500px 0px 500px;
    }
    
    .form-container {
        border-color: #d8d5cd;
        border-style: solid;
        border-radius: 5px;
        padding: 45px 40px 25px 40px;
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