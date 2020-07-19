import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import About from '@/components/About'

Vue.use(Router)

export default new Router({
  mode: 'history', 
  routes: [
    {
      path: '/home-page/',
      name: 'home',
      component: Home
    },
    {
      path: '/home-page/',
      name: 'about',
      component: About
    }
  ]
})