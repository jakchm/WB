import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home'
import CategoryView from './views/CategoryView'
import SubCategoryView from './views/SubCategoryView'
import PostView from './views/PostView'
import AddPost from './views/AddPost'
import Login from './views/Login'
import Account from './views/Account'
import AccountPosts from './views/AccountPosts'


Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home, },
        {
            path: '/category/:id',
            name: 'CategoryView',
            props: true,
            component: CategoryView, },
        {
            path: '/subcategory/:id',
            name: 'SubCategoryView',
            props: true,
            component: SubCategoryView, },        
        {
            path: '/post/:id',
            name: 'PostView',
            props: true,
            component: PostView, },
        {
            path: '/post_add',
            name: 'AddPost',
            component: AddPost, },
        {
            path: '/account/login',
            name: 'Login',
            component: Login, },  
        {
            path: '/account',
            name: 'Account',
            component: Account, },
        {
            path: '/account/posts',
            name: 'AccountPosts',
            component: AccountPosts, },
    ]
})