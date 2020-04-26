import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import CougarsLament from './views/CougarsLament.vue'
// const CougarsLament = () => import('./views/CougarsLament.vue') 

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/blag',
      name: 'home',
      component: Home
    },
    {
      path: '/cougarslament',
      name: "Cougar's Lament",
      component: CougarsLament
      // component: () => import('./views/CougarsLament.vue')
    }
    // {
    //   path: '/blag/truth',
    //   name: 'truth',
    //   // component: () => import('./views/Truth.vue')
    // },
    // {
    //   path: '/movie',
    //   name: 'movie',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('./views/Movie.vue')
    // }
  ]
})