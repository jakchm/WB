<template>
<div>
    <div v-if="!logged" class="comment">
        <h3>Log in to add comments</h3>
    </div>
    <div v-else class="comment">
        <h4>Add comment</h4>
        <div class="row">
            <input v-model="input_text">
            <button @click="AddComment">Send</button>
        </div>
    </div>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
export default {
    name: 'AddComment',
    methods: {
        AddComment() {
            let fd = {
                text: this.input_text,
                post: this.id
            }
            console.log(fd)
            getAPI.post('/comment/add/', fd, {
                headers: {
                    'accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Authorization': `Token ${this.$store.getters.getToken}`
                }
            })
            .then(response => {
                console.log(response)
                this.$forceUpdate();
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
    mounted() {
      this.logged = this.$store.getters.isAuthenticated;
    },
    data() {
        return {
            logged: false,
            input_text: '',
            id: this.$route.params.id,
        }
    },
}
</script>

<style scoped>
.comment {
    border: 1px solid #ccc!important;
    border-style: groove;
    border-radius: 15px;
    padding: 2%;
    min-height: 60px;
    margin-top: 20px;
    margin-left: 10%;
    margin-right: 0%;
    background-color: rgb(214, 214, 214);
}
.comment input {
    margin-left: 15px;
    margin-right: 5px;
    border-radius: 5px;
    width: 85%;
    height: 30px;
}
.comment button {
    border-radius: 5px;
    background-color: rgb(230, 230, 230);
    
}
</style>
