import Vue from 'vue'
import axios from 'axios'
import router from './router'
import store from './store'

// Basic Config
axios.defaults.timeout = 5000
axios.defaults.baseURL = 'http://localhost:5000/api'

// Add a request interceptor
axios.interceptors.request.use(function (config) {
  const token = window.localStorage.getItem('blog-token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
}, function (error) {
  return Promise.reject(error)
})

// Add a response interceptor
axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  switch (error.response.status) {
    case 401:
      // clear Token and Authorization infos
      store.logoutAction()
      if (router.currentRoute.path !== '/login') {
        Vue.toasted.error('401: 认证已失效，请先登录', { icon: 'fingerprint' })
        router.replace({
          path: 'login',
          query: { redirect: router.currentRoute.path }
        })
      }
      break
    case 404:
      Vue.toasted.error('404: NOT FOUND', { icon: 'fingerprint' })
      router.back()
      break
  }
  return Promise.reject(error)
})

export default axios
