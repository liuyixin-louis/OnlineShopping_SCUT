//app.js
App({
  get_userID:function(){
    return 1;
  },
  onLaunch: function () {
     //查询服务器，对应用户的购物车信息
     var that = this;
     wx.request({
       url: 'http://localhost:5000/query_cart',
       data: {
         //数据urlencode方式编码，变量间用&连接，再post
         'user_id':that.get_userID()
       },
       method: 'POST',
       header:{
         'content-type':'application/x-www-form-urlencoded'
       },
       success: function (res) {
         // console.log(res);
         if (res.data.code == 200) {
          //something to do
          console.log("成功");
          var cartList = res.data.res;
          wx.setStorageSync("cartList", cartList);
          // that.setData({
          //  cartList:res.data.res
          // })
          // wx.setStorageSync("cartList", cartList);
         }
         else{
          //something to do
         }
       },
       fail: function (res) {
         console.log(res);
       }
     });
  },
  globalData: {
    order : [
      {
      id: '1',
      orderSn: '20180320',
      createTime: '2019-08-18 18:35',
      payType: '微信',
      productList: [{
        id: '1',
        picUrl: 'https://yanxuan.nosdn.127.net/1979054e3a1c8409f10191242165e674.png',
        title: '常温纯牛奶 250毫升*12盒*2提',
        specDesc: '纯牛奶 12盒*2提',
        status: 1,
        count: 1,
        price: 88.00
      }],
      totalPrice: 88.00,
      expressPrice: 0.00,
      actualPrice: 88.00,
      orderStatus: 1
    },
    {
      id: '2',
      orderSn: '20180321',
      createTime: '2019-08-18 18:35',
      payType: '微信',
      productList: [{
        id: '2',
        picUrl: 'https://yanxuan.nosdn.127.net/22d0a46bac31ad7f882830e698ed5132.png',
        title: '无损风味 超即溶精品咖啡（24颗入）',
        specDesc: '24颗精品混合装（1-6号）',
        count: 1,
        price: 165.00,
        status: 3
      }],
      totalPrice: 165.00,
      expressPrice: 0.00,
      actualPrice: 165.00,
      orderStatus: 3
    },
    {
      id: '3',
      orderSn: '20180321',
      createTime: '2019-08-18 18:35',
      payType: '微信',
      productList: [{
        id: '3',
        picUrl: 'https://yanxuan.nosdn.127.net/87eb525e1a7998b7a88f45a86b912e01.jpg',
        title: '有道口袋打印机',
        specDesc: '口袋打印机',
        status: 5,
        count: 1,
        price: 239.00
      }, {
        id: '4',
        picUrl: 'https://yanxuan.nosdn.127.net/604941c1a657e49f4114dabb201ab2aa.png',
        title: '智能降温保冷杯',
        specDesc: '帝王黑',
        count: 1,
        price: 159.00,
        status: 5
      }],
      totalPrice: 398.00,
      expressPrice: 0.00,
      actualPrice: 398.00,
      orderStatus: 5
    },
    {
      id: '4',
      orderSn: '20181328',
      createTime: '2019-08-18 18:35',
      payType: '微信',
      productList: [{
        id: '5',
        picUrl: 'https://yanxuan.nosdn.127.net/69a890ff1cfe400c4e2fdaee7d9e598a.png',
        title: '自动喷香机',
        specDesc: '主机+4罐芳香喷雾罐',
        status: 4,
        count: 1,
        price: 99.00
      }],
      totalPrice: 99.00,
      expressPrice: 0.00,
      actualPrice: 99.90,
      orderStatus: 4
    }
    ],
    userInfo: {
      nickName: "Hi，游客",
      username: "点击去登录",
      avatarUrl: "/assets/avatar.png"
    },
    token: "",
  }
})