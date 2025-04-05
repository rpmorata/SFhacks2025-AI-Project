import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GetStartedView from '../views/GetStartedView.vue'
import AboutView from '../views/AboutView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/about', component: AboutView },
  { path: '/get-started', component: GetStartedView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
