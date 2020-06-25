<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>数据统计</el-breadcrumb-item>
      <el-breadcrumb-item>商家销量排名</el-breadcrumb-item>
    </el-breadcrumb>

    <!-- 卡片视图区域 -->
    <el-card>
      <!-- 用户列表区域 -->
      <el-table :data="shopranklist" style="width: 100%" border>
        <el-table-column type="index">
        </el-table-column>
        <el-table-column prop="id" label="商家编号">
        </el-table-column>
        <el-table-column prop="shopName" label="商家名称">
        </el-table-column>
        <el-table-column prop="sale" label="销量">
        </el-table-column>
      </el-table>
    </el-card>

  </div>
</template>

<script>
export default {
  data: function () {
    return {
      shopranklist: []
    }
  },
  created () {
    this.getShoprank()
  },
  methods: {
    async getShoprank () {
      const { data: res } = await this.$http.get('rank/shop')
      console.log(res)
      this.shopranklist = res.rank_res
    }
  }
}
</script>
<style>
</style>