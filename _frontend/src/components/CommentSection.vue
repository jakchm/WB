<template>
<div class="comment-box">
    <h2>Comments</h2>
<Comment v-for="comment in comment_list" :key="comment.id" :author="comment.author_name">{{comment.text}}</Comment>
<AddComment v-bind:logged="logged" />
</div>
</template>

<script>
import Comment from '../components/Comment'
import AddComment from '../components/AddComment'
export default {
    name: 'CommentSection',
    components: {
        Comment,
        AddComment
    },
    props: {
        comment_list: Array,
    },
    data() {
        return {
        }
    },
}
</script>

<style scoped>
.comment-box {
    border: 1px solid #ccc!important;
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
</style>
