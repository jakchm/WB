import Vue from 'vue';
import VueCookies from 'vue-cookies';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';


Vue.use(Vuex);
Vue.use(VueCookies);

Vue.$cookies.config('30min')


export default new Vuex.Store({
    plugins: [createPersistedState({
      storage: window.sessionStorage,
    })],
    state: {
        token: null,
        categories_list: []
    },
    mutations: {
        Authenticat(state, token) {
            state.token = token;
        },
        UnAuthenticat(state) {
            state.token = null;
        },
        loadCategories(state, response) {
            state.categories_list = response;
        }
    },
    actions: {},
    getters: {
        isAuthenticated(state) {
            if(state.token != null) return true;
            else return false;
        },
        getToken(state) {
            return state.token
        },
        getCategories(state) {
            return state.categories_list
        }
    }
  });