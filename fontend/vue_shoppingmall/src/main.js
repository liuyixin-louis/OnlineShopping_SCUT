import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'





//echart
import VCharts from 'v-charts'
// import VeLine from 'v-charts/lib/line.common'
// Vue.component("ve-line", VeLine)
// import Vue from 'vue'
// import ECharts from 'vue-echarts' // 在 webpack 环境下指向 components/ECharts.vue

// 手动引入 ECharts 各模块来减小打包体积
// import 'echarts/lib/chart/bar'
// import 'echarts/lib/component/tooltip'

// 如果需要配合 ECharts 扩展使用，只需要直接引入扩展包即可
// 以 ECharts-GL 为例：
// 需要安装依赖：npm install --save echarts-gl，并添加如下引用
// import 'echarts-gl'

// 注册组件后即可使用
// Vue.component('v-chart', ECharts)


// 导入组件
import TreeTable from 'vue-table-with-tree-grid'
// 导入全局样式表
import './assets/css/global.css'
// 导入axios包
import axios from 'axios'

//  配置请求根路径
axios.defaults.baseURL = 'http://127.0.0.1:5000/'
Vue.prototype.$http = axios
Vue.config.productionTip = false

// 注册树形结构为全局可用的组件
Vue.component('tree-table', TreeTable)

Vue.use(VCharts)

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')