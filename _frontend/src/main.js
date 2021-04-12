import Vue from 'vue';
import App from './App.vue';
import router from './routes.js';
import store from './store.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';
import 'vue-material/dist/theme/default.css';

Vue.config.productionTip = false;

Vue.use(VueMaterial);

import Vuelidate from 'vuelidate'
Vue.use(Vuelidate);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
