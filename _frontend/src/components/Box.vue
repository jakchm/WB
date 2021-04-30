<template>
<div class="component-box">
    <div class="head">
        <h3>{{title}}</h3>
    </div>
    <div class="body">
        <slot> </slot>
    </div>
</div>
</template>

<script>
export default {
    name: 'Box',
    props: {
        title: String,
    },
    data() {
        return { }
    },
}
</script>

<style lang="scss" scoped>
@import "@/assets/style.scss";

.component-box {
    max-width: 50%;
    max-height: 50%;
    min-width: 250px;
}
.component-box .head {
    background-color: $headColor;
    height: 60px;
    color: $backgroundColor;
    font-size: 20px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    
}
.component-box .head h3 {
    font-size: 24px;
    margin: auto;
    padding: 15px;
    
}
.component-box .body {
    border: 1px solid $borderColor!important;
    border-style: groove;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    min-height: 50px;
    padding: 2% 5% 12% 5%;
}
</style>
