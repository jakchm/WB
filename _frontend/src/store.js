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
        categories_list: {},
    },
    mutations: {
        LoadData(state, categories) {
            if(state.categories_list == null) {
                state.categories_list = categories;
            }
        }
    },
    actions: {},
    getters: {
        getCategories(state) {
            return state.categories_list
        }
    }
  });