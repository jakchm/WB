<template>
<div id='app'>
    <Navbar />
        <div class=" container account-box col-md-6 col-sm-12 col-xs-12">
            <Box title="Account data">
                <div class="info_text_box">
                    <span> Name: </span>{{user_data.username}} <br />
                    <span> Email: </span>{{user_data.email}}
                </div> 
            </Box>
        </div>
        <div class=" container account-box col-md-6 col-sm-12 col-xs-12">
            <Box title="My Posts">
                Total post: {{user_data.posts}} <br />
                <router-link :to="{ name: 'AccountPosts'}" >List of post</router-link>
            </Box>
        </div>
        <div class=" container account-box col-md-6 col-sm-12 col-xs-12">
            <Box title="Statistics">
                cec
            </Box>
        </div>
    <Footer />
</div>
</template>

<script>
import { getAPI } from '../axios-api'
import Navbar from '../components/Navbar'
import Footer from '../components/Footer'
import Box from '../components/Box'
export default {
    name: 'AddPostView',
    components: {
        Navbar,
        Footer,
        Box
    },
    created() {
        getAPI.get('/account/info/', {
            headers: {
                'accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.8',
                'Content-Type': `multipart/form-data`,
                'Authorization': `Token ${this.$store.getters.getToken}`
                }
            })
            .then(response => {
                this.user_data = response.data[0]
                console.log(this.user_data)
            })
            .catch(error => {
                console.log(error.response.data.non_field_errors[0])
                console.log(error)
            })
        },
    data () {
        return {
            user_data: []
        }
    }
}
</script>

<style scoped>
.vh-sm-70{
min-height:72.4vh;
}

.account-box {
    margin-bottom: 35px;
    margin-top: 35px;
    align-items: center;
}

.account-box p {
    font-size: 15px;
}


.info_text_box {
  display: table-cell;
  vertical-align: middle;
}

span {
    font-size: 22px;
    margin-top: 15px;
    display: inline-block;
    vertical-align: middle;
    line-height: normal
}




</style>