<template>
    <div class="alert-box">
        <slot> </slot>
    </div>
</template>

<script>
export default {
    name: 'Alert',
    data() {
        return {}
    },
}
</script>

<style lang="scss" scoped>
@import "@/assets/style.scss";
.alert-box {
    max-width: 50%;
    max-height: 50%;
    background-color: $headColor;
    border: 1px solid $borderColor!important;
    border-style: groove;
    border-radius: 5px;
    min-height: 70px;
    padding: 2% 5% 12% 5%;
    font-size: 24px;
    padding: 15px;
    margin: 15px 0 15px 0;
    color: white;
    display: table-cell;
    vertical-align: middle;
    }
.alert-box p {
    font-size: 18px;
    color: white;
    margin: 5px;
    line-height: 1.4;
}
</style>
