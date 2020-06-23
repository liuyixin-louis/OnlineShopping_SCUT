<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>商品管理</el-breadcrumb-item>
      <el-breadcrumb-item>商品分类</el-breadcrumb-item>
    </el-breadcrumb>

    <!-- 卡片视图区域 -->
    <el-card>
      <el-row>
        <el-col>
          <el-button type="primary">添加分类</el-button>
        </el-col>
      </el-row>
    </el-card>

    <!-- 表格-->
    <tree-table :data="catelist" :columns="columns" :selection-type="false" :expand-type="false" show-index border>
      <!-- 排序 -->
      <template slot="order" slot-scope="scope">
        <el-tag size="mini" v-if="scope.row.cat_level==0">一级</el-tag>
        <el-tag type="success" size="mini" v-else-if="scope.row.cat_level==1">二级</el-tag>
        <el-tag type="warning" size="mini" v-else>三级</el-tag>
      </template>
      <!-- 操作 -->
      <template slot="opt">
        <el-button type="primary" icon="el-icon-edit" size="mini">编辑</el-button>
        <el-button type="danger" icon="el-icon-delete" size="mini">删除</el-button>
      </template>
    </tree-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      columns: [{
        label: '分类名称',
        prop: 'title'
      },
      {
        label: '操作',
        type: 'template',
        template: 'opt'
      }],
      catelist: [],
      total: 0
    }
  },
  created () { this.getCateList() },
  methods: {
    async getCateList () {
      const { data: res } = await this.$http.get('get_category')
      console.log(res)
      console.log(res.res)
      this.catelist = res.res
      this.total = res.res.length
      //  this.total = res.res.length
    }
  }
}

</script>
<style lang="less" scoped>
</style>
