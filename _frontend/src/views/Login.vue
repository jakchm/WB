<template>

<div id='app' class="vh-sm-70">
    
    <Navbar></Navbar>

    <div v-if="!isLoggenIn()" class='container login '>
            <Box title="Login">
                <md-field :class="messageClass">
                    <label>Username</label>
                    <md-input v-model="login_data.username" required></md-input>
                    <span class="md-error">Username is required</span>
                </md-field>
                <md-field :class="messageClass">
                    <label>Password</label>
                    <md-input type="password" v-model="login_data.password" required></md-input>
                    <span class="md-error">Password is required</span>
                 </md-field>
                <md-field v-if="register_form == true">
                    <label>Email</label>
                    <md-input v-model="login_data.email" required></md-input>
                    <span class="md-error">There is an error</span>
                </md-field>
                <md-button class="md-raised" style="float: left;" @click="FormSubmit">Login</md-button>
                <md-button class="md-raised" style="float: right;" @click="RegisterButton">Register</md-button>
                <md-button class="md-raised" v-if="register_form == true" style="float: right;" @click="HideEmail">Hide email</md-button>
            </Box>
            <Alert>
                <p>
                Creating account allow you to add new content and edit it. There is some content available for logged users.
                </p>
            </Alert>
    </div>
    <div v-else class='container login'>
        <button class="btn btn-primary" style="margin: 20px; float: center;" @click="RemoveToken">LogOut</button>
    </div>
    <Footer></Footer>
</div>
</template>

<script>
import { required, minLength, maxLength } from 'vuelidate/lib/validators'
import { getAPI } from '../axios-api'
import Navbar from '../components/Navbar'
import Footer from '../components/Footer'
import Box from '../components/Box'
import Alert from '../components/Alert'
export default {
    name: 'Login',
    components: {
        Navbar,
        Footer,
        Box,
        Alert
    },
    validations: {
        login_data: {
            username: {
                required,
                minLength: minLength(5),
                maxLength: maxLength(25)
            },
            password: {
                required,
                minLength: minLength(6),
                maxLength: maxLength(25)
            },
            email: {
                required,
                minLength: minLength(5),
                maxLength: maxLength(50)
            },
        }
    },
    methods: {
        isLoggenIn() {
            if (this.$cookies.get("token") == null) {
                return false
            } else {
                return true
            }
        },
        RemoveToken() {
            this.$cookies.remove("token")
            this.$forceUpdate()
        },
        FormSubmit() {
            getAPI.post('/account/login/', this.login_data)
            .then(response => {
                if(this.$cookies.get("token") == null) {
                    this.$cookies.set('token',response.data.token,"30MIN")
                    this.$forceUpdate()
                }
            })
            .catch(error => {
                if (error.request.status == 400) {
                    console.log("Zły login lub hasło")
                }
            })
        },
        RegisterButton() {
            if(this.register_form == false) {
            this.register_form = true;
            this.$forceUpdate()          
            } else {
                getAPI.post('/account/register/', this.login_data)
                .then(response => {
                    console.log(response)
                    this.register_form = false;
                    this.$cookies.set('token',response.data.token,"30MIN")
                    this.$forceUpdate()
                })
                .catch(error => {
                    console.log(error)
                    console.log(this.login_data)
                })  
            }
        },
        HideEmail() {
            this.register_form = false
            this.$forceUpdate() 
        }
    },
    computed: {
      messageClass () {
        return {
            'md-invalid': this.hasMessages
            }
        }
    },
    data () {
        return {
            login_data: {
                username: '',
                password: '',
                email: ''
            },
            register_form: false,
        }
    },
}
</script>

<style scoped>
.vh-sm-70{
min-height:70vh;
}
.w-50{
max-width:50%;
}
.login {
    min-height: 63vh;
    margin-top: 50px;
    left: 15%;
    position: relative;
}
.md-app {
    min-height: 300px;
    border: 1px solid rgba(#000, .12);
  }

.md-button {
    background-color:  #343a40;
}

</style>