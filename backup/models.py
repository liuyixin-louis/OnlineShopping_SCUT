# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, DateTime, ForeignKey, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, SMALLINT, TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PmsBrand(Base):
    __tablename__ = 'pms_brand'
    __table_args__ = {'comment': '品牌表'}

    id = Column(BIGINT(20), primary_key=True)
    name = Column(VARCHAR(64))
    first_letter = Column(VARCHAR(8), comment='首字母')
    sort = Column(INTEGER(11))
    factory_status = Column(INTEGER(11), comment='是否为品牌制造商：0->不是；1->是')
    show_status = Column(INTEGER(11))
    product_count = Column(INTEGER(11), comment='产品数量')
    product_comment_count = Column(INTEGER(11), comment='产品评论数量')
    logo = Column(VARCHAR(255), comment='品牌logo')
    description = Column(VARCHAR(255), comment='介绍')


class PmsFeightTemplate(Base):
    __tablename__ = 'pms_feight_template'
    __table_args__ = {'comment': '运费模版'}

    id = Column(BIGINT(20), primary_key=True)
    name = Column(VARCHAR(64))
    charge_type = Column(INTEGER(11), comment='计费类型:0->按重量；1->按件数')
    first_weight = Column(DECIMAL(10, 2), nullable=False, comment='首重kg')
    first_fee = Column(DECIMAL(10, 2), comment='首费（元）')
    continue_weight = Column(DECIMAL(10, 2))
    continme_fee = Column(DECIMAL(10, 2))
    dest = Column(VARCHAR(255), comment='目的地（省、市）')


class PmsPlatformStatistic(Base):
    __tablename__ = 'pms_platform_statistics'

    id = Column(INTEGER(11), primary_key=True)
    datetime = Column(DateTime)
    tody_sale = Column(INTEGER(8))


class PmsProductAttributeCategory(Base):
    __tablename__ = 'pms_product_attribute_category'
    __table_args__ = {'comment': '产品属性分类表'}

    id = Column(BIGINT(20), primary_key=True)
    name = Column(VARCHAR(64))
    attribute_count = Column(INTEGER(11), server_default=text("'0'"), comment='属性数量')
    param_count = Column(INTEGER(11), server_default=text("'0'"), comment='参数数量')


class PmsProductCategory(Base):
    __tablename__ = 'pms_product_category'
    __table_args__ = {'comment': '产品分类'}

    id = Column(BIGINT(20), primary_key=True)
    parent_id = Column(BIGINT(20), comment='上机分类的编号：0表示一级分类')
    name = Column(VARCHAR(64))
    level = Column(INTEGER(11), comment='分类级别：0->1级；1->2级')
    product_count = Column(INTEGER(11))
    product_unit = Column(VARCHAR(64))
    nav_status = Column(INTEGER(11), comment='是否显示在前台导航栏：0->不显示；1->显示')
    show_status = Column(INTEGER(11), comment='显示在前台的情况下，控制显示状态：0->不显示；1->显示')
    sort = Column(INTEGER(11))
    icon = Column(VARCHAR(255), comment='图标')
    keywords = Column(VARCHAR(255))
    description = Column(TEXT, comment='描述')


class PmsShop(Base):
    __tablename__ = 'pms_shop'

    sale = Column(INTEGER(11))
    id = Column(BIGINT(20), primary_key=True)
    shopName = Column(VARCHAR(255))
    product_number = Column(INTEGER(11))
    is_valid = Column(SMALLINT(6))


class PmsShopsale(Base):
    __tablename__ = 'pms_shopsale'

    time = Column(DateTime, primary_key=True, nullable=False)
    dailysale = Column(INTEGER(11))
    id = Column(BIGINT(20), primary_key=True, nullable=False)


class UmsAdmin(Base):
    __tablename__ = 'ums_admin'
    __table_args__ = {'comment': '后台用户表'}

    id = Column(BIGINT(20), primary_key=True)
    username = Column(VARCHAR(64))
    password = Column(VARCHAR(64))
    icon = Column(VARCHAR(500), comment='头像')
    email = Column(VARCHAR(100), comment='邮箱')
    nick_name = Column(VARCHAR(200), comment='昵称')
    note = Column(VARCHAR(500), comment='备注信息')
    create_time = Column(DateTime, comment='创建时间')
    login_time = Column(DateTime, comment='最后登录时间')
    status = Column(INTEGER(11), server_default=text("'1'"), comment='帐号启用状态：0->禁用；1->启用')


class UmsMember(Base):
    __tablename__ = 'ums_member'
    __table_args__ = {'comment': '会员表'}

    id = Column(BIGINT(20), primary_key=True)
    member_level_id = Column(BIGINT(20))
    username = Column(VARCHAR(64), unique=True, comment='用户名')
    password = Column(VARCHAR(64), comment='密码')
    nickname = Column(VARCHAR(64), comment='昵称')
    phone = Column(VARCHAR(64), unique=True, comment='手机号码')
    status = Column(INTEGER(11), comment='帐号启用状态:0->禁用；1->启用')
    create_time = Column(DateTime, comment='注册时间')
    icon = Column(VARCHAR(500), comment='头像')
    gender = Column(INTEGER(11), comment='性别：0->未知；1->男；2->女')
    birthday = Column(Date, comment='生日')
    city = Column(VARCHAR(64), comment='所做城市')
    job = Column(VARCHAR(100), comment='职业')
    personalized_signature = Column(VARCHAR(200), comment='个性签名')
    source_type = Column(INTEGER(11), comment='用户来源')


class OmsOrder(Base):
    __tablename__ = 'oms_order'
    __table_args__ = {'comment': '订单表'}

    id = Column(BIGINT(20), primary_key=True, comment='订单id')
    member_id = Column(ForeignKey('ums_member.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    order_sn = Column(VARCHAR(64), comment='订单编号')
    create_time = Column(DateTime, comment='提交时间')
    member_username = Column(VARCHAR(64), comment='用户帐号')
    total_amount = Column(DECIMAL(10, 2), comment='订单总金额')
    pay_amount = Column(DECIMAL(10, 2), comment='应付金额（实际支付金额）')
    freight_amount = Column(DECIMAL(10, 2), comment='运费金额')
    pay_type = Column(INTEGER(11), comment='支付方式：0->未支付；1->支付宝；2->微信')
    source_type = Column(INTEGER(11), comment='订单来源：0->PC订单；1->app订单')
    status = Column(INTEGER(11), comment='订单状态：1->待付款；2->待发货；3->已发货；4->待评价；5->已评价；6->已关闭')
    delivery_company = Column(VARCHAR(64), comment='物流公司(配送方式)')
    delivery_sn = Column(VARCHAR(64), comment='物流单号')
    receiver_name = Column(VARCHAR(100), nullable=False, comment='收货人姓名')
    receiver_phone = Column(VARCHAR(32), nullable=False, comment='收货人电话')
    receiver_post_code = Column(VARCHAR(32), comment='收货人邮编')
    receiver_province = Column(VARCHAR(32), comment='省份/直辖市')
    receiver_city = Column(VARCHAR(32), comment='城市')
    receiver_region = Column(VARCHAR(32), comment='区')
    receiver_detail_address = Column(VARCHAR(200), comment='详细地址')
    note = Column(VARCHAR(500), comment='订单备注')
    confirm_status = Column(INTEGER(11), comment='确认收货状态：0->未确认；1->已确认')
    delete_status = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='删除状态：0->未删除；1->已删除')
    payment_time = Column(DateTime, comment='支付时间')
    delivery_time = Column(DateTime, comment='发货时间')
    receive_time = Column(DateTime, comment='确认收货时间')
    comment_time = Column(DateTime, comment='评价时间')

    member = relationship('UmsMember')


class PmsProduct(Base):
    __tablename__ = 'pms_product'
    __table_args__ = {'comment': '商品信息'}

    id = Column(BIGINT(20), primary_key=True)
    brand_id = Column(ForeignKey('pms_brand.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_category_id = Column(ForeignKey('pms_product_category.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    feight_template_id = Column(ForeignKey('pms_feight_template.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_attribute_category_id = Column(ForeignKey('pms_product_attribute_category.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    name = Column(VARCHAR(64), nullable=False)
    pic = Column(VARCHAR(255))
    product_sn = Column(VARCHAR(64), nullable=False, comment='货号')
    delete_status = Column(INTEGER(11), comment='删除状态：0->未删除；1->已删除')
    publish_status = Column(INTEGER(11), comment='上架状态：0->下架；1->上架')
    new_status = Column(INTEGER(11), comment='新品状态:0->不是新品；1->新品')
    recommand_status = Column(INTEGER(11), comment='推荐状态；0->不推荐；1->推荐')
    verify_status = Column(INTEGER(11), comment='审核状态：0->未审核；1->审核通过')
    sort = Column(INTEGER(11), comment='排序')
    sale = Column(INTEGER(11), comment='销量')
    price = Column(DECIMAL(10, 2))
    sub_title = Column(VARCHAR(255), comment='副标题')
    description = Column(TEXT, comment='商品描述')
    original_price = Column(DECIMAL(10, 2), comment='市场价')
    stock = Column(INTEGER(11), comment='库存')
    low_stock = Column(INTEGER(11), comment='库存预警值')
    unit = Column(VARCHAR(16), comment='单位')
    weight = Column(DECIMAL(10, 2), comment='商品重量，默认为克')
    preview_status = Column(INTEGER(11), comment='是否为预告商品：0->不是；1->是')
    service_ids = Column(VARCHAR(64), comment='以逗号分割的产品服务：1->无忧退货；2->快速退款；3->免费包邮')
    keywords = Column(VARCHAR(255))
    note = Column(VARCHAR(255))
    album_pics = Column(VARCHAR(255), comment='画册图片，连产品图片限制为5张，以逗号分割')
    detail_title = Column(VARCHAR(255))
    detail_desc = Column(TEXT)
    detail_html = Column(TEXT, comment='产品详情网页内容')
    detail_mobile_html = Column(TEXT, comment='移动端网页详情')
    brand_name = Column(VARCHAR(255), comment='品牌名称')
    product_category_name = Column(VARCHAR(255), comment='商品分类名称')
    shop_id = Column(ForeignKey('pms_shop.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    brand = relationship('PmsBrand')
    feight_template = relationship('PmsFeightTemplate')
    product_attribute_category = relationship('PmsProductAttributeCategory')
    product_category = relationship('PmsProductCategory')
    shop = relationship('PmsShop')


class PmsProductAttribute(Base):
    __tablename__ = 'pms_product_attribute'
    __table_args__ = {'comment': '商品属性参数表'}

    id = Column(BIGINT(20), primary_key=True)
    product_attribute_category_id = Column(ForeignKey('pms_product_attribute_category.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    name = Column(VARCHAR(64))
    select_type = Column(INTEGER(11), comment='属性选择类型：0->唯一；1->单选；2->多选')
    input_type = Column(INTEGER(11), comment='属性录入方式：0->手工录入；1->从列表中选取')
    input_list = Column(VARCHAR(255), comment='可选值列表，以逗号隔开')
    sort = Column(INTEGER(11), comment='排序字段：最高的可以单独上传图片')
    filter_type = Column(INTEGER(11), comment='分类筛选样式：1->普通；1->颜色')
    search_type = Column(INTEGER(11), comment='检索类型；0->不需要进行检索；1->关键字检索；2->范围检索')
    related_status = Column(INTEGER(11), comment='相同属性产品是否关联；0->不关联；1->关联')
    hand_add_status = Column(INTEGER(11), comment='是否支持手动新增；0->不支持；1->支持')
    type = Column(INTEGER(11), comment='属性的类型；0->规格；1->参数')

    product_attribute_category = relationship('PmsProductAttributeCategory')


class UmsMemberReceiveAddres(Base):
    __tablename__ = 'ums_member_receive_address'
    __table_args__ = {'comment': '会员收货地址表'}

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(ForeignKey('ums_member.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    name = Column(VARCHAR(100), comment='收货人名称')
    phone_number = Column(VARCHAR(64))
    default_status = Column(SMALLINT(6), comment='是否为默认')
    post_code = Column(VARCHAR(100), comment='邮政编码')
    province = Column(VARCHAR(100), comment='省份/直辖市')
    city = Column(VARCHAR(100), comment='城市')
    region = Column(VARCHAR(100), comment='区')
    detail_address = Column(VARCHAR(128), comment='详细地址(街道)')

    member = relationship('UmsMember')


class UmsMemberStatisticsInfo(Base):
    __tablename__ = 'ums_member_statistics_info'
    __table_args__ = {'comment': '会员统计信息'}

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(ForeignKey('ums_member.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    consume_amount = Column(DECIMAL(10, 2), comment='累计消费金额')
    order_count = Column(INTEGER(11), comment='订单数量')
    comment_count = Column(INTEGER(11), comment='评价数')
    return_order_count = Column(INTEGER(11), comment='退货数量')
    login_count = Column(INTEGER(11), comment='登录次数')
    attend_count = Column(INTEGER(11), comment='关注数量')
    fans_count = Column(INTEGER(11), comment='粉丝数量')
    recent_order_time = Column(DateTime, comment='最后一次下订单时间')

    member = relationship('UmsMember')


class OmsCartItem(Base):
    __tablename__ = 'oms_cart_item'
    __table_args__ = {'comment': '购物车表'}

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(ForeignKey('pms_product.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_sku_id = Column(BIGINT(20))
    member_id = Column(ForeignKey('ums_member.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    quantity = Column(INTEGER(11), comment='购买数量')
    price = Column(DECIMAL(10, 2), comment='添加到购物车的价格')
    product_pic = Column(VARCHAR(1000), comment='商品主图')
    product_name = Column(VARCHAR(500), comment='商品名称')
    product_sub_title = Column(VARCHAR(500), comment='商品副标题（卖点）')
    product_sku_code = Column(VARCHAR(200), comment='商品sku条码')
    member_nickname = Column(VARCHAR(500), comment='会员昵称')
    create_date = Column(DateTime, comment='创建时间')
    modify_date = Column(DateTime, comment='修改时间')
    delete_status = Column(INTEGER(11), server_default=text("'0'"), comment='是否删除')
    product_category_id = Column(ForeignKey('pms_product_category.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='商品分类')
    product_brand = Column(ForeignKey('pms_brand.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_sn = Column(VARCHAR(200))
    product_attr = Column(VARCHAR(500), comment='商品销售属性:[{"key":"颜色","value":"颜色"},{"key":"容量","value":"4G"}]')
    max_number = Column(INTEGER(11))
    checked = Column(SMALLINT(1))

    member = relationship('UmsMember')
    pms_brand = relationship('PmsBrand')
    product_category = relationship('PmsProductCategory')
    product = relationship('PmsProduct')


class OmsOrderItem(Base):
    __tablename__ = 'oms_order_item'
    __table_args__ = {'comment': '订单中所包含的商品'}

    id = Column(BIGINT(20), primary_key=True)
    order_id = Column(ForeignKey('oms_order.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='订单id')
    order_sn = Column(VARCHAR(64), comment='订单编号')
    product_id = Column(BIGINT(20))
    product_pic = Column(VARCHAR(500))
    product_name = Column(VARCHAR(200))
    product_brand = Column(VARCHAR(200))
    product_sn = Column(VARCHAR(64))
    product_price = Column(DECIMAL(10, 2), comment='销售价格')
    product_quantity = Column(INTEGER(11), comment='购买数量')
    product_sku_id = Column(BIGINT(20), comment='商品sku编号')
    product_sku_code = Column(VARCHAR(50), comment='商品sku条码')
    product_category_id = Column(BIGINT(20), comment='商品分类id')
    product_attr = Column(VARCHAR(500), comment='商品销售属性:[{"key":"颜色","value":"颜色"},{"key":"容量","value":"4G"}]')

    order = relationship('OmsOrder')


class PmsComment(Base):
    __tablename__ = 'pms_comment'
    __table_args__ = {'comment': '商品评价表'}

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(ForeignKey('pms_product.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    member_nick_name = Column(VARCHAR(255))
    product_name = Column(VARCHAR(255))
    star = Column(INTEGER(11), comment='评价星数：0->5')
    create_time = Column(DateTime)
    show_status = Column(INTEGER(11))
    product_attribute = Column(VARCHAR(255), comment='购买时的商品属性')
    collect_count = Column(INTEGER(11))
    read_count = Column(INTEGER(11))
    content = Column(TEXT)
    pics = Column(VARCHAR(1000), comment='上传图片地址，以逗号隔开')
    member_icon = Column(VARCHAR(255), comment='评论用户头像')
    member_id = Column(ForeignKey('ums_member.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    member = relationship('UmsMember')
    product = relationship('PmsProduct')


class PmsProductAttributeValue(Base):
    __tablename__ = 'pms_product_attribute_value'
    __table_args__ = {'comment': '存储产品参数信息的表'}

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(ForeignKey('pms_product.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_attribute_id = Column(ForeignKey('pms_product_attribute.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    value = Column(VARCHAR(64), nullable=False, comment='手动添加规格或参数的值，参数单值，规格有多个时以逗号隔开')
    picture = Column(VARCHAR(255))

    product_attribute = relationship('PmsProductAttribute')
    product = relationship('PmsProduct')


class PmsProductCategoryAttributeRelation(Base):
    __tablename__ = 'pms_product_category_attribute_relation'
    __table_args__ = {'comment': '产品的分类和属性的关系表，用于设置分类筛选条件（只支持一级分类）'}

    id = Column(BIGINT(20), primary_key=True)
    product_category_id = Column(ForeignKey('pms_product_category.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_attribute_id = Column(ForeignKey('pms_product_attribute.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    product_attribute = relationship('PmsProductAttribute')
    product_category = relationship('PmsProductCategory')


class PmsSkuStock(Base):
    __tablename__ = 'pms_sku_stock'
    __table_args__ = {'comment': 'sku的库存'}

    id = Column(BIGINT(20), primary_key=True, nullable=False)
    product_id = Column(ForeignKey('pms_product.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    sku_code = Column(VARCHAR(64), primary_key=True, nullable=False, comment='sku编码')
    price = Column(DECIMAL(10, 2))
    stock = Column(INTEGER(11), server_default=text("'0'"), comment='库存')
    low_stock = Column(INTEGER(11), comment='预警库存')
    pic = Column(VARCHAR(255), comment='展示图片')
    sale = Column(INTEGER(11), comment='销量')
    sp_data = Column(VARCHAR(500), comment='商品销售属性，json格式')

    product = relationship('PmsProduct')


class SmsFontbanner(Base):
    __tablename__ = 'sms_fontbanner'

    banner_id = Column(INTEGER(11), primary_key=True)
    product_id = Column(ForeignKey('pms_product.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    picture_src = Column(VARCHAR(255))
    createTime = Column(DateTime)
    display = Column(TINYINT(1))

    product = relationship('PmsProduct')


class SmsHot(Base):
    __tablename__ = 'sms_hot'

    id = Column(INTEGER(11), primary_key=True)
    product_id = Column(ForeignKey('pms_product.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    title = Column(VARCHAR(255))
    description = Column(VARCHAR(255))
    picUrl = Column(VARCHAR(255))
    price = Column(DECIMAL(10, 2))
    sort = Column(INTEGER(11))
    display = Column(TINYINT(1))

    product = relationship('PmsProduct')
