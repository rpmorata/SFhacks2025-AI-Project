import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Clasify from '../views/Clasify.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/clasify', component: Clasify }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
