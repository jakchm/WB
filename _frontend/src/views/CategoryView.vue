<template>
<div id='app'>
    <Navbar></Navbar>
    <div class='container p-2 my-2 vh-sm-70'>
        <div class="row">
            <div class="col-xl-4 col-lg-6 col-md-6 col-sm-12 col-xs-12" v-for="advert in adverts" :key="advert.id">
                <Card v-bind:image="advert.image" v-bind:title="advert.title" v-bind:id="advert.id"/>
            </div>
        </div>
    </div>
    <Footer></Footer>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
import Navbar from '../components/Navbar'
import Footer from '../components/Footer'
import Card from '../components/Card'
export default {
    name: 'SubCategoryView',
    components: {
        Navbar,
        Footer,
        Card
    },
    created() {
        getAPI.get('post/category/' + this.id,) 
        .then(response => {
            this.adverts = response.data
        })
        .catch(e => {
            console.log(e)
        })
    },
    data () {
        return {
            id: this.$route.params.id,
            adverts: []
        }
    },
}
</script>

<style scoped>
.vh-sm-70 {
min-height:73.2vh;
}
.fill .map {
  min-height: 500px;
}
</style>
