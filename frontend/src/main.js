import Vue from 'vue'
import App from './App.vue'
import '../node_modules/spectre.css/dist/spectre.min.css'
import '../node_modules/spectre.css/dist/spectre-icons.min.css'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
