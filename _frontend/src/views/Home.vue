<template>
<div id='app'>
    <Navbar />
    <div class='container p-2 my-2 vh-sm-70'>
        <div class="row">
            <div class="col-xl-4 col-lg-6 col-md-6 col-sm-12 col-xs-12" v-for="post in posts" :key="post.id">
                <Card v-bind:image="post.image" v-bind:title="post.title" v-bind:id="post.id"/>
            </div>
        </div>
    </div>
    <Footer />
    <div v-observe-visibility="bottomPaginator"> </div>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
import axios from 'axios'
import Navbar from '../components/Navbar'
import Footer from '../components/Footer'
import Card from '../components/Card'
export default {
    name: 'Home',
    components: {
        Navbar,
        Footer,
        Card
    },
    created() {
        getAPI.get('post/',) 
        .then(response => {
            this.posts = response.data.results
            this.paginator = response.data.next
            console.log(response.data)
        })
        .catch(e => {
            console.log(e)
        })
    },
    data () {
        return {
            posts: []
        }
    },
    methods: {
        bottomPaginator(isVisible) {
            if (!isVisible) { return } 
            if (this.paginator == null) {
                console.log("Last page")
            } else {
                console.log(this.paginator)
                this.loadPagination(this.paginator)
                this.$forceUpdate()
            }
        },
        loadPagination(path) {
        axios.get(path) 
        .then(response => {
            this.posts.push(...response.data.results)
            console.log(this.posts)
            this.paginator = response.data.next
        })
        .catch(e => {
            console.log(e)
        })
        }
    }
}
</script>

<style scoped>
.fill .map {
  min-height: 500px;
}
.vh-sm-70 {
min-height:73.2vh;
}
</style>
