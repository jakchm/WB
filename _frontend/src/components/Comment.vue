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
        return { }
    },
}
</script>

<style lang="scss" >
@import "@/assets/style.scss";
</style>
