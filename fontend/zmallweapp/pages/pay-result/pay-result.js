// pages/pay-result/pay-result.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    status: 1,
    point: 0
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    if(options.actualPrice){
      this.setData({
        point: options.actualPrice
      })
    }
    //订单列表添加
    var neworder = {
      id: '5',
      orderSn: '20200612',
      createTime: '2020-08-18 18:35',
      payType: '微信',
      productList: [{
        id: '1',
        picUrl: 'https://img11.360buyimg.com/n1/s450x450_jfs/t1/62813/33/2131/584186/5d079803E03084b0d/2b4970456b7bf49f.png',
        title: 'Apple iPhone XS Max (A2104)',
        specDesc: '银色 256GB',
        status: 2,
        count: 1,
        price: 4999.00
      }],
      totalPrice: 4999.00,
      expressPrice: 0.00,
      actualPrice: 2.00,
      orderStatus: 2
    }
    let order = getApp().globalData.order;
    order.push(neworder);

    //删除购物车
    let cartList = wx.getStorageSync("cartList");
    var r = cartList.pop();
    console.log(r);
    wx.setStorageSync("cartList", cartList);
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  showOrder: function(){
    
    wx.navigateTo({
      url: '/pages/ucenter/order/order',
    })
  },
  hangOut: function () {
    wx.switchTab({
      url: '/pages/index/index',
    })
  },
})