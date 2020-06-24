import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/Login.vue'
import Home from '../components/Home.vue'
import Cate from '../components/goods/Cate.vue'
import Users from '../components/user/Users.vue'
import List from '../components/goods/list.vue'
import Add from '../components/goods/Add.vue'
import Shops from '../components/shops/Shops.vue'

Vue.use(Router)
export default new Router({
    routes: [
        { path: '/', redirect: '/login' },
        { path: '/login', component: Login },
        {
            path: '/home',
            component: Home,
            children: [
                { path: '/categories', component: Cate },
                { path: '/users', component: Users },
                { path: '/lists', component: List },
                { path: '/add', component: Add },
                { path: '/shops', component: Shops }
            ]
        }

    ]
})