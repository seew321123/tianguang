import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Admin from '../views/Admin.vue'
import categoryAdmin from '../views/categoryAdmin.vue'
import scrollAdmin from '../views/scrollAdmin.vue'
import adminCenter from '../views/adminCenter.vue'
import configAdmin from '../views/configAdmin.vue'
import index from '../views/index.vue'
import intro from '../views/intro.vue'
import news from '../views/news.vue'
import product from '../views/product.vue'
import productdetail from '../views/productDetail.vue'
import newsdetail from '../views/newsDetail.vue'
import project from '../views/project.vue'
import contact from '../views/contact.vue'

Vue.use(VueRouter)

  const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  {
    path: '/admin',
    name: 'admin',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Admin
  },
  {
    path: '/categoryadmin',
    name: 'categoryadmin',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: categoryAdmin
  },
  {
    path: '/configadmin',
    name: 'configadmin',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: configAdmin
  },
  {
    path: '/scrolladmin',
    name: 'scrolladmin',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: scrollAdmin
  },
  {
    path: '/',
    name: 'admincenter',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: adminCenter
  },
  {
    path: '/index',
    name: 'index',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: index
  },
  {
    path:'/intro',
    name:'intro',
    component: intro
  },
  {
    path:'/news',
    name:'news',
    component: news
  },
  {
    path:'/product',
    name:'product',
    component: product
  },  
  {
    path:'/productdetail',
    name:'productdetail',
    component: productdetail
  },
  {
    path:'/newsdetail',
    name:'newsdetail',
    component: newsdetail
  },
  {
    path:'/project',
    name:'project',
    component: project
  },
  {
    path:'/contact',
    name:'contact',
    component: contact
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
