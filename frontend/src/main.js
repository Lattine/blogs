// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from './http' // 导入配置的全局AXIOS
import moment from 'moment' // 导入moment用来格式化UTC时间为本地时间
import 'bootstrap/dist/css/bootstrap.min.css' // Import Booststrap css files
import 'bootstrap'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import VueToasted from 'vue-toasted'
// 字体
import './assets/icon-line/css/simple-line-icons.css'
import './assets/icon-material/material-icons.css'
// 自定义css
import './assets/core.css'
import './assets/custom.css'

// markdown
Vue.use(mavonEditor)

Vue.use(ElementUI)

// Register the vue-toasted plugin on vue
Vue.use(VueToasted, {
  theme: 'bubble',
  position: 'top-center',
  duration: 3000,
  iconPack: 'material',
  action: {
    text: 'Cancel',
    onClick: (e, toastObject) => {
      toastObject.goAway(0)
    }
  }
})

Vue.config.productionTip = false
Vue.prototype.$axios = axios // 将axios挂载到prototype上，在组件中可以直接使用this.$axios访问
Vue.prototype.$moment = moment // 将moment挂载到prototype上，在组件中可以直接使用this.$moment访问

/* eslint-disable no-new */
// npm run lint -- --fix
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
