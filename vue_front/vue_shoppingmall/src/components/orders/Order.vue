<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>订单管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户订单</el-breadcrumb-item>
    </el-breadcrumb>

    <!-- 卡片视图区域 -->
    <el-card>
      <el-row :gutter="20">
        <el-col :span="7">
          <!-- 搜索区域 -->
          <el-input placeholder="请输入内容" v-model="querystr" clearable>
            <el-button slot="append" icon="el-icon-search" @click="fillterOrderList"></el-button>
          </el-input>
        </el-col>
        <el-col :span="5">
          <el-button type="primary" @click="goAddpage">添加订单</el-button>
        </el-col>
      </el-row>
      <!-- 用户列表区域 -->
      <el-table :data="tempOrderList" style="width: 100%" border>
        <el-table-column type="index">
        </el-table-column>
        <el-table-column prop="id" label="商品编号">
        </el-table-column>
        <el-table-column prop="name" label="商品名称" width="120">
        </el-table-column>
        <el-table-column prop="brand_name" label="品牌">
        </el-table-column>
        <el-table-column prop="price" label="价格">
        </el-table-column>
        <el-table-column prop="sale" label="销量">
        </el-table-column>
        <el-table-column prop="shop_id" label="商店ID">
        </el-table-column>
        <el-table-column label="操作">
          <!-- 操作 -->
          <template slot-scope="scope">
            <el-button type="primary" style="float: right;" icon="el-icon-edit" size="mini"
              @click="showEditDialog(scope.row.id)">编辑
            </el-button>
            <el-button type="danger" style="float: right;" icon="el-icon-delete" size="mini"
              @click="removeById(scope.row.id)">删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <!-- 修改用户对话框 -->
      <el-dialog title="修改商品" :visible.sync="editDialogVisible" width="50%" @click="editDialogClosed">
        <el-form :model="editForm" :rules="editFormRules" ref="editFormRef" label-width="70px">
          <el-form-item label="商品编号">
            <el-input v-model="editForm.id" disabled></el-input>
          </el-form-item>
          <el-form-item label="商品名称">
            <el-input v-model="editForm.name" disabled></el-input>
          </el-form-item>
          <el-form-item label="品牌">
            <el-input v-model="editForm.brand_name" disabled></el-input>
          </el-form-item>
          <el-form-item label="价格" prop="price">
            <el-input v-model="editForm.price"></el-input>
          </el-form-item>
          <el-form-item label="销量" prop="sale">
            <el-input v-model="editForm.sale"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="editDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="editUserInfo">确 定</el-button>
        </span>
      </el-dialog>

    </el-card>

  </div>
</template>

<script>
// 导入qs包
import qs from 'qs'
export default {
  data () {
    return {
      querystr: "",
      queryInfo: {
        query: '',
        pagenum: 1,
        pagesize: 10
      },
      goodslist: [],
      total: 0,
      editDialogVisible: false, // 控制修改商品对话框的显示与隐藏
      editForm: {}, // 保存查询到的用户信息
      // 修改表单的验证规则对象,但没有验证两者必须为数值
      editFormRules: {
        price: [{
          required: true, message: '请输入商品价格', trigger: 'blur'
        }],
        sale: [{
          required: true, message: '请输入商品销量', trigger: 'blur'
        }
        ]
      },
      tempGoodList: []
    }
  },
  created () {
    this.getGoodsList()
  },
  methods: {
    async getGoodsList () {
      const { data: res } = await this.$http.get('admin/products')
      // console.log('展示' + res.code)
      console.log(res)
      // console.log(res.res)
      //  console.log(res.all_users_info)
      this.goodslist = res.res;
      this.tempGoodList = res.res;
      this.total = res.res.length
    },
    handleSizeChange (newSize) {
      this.queryInfo.pagesize = newSize
      this.getGoodsList()
    },
    handleCurrentChange (newPage) {
      this.queryInfo.pagenum = newPage
      this.getGoodsList()
    },
    async removeById (id) {
      const { data: res } = await this.$http.delete(`admin/products/${id}`)
      this.getGoodsList()
      console.log(res)
    },
    goAddpage () {
      this.$router.push('/add')
    },
    // 展示修改对话框
    async showEditDialog (id) {
      // 未完成/admin/products/<int:product_id>的GET接口
      //  const { data: res } = await this.$http.get(`admin/products/${id}`)
      //  console.log(res)
      //  this.editForm = res.data
      console.log(this.goodslist)
      console.log(this.total)
      for (var i = 0; i < this.total; i++) {
        if (this.goodslist[i].id === id) { this.editForm = this.goodslist[i] }
      }
      this.editDialogVisible = true
    },
    // 监听修改用户对话框的关闭事件
    editDialogClosed () {
      this.$refs.editFormRef.resetFields()
    },
    // 修改并提交
    editUserInfo () {
      this.$refs.editFormRef.validate(async valid => {
        if (!valid) {
          return this.$message.error('请填写必要的表单项！')
        }
        console.log(this.editForm)
        const { data: res } = await this.$http.put('admin/products/' + this.editForm.id, qs.stringify(this.editForm))
        //  const { data: res } = await this.$http.post('admin/products/', qs.stringify(this.editForm))
        console.log(res)
        this.editDialogVisible = false
        this.getGoodsList()
        this.$message.success('更新用户信息成功！')
      })
    },
    fillterGoodList () {
      console.log(this.querystr);
      var query_str = this.querystr;
      if (query_str != "") {
        var t = [];
        for (const gi of this.goodslist) {
          // console.log(v);
          if (gi.name.search(query_str) != -1) {
            t.push(gi);
          };
        }
        this.tempGoodList = t;
      } else {
        this.tempGoodList = this.goodslist;
      };

    }
  }
}
</script>
<style lang="less" scoped>
</style>
