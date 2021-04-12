<template>
    <div class="alert-box">
        <slot> </slot>
    </div>
</template>

<script>
export default {
    name: 'Alert',
    data() {
        return {
        }
    },
}
</script>

<style scoped>
.alert-box {
    max-width: 50%;
    max-height: 50%;
    background-color: #343a40;
    border: 1px solid #ccc!important;
    border-style: groove;
    border-radius: 5px;
    min-height: 100px;
    padding: 2% 5% 12% 5%;
    font-size: 24px;
    padding: 15px;
    margin: 15px 0 0 0;
    color: white;
    
    }
.alert-box p {
    font-size: 18px;
    color: white;
    margin: 5px;
    line-height: 1.4;
}
</style>
