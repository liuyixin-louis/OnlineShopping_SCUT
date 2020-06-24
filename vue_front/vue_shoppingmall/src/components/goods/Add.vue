<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>商品管理</el-breadcrumb-item>
      <el-breadcrumb-item>添加商品</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图 -->
    <el-card>
      <!-- 提示区域 -->
      <el-alert title="添加商品信息" type="info" center show-icon :closable="false">
      </el-alert>
      <el-form :model="addForm" :rules="addFormRules" ref="addFormRef" label-width="100px" label-position="top">
        <el-form-item label="商品编号" prop="id">
          <el-input v-model="addForm.id"></el-input>
        </el-form-item>
        <el-form-item label="商品图片" prop="pic">
          <el-input v-model="addForm.pic"></el-input>
        </el-form-item>
        <el-form-item label="商品名称" prop="name">
          <el-input v-model="addForm.name"></el-input>
        </el-form-item>
        <el-form-item label="品牌名称" prop="brand_name">
          <el-input v-model="addForm.brand_name"></el-input>
        </el-form-item>
        <el-form-item label="商品价格" prop="price">
          <el-input v-model="addForm.price" type="number"></el-input>
        </el-form-item>
        <el-form-item label="商品货号" prop="product_sn">
          <el-input v-model="addForm.product_sn"></el-input>
        </el-form-item>
        <el-form-item label="商品上架状态" prop="publish_status">
          <el-input v-model="addForm.publish_status" type="number"></el-input>
        </el-form-item>
        <el-form-item label="商品推荐状态" prop="recommand_status">
          <el-input v-model="addForm.recommand_status" type="number"></el-input>
        </el-form-item>
        <el-form-item label="商品新品状态" prop="new_status">
          <el-input v-model="addForm.new_status" type="number"></el-input>
        </el-form-item>
        <el-form-item label="商品排序" prop="sort">
          <el-input v-model="addForm.sort"></el-input>
        </el-form-item>
        <el-form-item label="商品销量" prop="sale">
          <el-input v-model="addForm.sale" type="number"></el-input>
        </el-form-item>
        <!-- 添加商品按钮 -->
        <el-button type="primary" class="btnAdd" @click="add">添加商品</el-button>
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
        pic: '',
        name: '',
        brand_name: '',
        price: 0,
        product_sn: '',
        publish_status: 0,
        recommand_status: 0,
        new_status: 0,
        sort: '',
        sale: 0,
        shop_id:1
      },
      addFormRules: {
        id: [{
          required: true, message: '请输入商品编号', trigger: 'blur'
        }],
        pic: [{
          required: true, message: '请输入商品图片', trigger: 'blur'
        }],
        name: [{
          required: true, message: '请输入商品名称', trigger: 'blur'
        }],
        brand_name: [{
          required: true, message: '请输入品牌名称', trigger: 'blur'
        }],
        price: [{
          required: true, message: '请输入商品价格', trigger: 'blur'
        }],
        product_sn: [{
          required: true, message: '请输入商品货号', trigger: 'blur'
        }],
        publish_status: [{
          required: true, message: '请输入商品上架状态', trigger: 'blur'
        }],
        recommand_status: [{
          required: true, message: '请输入商品推荐状态', trigger: 'blur'
        }],
        new_status: [{
          required: true, message: '请输入商品新品状态', trigger: 'blur'
        }],
        sort: [{
          required: true, message: '请输入商品排序', trigger: 'blur'
        }],
        sale: [{
          required: true, message: '请输入商品销量', trigger: 'blur'
        }],
        shop_id: [{
          required: true, message: '请输入商品销量', trigger: 'blur'
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
        this.$http.post('admin/products/', qs.stringify(this.addForm)).then(function(res){
                    // document.write(res.body);    
                    console.log(res);
                    if(res.data.code=="sucess"){
                      alert("添加商品成功！");
                      that.$router.push({
                      path:'/lists'
                      })
                    }
                },function(){
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
