<template>
<div id='app'>
    <Navbar></Navbar>
    <div class='container p-2 my-2 vh-sm-70'>
            <div class="form-group">
                <label for="PostTitle">Post Title</label>
                <input class="form-control" id="PostTitle" v-model="post_data.title">
            </div>
            <div class="form-group">
                <label for="PostText">Post text</label>
                <textarea class="form-control" id="PostText" rows="3"  v-model="post_data.text"></textarea>
            </div>
            <div class="form-group">
                <label for="Select1">Category select</label>
                <select class="form-control" id="Select1">
                    <option v-for="category in categories_list" :key="category.id" :value="category.id">{{category.name}}</option>
                </select>
            </div>
            <div class="form-group">
                <input class="form-control" type='file' id='img_file' ref="image_file" @change="SelectFile()">
            </div>
            <button class="btn btn-primary" @click="FormSubmit">Submit</button>
    </div>
    <Footer></Footer>
</div>
</template>

<script>
import { mapState } from 'vuex';
import { getAPI } from '../axios-api'
import Navbar from '../components/Navbar'
import Footer from '../components/Footer'
import FormData from 'form-data'
export default {
    name: 'AddPostView',
    components: {
        Navbar,
        Footer
    },
    computed: {
        ...mapState([
            'categories_list'
        ])
    },
    methods: {
        FormSubmit() {
            let fd = new FormData();
            fd.append('title', this.post_data.title)
            fd.append('text', this.post_data.text)
            fd.append('category', document.getElementById("Select1").value)
            fd.append('subcategory', this.post_data.subcategory)
            fd.append('image', this.selected_file)
            getAPI.post('/post/add/', fd, {
                headers: {
                    'accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Content-Type': `multipart/form-data`,
                    'Authorization': `Token ${this.$cookies.get("token")}`
                }
            })
            .then(response => {
                console.log(response)
            })
            .catch(error => {
                console.log(error)
            })
        },
        SelectFile() {
            this.selected_file = this.$refs.image_file.files[0]
        }
    },
    data () {
        return {
            post_data: {
                title: '',
                text: '',
                category: 1,
                subcategory: 1,
            },
            selected_file: ''
        }
    },
}
</script>

<style scoped>
.vh-sm-70{
min-height:72.4vh;
}
</style>