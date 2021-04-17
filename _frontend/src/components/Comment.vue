<template>
<div class="comment">
    <h4>{{author}}</h4>
    <slot></slot>
</div>
</template>

<script>
export default {
    name: 'Comment',
    props: {
        author: String
    },
    data() {
        return {
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
    background-color: rgb(248, 248, 248);
}
</style>
