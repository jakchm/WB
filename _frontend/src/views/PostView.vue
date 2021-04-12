<template>
<div id='app'>
    <Navbar></Navbar>
    <div class='container p-4 my-4 vh-sm-70 border'>
        <h2>{{advert.title}}</h2>
        <div class="container m-wd">
            <div class="image-wrapper">
                <img v-if="advert.image != null" :src=advert.image height="300px" width="auto" style="float: left;"/>
            </div>
            <div class="text-block">
                <p>{{advert.text}}</p>
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
export default {
    name: 'AdvertisementView',
    components: {
        Navbar,
        Footer
    },
    created() {
        getAPI.get('post/id/' + this.id,) 
        .then(response => {
            this.advert = response.data
        })
        .catch(e => {
            console.log(e)
        })
    },
    data () {
        return {
            id: this.$route.params.id,
            advert: {}
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
