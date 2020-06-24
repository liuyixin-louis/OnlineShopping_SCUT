import Vue from 'vue'
import Router from 'vue-router'
// import ECharts from 'vue-echarts/components/ECharts.vue'
// 手动引入 ECharts 各模块来减小打包体积
// import 'echarts/lib/chart/bar'
// import 'echarts/lib/component/tooltip'
// import 'echarts/lib/component/polar'
// import 'echarts/lib/component/legend'
// import 'echarts/lib/component/title.js'
import Login from '../components/Login.vue'
import Home from '../components/Home.vue'
import Cate from '../components/goods/Cate.vue'
import Users from '../components/user/Users.vue'
import List from '../components/goods/list.vue'
import Add from '../components/goods/Add.vue'
import Shops from '../components/shops/Shops.vue'
import Statistics from '../components/statistics/Statistics.vue'
import User_info from '../components/statistics/User_info.vue'
import Order from '../components/orders/Order.vue'
import Stock from '../components/goods/Stock.vue'
import Attribute from '../components/goods/Attribute.vue'


// 注册组件后即可使用
// Vue.component('v-chart', ECharts)


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
                { path: '/attribute', component: Attribute }, ,
                { path: '/shops', component: Shops },
                { path: '/stock', component: Stock },
                { path: '/orders', component: Order },
                { path: '/user_info', component: User_info },
                { path: '/statistics', component: Statistics }
            ]
        }

    ]
})