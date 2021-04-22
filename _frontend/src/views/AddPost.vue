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
                <select class="form-control" id="Select1" @change="FetchSubacategory()">
                    <option v-for="category in $store.getters.getCategories" :key="category.id" :value="category.id">{{category.name}}</option>
                </select>
            </div>
            <div class="form-group">
                <label for="Select2">SubCategory select</label>
                <select class="form-control" id="Select2">
                    <option v-for="subcategory in subcategories" :key="subcategory.id" :value="subcategory.id">{{subcategory.name}}</option>
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
            fd.append('subcategory', document.getElementById("Select2").value)
            fd.append('image', this.selected_file)
            getAPI.post('/post/add/', fd, {
                headers: {
                    'accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Content-Type': `multipart/form-data`,
                    'Authorization': `Token ${this.$store.getters.getToken}`
                }
            })
            .then(response => {
                console.log(response)
            })
            .catch(error => {
                console.log(error.response.data.non_field_errors[0])
                console.log(error)
            })
        },
        SelectFile() {
            this.selected_file = this.$refs.image_file.files[0]
        },
        FetchSubacategory () {
            if(this.$store.getters.getCategories[parseInt(document.getElementById("Select1").value) - 1] != null)
            {
                this.subcategories = this.$store.getters.getCategories[parseInt(document.getElementById("Select1").value) - 1].subcategories
                document.getElementById("Select2").disabled = false;
            } else {
                document.getElementById("Select2").disabled = true;
                this.subcategories = {name: '', id: 1}
            }
            console.log(document.getElementById("Select1").value)
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
            selected_file: '',
            subcategories: this.$store.getters.getCategories[0].subcategories
        }
    },
}
</script>

<style scoped>
.vh-sm-70{
min-height:72.4vh;
}
</style>