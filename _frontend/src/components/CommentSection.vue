<template>
<div class="comment-box">
    <h2>Comments</h2>
    <div v-if="comment_list.length > 0">
        <Comment v-for="comment in comment_list" :key="comment.id" :author="comment.author_name">{{comment.text}}</Comment>
    </div>
    <div>
        <div v-if="!logged" class="add">
            <h3>Log in to add comments</h3>
        </div>
        <div v-else class="add">
            <h4>Add comment</h4>
            <div class="row">
                <input v-model="input_text">
                <button @click="AddComment" >Send</button>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
import Comment from '../components/Comment'
export default {
    name: 'CommentSection',
    components: { Comment },
    props: { comment_list: Array },
    methods: {
        AddComment() {
            let fd = {
                text: this.input_text,
                post: this.id }
            if(this.input_text.length < 5 || this.input_text.length > 50) { return false }
            getAPI.post('/comment/add/', fd, {
                headers: {
                    'accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Authorization': `Token ${this.$store.getters.getToken}` }
            })
            .then(response => {
                console.log(response)
                this.$parent.loadComments() })
            .catch(error => {
                console.log(error.response.data.non_field_errors[0]) })
        }
    },
    mounted() { this.logged = this.$store.getters.isAuthenticated; },
    data() {
        return {
            logged: false,
            input_text: '',
            id: this.$route.params.id,
        }
    },
}
</script>

<style lang="scss">
@import "@/assets/style.scss";
.comment-box {
    border: 1px solid $borderColor!important;
    border-style: groove;
    border-radius: 15px;
    padding: 2%;
    min-height: 100px;
    margin-top: 30px;
}
.comment-box h2{
    font-size: 30px;
    margin-bottom: 20px;
    margin-left: 10%;
}
.add {
        border: 1px solid $borderColor!important;
        border-style: groove;
        border-radius: 15px;
        padding: 2%;
        min-height: 60px;
        margin-top: 20px;
        margin-left: 10%;
        margin-right: 0%;
        background-color: rgb(194, 194, 194)!important;
    }
</style>
