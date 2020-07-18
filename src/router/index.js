import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  mode: 'history',  // 追記 URLに#が入るのを防止
  routes: [
    {
        path: '/hello',
        name: 'HelloWorld',
        component: HelloWorld
    }
  ]
})