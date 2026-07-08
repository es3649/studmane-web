import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import { MEALS, type Meal } from '@/data'
import HomeView from '@/views/HomeView.vue'
import NotFound from '@/views/NotFound.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
]

// build up the list from the known list of meals
MEALS.forEach((meal: Meal) => {
  routes.push({
    path: `/${meal.numbers}`,
    name: meal.name,
    component: () => import(`../views/RecipeNumber${meal.numbers}.vue`),
  })
})

routes.push({
  path: '/:pathMatch(.*)',
  // path: '*',
  name: '404 - Not Found',
  component: NotFound,
})

const router = createRouter({
  history: createWebHistory('/totk-cookbook'),
  routes: routes,
})

export default router
