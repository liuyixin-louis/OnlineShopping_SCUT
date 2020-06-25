import time


data = {'address': {'id': 1, 'isDefault': True, 'name': 'Exrick', 'mobile': '17621230884', 'address': '四川省成都市武侯区', 'street': '益州大道香月湖7栋188号'},
 'totalPrice': 1, 'expressPrice': 10, 'actualPrice': 11, 
'couponCount': 2, 'coupon': {'id': '', 'title': '', 'discount': 0},
 'productList': [{'checked': 1, 'count': 1, 'id': 8, 'maxNum': 100, 
 'picUrl': 'https://img11.360buyimg.com/n1/s450x450_jfs/t1/62813/33/2131/584186/5d079803E03084b0d/2b4970456b7bf49f.png', 
 'price': 1, 'spec': ' 银色 64GB',
 'title': 'Apple iPhone XS Max (A2104)'}],
 'agree': True, '__webviewId__': 52}


member_id = data['address']['id']
order_sn = time.strftime("%y%m%d%H%M%S")+str(member_id)

order = {
     "order_sn":order_sn,
     "member_id":member_id,
     "total_amount":data['totalPrice'],
     "pay_amount":data['actualPrice'],
     "feight_amount":data['expressPrice'],
     "status":2,
     "receiver_name":data['address']['name']
 }

order_item = [
    {
     "order_sn":order_sn,
     "product_id":d['id'],
     "product_pic":d['picUrl'],
     "product_name":d['title'],
     "product_price":d['price'],
     "product_quantity":d['count'],
     "product_attr":d['spec']
     }
     for d in data['productList']
]