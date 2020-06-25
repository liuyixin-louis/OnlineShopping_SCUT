<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>数据统计</el-breadcrumb-item>
      <el-breadcrumb-item>产品销量排名</el-breadcrumb-item>
    </el-breadcrumb>

    <!-- 卡片视图区域 -->
    <el-card>
      <!-- 用户列表区域 -->
      <el-table :data="productranklist" style="width: 100%" border>
        <el-table-column type="index">
        </el-table-column>
        <el-table-column prop="id" label="商品编号">
        </el-table-column>
        <el-table-column prop="name" label="商品名称">
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
      productranklist: []
    }
  },
  created () {
    this.getProductrank()
  },
  methods: {
    async getProductrank () {
      const { data: res } = await this.$http.get('rank/product')
      console.log(res)
      this.productranklist = res.rank_res
    }
  }
}
</script>
<style>
</style>