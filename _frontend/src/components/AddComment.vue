<template>
<div>
    <div v-if="!logged" class="comment">
        <h3>Log in to add comments</h3>
    </div>
    <div v-else class="comment">
        <h4>Add comment</h4>
        <input>
    </div>
</div>
</template>

<script>
export default {
    name: 'AddComment',
    mounted() {
      this.logged = this.$store.getters.isAuthenticated
    },
    data() {
        return {
            logged: false,
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
</style>
