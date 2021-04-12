import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home'
import CategoryView from './views/CategoryView'
import PostView from './views/PostView'
import AddPost from './views/AddPost'
import Login from './views/Login'


Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home,
        },
        {
            path: '/category/:id',
            name: 'CategoryView',
            props: true,
            component: CategoryView,
        },
        {
            path: '/post/:id',
            name: 'PostView',
            props: true,
            component: PostView,
        },
        {
            path: '/post_add',
            name: 'AddPost',
            component: AddPost,
        },
        {
            path: '/account/login',
            name: 'Login',
            component: Login,
        }   
    ]
})