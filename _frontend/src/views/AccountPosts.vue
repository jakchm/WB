<template>
<div id='app'>
    <Navbar />
    <div class="main">
        <div v-if="$store.getters.isAuthenticated" class='container p-2 my-2'>
            <div class="row">
                <div class="col-xl-4 col-lg-6 col-md-6 col-sm-12 col-xs-12" v-for="post in posts" :key="post.id">
                    <Card v-bind:image="post.image" v-bind:title="post.title" v-bind:id="post.id"/>
                </div>
            </div>
        </div>
    </div>
    <Footer />
    <div v-observe-visibility="bottomPaginator"> </div>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
import Navbar from '../components/Navbar'
import Footer from '../components/Footer'
import Card from '../components/Card'
import axios from 'axios'
export default {
    name: 'AccountPosts',
    components: {
        Navbar,
        Footer,
        Card
    },
    created() {
        getAPI.get('post/user', {
                headers: {
                    'accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Authorization': `Token ${this.$store.getters.getToken}` }
            }) 
        .then(response => {
            this.posts = response.data.results
            this.paginator = response.data.next })
        .catch(e => { console.log(e) })
    },
    data () {
        return {
            id: this.$route.params.id,
            posts: [],
            paginator: null
        }
    },
    mounted() { if(!this.$store.getters.isAuthenticated) {this.$router.push({name: 'Home'})} },
    methods: {
        bottomPaginator(isVisible) {
            if (!isVisible) { return } 
            if (this.paginator == null) { console.log("Last page") } 
            else {
                console.log(this.paginator)
                this.loadPagination(this.paginator)
                this.$forceUpdate() }
        },
        loadPagination(path) {
        axios.get(path,  {
                headers: {
                    'accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Authorization': `Token ${this.$store.getters.getToken}` }
            }) 
        .then(response => {
            this.posts.push(...response.data.results)
            console.log(this.posts)
            this.paginator = response.data.next })
        .catch(e => { console.log(e) })
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/style.scss";
</style>
