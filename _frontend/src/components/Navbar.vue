<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class='container'>
    <router-link class="navbar-brand" to="/" ><img src="../assets/logo.png"></router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <ul class="navbar-nav" v-for="c in getCategories" :key="c.key">
        <li class="nav-item">
          <router-link class="menu-item" :to="{ name: 'CategoryView', params: {id: c.id} }" >{{c.name}}</router-link>
        </li>
      </ul>
    </div>
    <router-link :v-if="$cookies.isKey('token')" class="nav-link" to="/account/login" >
      Logged
    </router-link>
    <router-view :key ='$route.path' />
  </div>
</nav>
</template>

<script>
import { mapMutations } from 'vuex';
import { mapGetters } from 'vuex';
import { getAPI } from '../axios-api'
export default {
    name: 'Navbar',
    data() {
        return {
          Categories: []
        }
    },
    methods: {
    isLoggenIn() {
      if (!this.$cookies.isKey("token")) {
        return false
      } else {
        return true
      }
    },
      ...mapMutations([
        'LoadData'
      ]),
      ...mapGetters([
        'getCategories'
      ]),
    },
    created() {
      if(this.getCategories == null) {
        getAPI.get('/category/')
        .then(response => {
          this.Categories = response.data
          this.LoadData(response.data)
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
    watch: { 
      $route(to, from) { 
        if(to !== from) { location.reload(); } 
      }
    }

}
</script>

<style scoped>
nav {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  nav .menu-item:link {
  color: red;
  }
  nav .menu-item {
    color: rgb(241, 241, 241);
    font-size: 18px;
    font-family: "Helvetica", sans-serif;
    padding: 10px 10px;
    margin: 2px;
    position: relative;
    text-align: center;
    border-bottom: 3px solid transparent;
    display: flex;
    transition: 0.4s;
  }
.md-theme-default a:not(.md-button) {
    color: #448aff;
    color: #ffffff;
    text-decoration: none;
}
</style>
