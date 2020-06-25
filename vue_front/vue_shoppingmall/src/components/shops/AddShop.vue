<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>商品管理</el-breadcrumb-item>
      <el-breadcrumb-item>添加商家</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图 -->
    <el-card>
      <!-- 提示区域 -->
      <el-alert title="添加商家信息" type="info" center show-icon :closable="false">
      </el-alert>
      <el-form :model="addForm" :rules="addFormRules" ref="addFormRef" label-width="100px" label-position="top">
        <el-form-item label="商家编号" prop="id">
          <el-input v-model="addForm.id"></el-input>
        </el-form-item>
        <el-form-item label="商家名称" prop="shopName">
          <el-input v-model="addForm.shopName"></el-input>
        </el-form-item>
        <el-form-item label="商品数" prop="product_number">
          <el-input v-model="addForm.product_number"></el-input>
        </el-form-item>
        <el-form-item label="有效与否" prop="is_valid">
          <el-input v-model="addForm.is_valid"></el-input>
        </el-form-item>
        <el-form-item label="销量" prop="sale">
          <el-input v-model="addForm.price" type="sale"></el-input>
        </el-form-item>

        <!-- 添加商品按钮 -->
        <el-button type="primary" class="btnAdd" @click="add">添加商家</el-button>
      </el-form>
    </el-card>
  </div>
</template>

<script>
// 导入qs包
import qs from 'qs'
export default {
  data () {
    return {
      // 添加商品表单对象
      addForm: {
        id: '',
        shopName: '',
        product_number: 0,
        is_valid: 0,
        sale: 0
      },
      addFormRules: {
        id: [{
          required: true, message: '请输入商家编号', trigger: 'blur'
        }],
        shopName: [{
          required: true, message: '请输入商家名称', trigger: 'blur'
        }],
        product_number: [{
          required: true, message: '请输入商品数', trigger: 'blur'
        }],
        is_valid: [{
          required: true, message: '请输入商家状态，0为无效，1为有效', trigger: 'blur'
        }],
        sale: [{
          required: true, message: '请输入商家销量', trigger: 'blur'
        }]
      },
      catelist: []
    }
  },
  created () { this.getCateList() },
  methods: {
    // 获取所有商品分类数据
    async getCateList () {
      const { data: res } = await this.$http.get('get_category')
      this.catelist = res.res
      console.log(this.catelist)
    },
    add () {
      this.$refs.addFormRef.validate(async valid => {
        if (!valid) {
          return this.$message.error('请填写必要的表单项！')
        }
        //  const form = _.cloneDeep(this.addForm)
        console.log(this.addForm)
        // const result = await this.$http.post('admin/products/', qs.stringify(this.addForm))
        // console.log(JSON.parse(result.request.response))
        // this.$http.post('admin/products/', qs.stringify(this.addForm)).then(func)

        var that = this;
        this.$http.post('admin/products/', qs.stringify(this.addForm)).then(function (res) {
          // document.write(res.body);    
          console.log(res);
          if (res.data.code == "sucess") {
            alert("添加商品成功！");
            that.$router.push({
              path: '/lists'
            })
          }
        }, function () {
          alert("添加商品失败！");
          console.log('请求失败处理');
        });


      })
    }
  }
}

</script>
<style lang="less" scoped>
</style>
