<template>
  <el-container class="home-container">
    <!-- 头部区域 -->
    <el-header>
      <div>
        <img src="../assets/logo3.png" alt="">
        <span>电商后台管理系统</span>
      </div>
      <el-button type="info">退出</el-button>
    </el-header>
    <!-- 页面主体区域 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside :width="isCollapse ? '64px' : '200px'">
        <div class="toggle-button" @click="toggleCollapse">|||</div>
        <!-- 侧边栏菜单区 -->
        <el-menu background-color="#333744" text-color="#fff" active-text-color="#ffd04b" unique-opened
          :collapse="isCollapse" :collapse-transition="false" router default-active="activePath">
          <!-- 一级菜单 -->
          <el-submenu index="1">
            <!-- 一级菜单模版区域 -->
            <template slot="title">
              <!-- 图标 -->
              <i class="el-icon-s-custom"></i>
              <!-- 文本 -->
              <span>用户管理</span>
            </template>

            <!-- 二级菜单 -->
            <el-menu-item index="users" @click="saveNavState('/users')">
              <!-- 一级菜单模版区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-help"></i>
                <!-- 文本 -->
                <span>用户基本信息</span>
              </template>
            </el-menu-item>

            <el-menu-item index="shops" @click="saveNavState('/shops')">
              <!-- 一级菜单模版区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-help"></i>
                <!-- 文本 -->
                <span>商家信息管理</span>
              </template>
            </el-menu-item>
          </el-submenu>

          <!-- 一级菜单 -->
          <el-submenu index="3">
            <!-- 一级菜单模版区域 -->
            <template slot="title">
              <!-- 图标 -->
              <i class="el-icon-shopping-cart-1"></i>
              <!-- 文本 -->
              <span>商品管理</span>
            </template>
            <!-- 二级菜单 -->
            <el-menu-item index="lists" @click="saveNavState('/lists')">
              <!-- 一级菜单模版区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-help"></i>
                <!-- 文本 -->
                <span>商品列表</span>
              </template>
            </el-menu-item>

            <!-- 二级菜单 -->
            <el-menu-item index="attribute" @click="saveNavState('/attribute')">
              <!-- 一级菜单模版区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-help"></i>
                <!-- 文本 -->
                <span>属性管理</span>
              </template>
            </el-menu-item>

            <!-- 二级菜单 -->
            <el-menu-item index="categories" @click="saveNavState('/categories')">
              <!-- 一级菜单模版区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-help"></i>
                <!-- 文本 -->
                <span>商品分类</span>
              </template>
            </el-menu-item>

            <!-- 二级菜单 -->
            <el-menu-item index="stock" @click="saveNavState('/stock')">
              <!-- 一级菜单模版区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-help"></i>
                <!-- 文本 -->
                <span>库存管理</span>
              </template>
            </el-menu-item>

          </el-submenu>

          <!-- 一级菜单 -->
          <el-submenu index="4">
            <!-- 一级菜单模版区域 -->
            <template slot="title">
              <!-- 图标 -->
              <i class="el-icon-s-order"></i>
              <!-- 文本 -->
              <span>订单管理</span>
            </template>

            <!-- 二级菜单 -->
            <el-menu-item index="orders" @click="saveNavState('/orders')">
              <!-- 一级菜单模版区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-help"></i>
                <!-- 文本 -->
                <span>用户订单</span>
              </template>
            </el-menu-item>

          </el-submenu>

          <!-- 一级菜单 -->
          <el-submenu index="5">
            <!-- 一级菜单模版区域 -->
            <template slot="title">
              <!-- 图标 -->
              <i class="el-icon-s-platform"></i>
              <!-- 文本 -->
              <span>数据统计</span>
            </template>

            <!-- 二级菜单 -->
            <el-menu-item index="user_info" @click="saveNavState('/user_info')">
              <!-- 一级菜单模版区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-help"></i>
                <!-- 文本 -->
                <span>用户统计信息</span>
              </template>
            </el-menu-item>

            <el-menu-item index="statistics" @click="saveNavState('/statistics')">
              <!-- 一级菜单模版区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-help"></i>
                <!-- 文本 -->
                <span>平台统计信息</span>
              </template>
            </el-menu-item>

            <!-- 二级菜单 -->
            <el-menu-item index="shoprank" @click="saveNavState('/shoprank')">
              <!-- 一级菜单模版区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-help"></i>
                <!-- 文本 -->
                <span>商家销量排名</span>
              </template>
            </el-menu-item>

            <!-- 二级菜单 -->
            <el-menu-item index="productrank" @click="saveNavState('/productrank')">
              <!-- 一级菜单模版区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-s-help"></i>
                <!-- 文本 -->
                <span>产品销量排名</span>
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!-- 右侧内容主体 -->
      <el-main>
        <!-- 路由占位符 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      // 是否折叠
      isCollapse: false,

      // 被激活的链接
      activePath: ''
    }
  },
  created () {
    this.activePath = window.sessionStorage.getItem('activePath')
  },
  methods: {
    /*
    logout () {
      window.sessionStorage.clear()
      this.$router.push('/login')
    }
    */
    // 点击按钮切换菜单的折叠展开
    toggleCollapse () {
      this.isCollapse = !this.isCollapse
    },
    saveNavState (activePath) {
      window.sessionStorage.setItem('activePath', activePath)
      this.activePath = activePath
    }
  }
}
</script>

<style lang="less" scoped>
.el-header {
  background-color: #373d41;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-content: center;
  color: #fff;
  font-size: 20px;
  div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px;
    }
  }
  img {
    height: 75px;
    width: 100px;
    border-radius: 50%;
    background-color: #eee;
  }
}
.el-aside {
  background-color: #333744;
  .el-menu {
    border-right: 0;
  }
}
.el-main {
  background-color: #eaedf1;
}
.home-container {
  height: 100%;
}
.toggle-button {
  background-color: #4a5064;
  font-size: 10px;
  line-height: 24px;
  color: #fff;
  text-align: center;
  letter-spacing: 0.2em;
}
</style>
