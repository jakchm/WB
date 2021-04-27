<template>

<div id='app' class="vh-sm-70">
    <Navbar />
    <div v-if="!$store.getters.isAuthenticated" class='container login '>
            <Box title="Login">
                <Alert v-if="error_text != null">{{error_text}}</Alert>
                <md-field>
                    <label>Username</label>
                    <md-input v-model="login_data.username" required></md-input>
                    <span class="md-error">Username is required</span>
                </md-field>
                <md-field>
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
    </div>
    <div v-else class='container login'>
        <button class="btn btn-primary" style="margin: 20px; float: center;" @click="RemoveToken">LogOut</button>
    </div>
    <Footer />
</div>
</template>

<script>
import { getAPI } from '../axios-api'
import Navbar from '../components/Navbar'
import Footer from '../components/Footer'
import Box from '../components/Box'
import Alert from '../components/Alert'
import { mapMutations } from 'vuex';
export default {
    name: 'Login',
    components: {
        Navbar,
        Footer,
        Box,
        Alert
    },
    methods: {
        ...mapMutations([
            'Authenticat',
            'UnAuthenticat'
        ]),
        RemoveToken() {
            this.UnAuthenticat();
            this.$forceUpdate();
        },
        Validate() {
            if(this.login_data.username.length < 3 || this.login_data.username.length > 35) {
                this.error_text = "Username should contain between 3 to 35 characters"
                return false
            }
            if(this.login_data.password.length < 3 || this.login_data.password.length > 20) {
                this.error_text = "Password should contain between 3 to 20 characters"
                return false
            }
            if(this.register_form == true) {
                if(this.login_data.email.length < 6 || this.login_data.email.length > 40)
                {
                    this.error_text = "Email should have at least 6 characters and not more than 40 characters"
                    return false
                }
                if(this.login_data.email.indexOf('@') == -1 || this.login_data.email.indexOf('.') == -1) {
                    this.error_text = "This is not an email address"
                    return false
                }
            }
            this.error_text = null
            return true
        },
        FormSubmit() {
            if(!this.Validate()) { return false}
            getAPI.post('/account/login/', this.login_data)
            .then(response => {
                this.Authenticat(response.data.token)
                this.$forceUpdate()
            })
            .catch(error => { this.error_text = error.response.data.non_field_errors[0] })
        },
        RegisterButton() {
            if(this.register_form == false) {
            this.register_form = true;
            this.$forceUpdate()          
            } else {
                if(!this.Validate()) { return false}
                getAPI.post('/account/register/', this.login_data)
                .then(response => {
                    console.log(response)
                    this.register_form = false;
                    this.$store.mutations.Authenticat(response.data.token)
                    this.$forceUpdate()
                })
                .catch(error => { 
                    this.error_text = error.response.data.non_field_errors[0] 
                    
                })  
            }
        },
        HideEmail() {
            this.register_form = false
            this.$forceUpdate() 
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
            error_text: null
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