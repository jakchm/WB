<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class='container'>
    <router-link class="navbar-brand" to="/" ><img src="../assets/logo.png"></router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarToggle">
      <ul class="navbar-nav dropdown" v-for="c in Categories" :key="c.key">
        <li class="nav-item">
          <router-link class="menu-item dropbtn" :to="{ name: 'CategoryView', params: {id: c.id} }" >{{c.name}}</router-link>
            <div class="dropdown-content">
            <router-link v-for="s in c.subcategories" :key="s.id" :to="{ name: 'SubCategoryView', params: {id: s.id} }" > {{s.name}} </router-link>
            </div>
        </li>
      </ul>
    </div>
    <div class="row" v-if="logged" >
      <router-link class="nav-link" to="/post_add" > Add Article </router-link>
      <router-link class="nav-link" to="/account/login" > Your account </router-link>
    </div>
    <div v-else>
      <router-link class="nav-link" to="/account/login" > Log In </router-link>
    </div>
    <router-view :key ='$route.path' />
  </div>
</nav>
</template>

<script>
import { getAPI } from '../axios-api'
import { mapMutations } from 'vuex'
export default {
    name: 'Navbar',
    data() {
        return {
          Categories: [],
          logged: false
        }
    },
    methods: {
      ...mapMutations([
      'loadCategories', 
      ]),
    },
    created() {
      if(this.$store.getters.getCategories.length == 0)
      {
        getAPI.get('/category/')
        .then(response => {
          this.Categories = response.data
          this.loadCategories(response.data);

        })
        .catch(err => {
          console.log(err)
        })
      } else {
        this.Categories = this.$store.getters.getCategories;
      }
    },
    mounted() {
      this.logged = this.$store.getters.isAuthenticated
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
    cursor: pointer;
}

.dropbtn {
  color: white;
  padding: 16px;
  font-size: 16px;
  cursor: pointer;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #343a40;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1000;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #43484e}

.dropdown:hover .dropdown-content {
  display: block;
}

</style>
