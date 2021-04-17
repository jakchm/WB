<template>
<div id='app'>
    <Navbar></Navbar>
    <div class='container p-4 my-4 vh-sm-70 border'>
        <h2>{{post.title}}</h2>
        <div class="container m-wd">
            <div class="image-wrapper">
                <img v-if="post.image != null" :src=post.image height="300px" width="auto" style="float: left;"/>
            </div>
            <div class="text-block">
                <p>{{post.text}}</p>
            </div>
            <CommentSection v-if="comments.length > 0" v-bind:comment_list="comments"></CommentSection>
        </div>
    </div>
    <Footer></Footer>
</div>
</template>

<script>
//import { BASE_URL } from '../axios-api'
import Navbar from '../components/Navbar'
import Footer from '../components/Footer'
import CommentSection from '../components/CommentSection'
import axios from 'axios'
export default {
    name: 'PostView',
    components: {
        Navbar,
        Footer,
        CommentSection
    },
    created() {
        const post_request = axios.get('http://127.0.0.1:8000' + '/post/id/' + this.id);
        const comment_request = axios.get('http://127.0.0.1:8000' + '/comment/post/' + this.id);

        axios.all([post_request, comment_request])
        .then(axios.spread((...responses) => {
            this.post = responses[0].data
            this.comments = responses[1].data
        }))
        .catch(errors => {
            console.log(errors)
        })
        //getAPI.get('post/id/' + this.id,) 
        //.then(response => {
        //    this.post = response.data
        //})
        //.catch(e => {
        //    console.log(e)
        //})
    },
    mounted() {
      this.logged = this.$store.getters.isAuthenticated
    },
    data () {
        return {
            id: this.$route.params.id,
            post: {},
            comments: {}
        }
    },
}
</script>

<style scoped>
body {
  display:flex;
  background-color:#acd5ff;
  justify-content:center;
  align-items:flex-end;
  font-family:Open Sans;
}

.vh-sm-70{
min-height:69.5vh;
}

h2 {
    position: relative;
    left: 3%;
    margin: 20px;
}

img {
    display: block;
    max-width: 100%;
    max-height: auto;
    margin: 0 0 10px 0;
    padding: 10px;
}

.image-wrapper {
  position: relative;
}

.image-wrapper img {
  position: relative;
  object-fit: cover;
  width: 100%;
  height: 100%;
}

.text-block {
    white-space: pre-line;
}

.m-wd {
    max-width: 80%;
    margin: 0 10% 0 10%;
    text-align: justify;
    text-justify: inter-word;
}

h2 {
    margin: 0 0 0 11%;
}

.border {
    border: 1px solid #ccc!important;
    border-style: groove;
    border-radius: 15px;
}

</style>
