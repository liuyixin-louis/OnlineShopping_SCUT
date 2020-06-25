# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, DateTime, ForeignKey, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, SMALLINT, TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PmsBrand(Base):
    __tablename__ = 'pms_brand'
    __table_args__ = {'comment': 'Ʒ�Ʊ�'}

    id = Column(BIGINT(20), primary_key=True)
    name = Column(VARCHAR(64))
    first_letter = Column(VARCHAR(8), comment='����ĸ')
    sort = Column(INTEGER(11))
    factory_status = Column(INTEGER(11), comment='�Ƿ�ΪƷ�������̣�0->���ǣ�1->��')
    show_status = Column(INTEGER(11))
    product_count = Column(INTEGER(11), comment='��Ʒ����')
    product_comment_count = Column(INTEGER(11), comment='��Ʒ��������')
    logo = Column(VARCHAR(255), comment='Ʒ��logo')
    description = Column(VARCHAR(255), comment='����')


class PmsFeightTemplate(Base):
    __tablename__ = 'pms_feight_template'
    __table_args__ = {'comment': '�˷�ģ��'}

    id = Column(BIGINT(20), primary_key=True)
    name = Column(VARCHAR(64))
    charge_type = Column(INTEGER(11), comment='�Ʒ�����:0->��������1->������')
    first_weight = Column(DECIMAL(10, 2), nullable=False, comment='����kg')
    first_fee = Column(DECIMAL(10, 2), comment='�׷ѣ�Ԫ��')
    continue_weight = Column(DECIMAL(10, 2))
    continme_fee = Column(DECIMAL(10, 2))
    dest = Column(VARCHAR(255), comment='Ŀ�ĵأ�ʡ���У�')


class PmsPlatformStatistic(Base):
    __tablename__ = 'pms_platform_statistics'

    id = Column(INTEGER(11), primary_key=True)
    datetime = Column(DateTime)
    tody_sale = Column(INTEGER(8))


class PmsProductAttributeCategory(Base):
    __tablename__ = 'pms_product_attribute_category'
    __table_args__ = {'comment': '��Ʒ���Է����'}

    id = Column(BIGINT(20), primary_key=True)
    name = Column(VARCHAR(64))
    attribute_count = Column(INTEGER(11), server_default=text("'0'"), comment='��������')
    param_count = Column(INTEGER(11), server_default=text("'0'"), comment='��������')


class PmsProductCategory(Base):
    __tablename__ = 'pms_product_category'
    __table_args__ = {'comment': '��Ʒ����'}

    id = Column(BIGINT(20), primary_key=True)
    parent_id = Column(BIGINT(20), comment='�ϻ�����ı�ţ�0��ʾһ������')
    name = Column(VARCHAR(64))
    level = Column(INTEGER(11), comment='���༶��0->1����1->2��')
    product_count = Column(INTEGER(11))
    product_unit = Column(VARCHAR(64))
    nav_status = Column(INTEGER(11), comment='�Ƿ���ʾ��ǰ̨��������0->����ʾ��1->��ʾ')
    show_status = Column(INTEGER(11), comment='��ʾ��ǰ̨������£�������ʾ״̬��0->����ʾ��1->��ʾ')
    sort = Column(INTEGER(11))
    icon = Column(VARCHAR(255), comment='ͼ��')
    keywords = Column(VARCHAR(255))
    description = Column(TEXT, comment='����')


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
    __table_args__ = {'comment': '��̨�û���'}

    id = Column(BIGINT(20), primary_key=True)
    username = Column(VARCHAR(64))
    password = Column(VARCHAR(64))
    icon = Column(VARCHAR(500), comment='ͷ��')
    email = Column(VARCHAR(100), comment='����')
    nick_name = Column(VARCHAR(200), comment='�ǳ�')
    note = Column(VARCHAR(500), comment='��ע��Ϣ')
    create_time = Column(DateTime, comment='����ʱ��')
    login_time = Column(DateTime, comment='����¼ʱ��')
    status = Column(INTEGER(11), server_default=text("'1'"), comment='�ʺ�����״̬��0->���ã�1->����')


class UmsMember(Base):
    __tablename__ = 'ums_member'
    __table_args__ = {'comment': '��Ա��'}

    id = Column(BIGINT(20), primary_key=True)
    member_level_id = Column(BIGINT(20))
    username = Column(VARCHAR(64), unique=True, comment='�û���')
    password = Column(VARCHAR(64), comment='����')
    nickname = Column(VARCHAR(64), comment='�ǳ�')
    phone = Column(VARCHAR(64), unique=True, comment='�ֻ�����')
    status = Column(INTEGER(11), comment='�ʺ�����״̬:0->���ã�1->����')
    create_time = Column(DateTime, comment='ע��ʱ��')
    icon = Column(VARCHAR(500), comment='ͷ��')
    gender = Column(INTEGER(11), comment='�Ա�0->δ֪��1->�У�2->Ů')
    birthday = Column(Date, comment='����')
    city = Column(VARCHAR(64), comment='��������')
    job = Column(VARCHAR(100), comment='ְҵ')
    personalized_signature = Column(VARCHAR(200), comment='����ǩ��')
    source_type = Column(INTEGER(11), comment='�û���Դ')


class OmsOrder(Base):
    __tablename__ = 'oms_order'
    __table_args__ = {'comment': '������'}

    id = Column(BIGINT(20), primary_key=True, comment='����id')
    member_id = Column(ForeignKey('ums_member.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    order_sn = Column(VARCHAR(64), comment='�������')
    create_time = Column(DateTime, comment='�ύʱ��')
    member_username = Column(VARCHAR(64), comment='�û��ʺ�')
    total_amount = Column(DECIMAL(10, 2), comment='�����ܽ��')
    pay_amount = Column(DECIMAL(10, 2), comment='Ӧ����ʵ��֧����')
    freight_amount = Column(DECIMAL(10, 2), comment='�˷ѽ��')
    pay_type = Column(INTEGER(11), comment='֧����ʽ��0->δ֧����1->֧������2->΢��')
    source_type = Column(INTEGER(11), comment='������Դ��0->PC������1->app����')
    status = Column(INTEGER(11), comment='����״̬��1->�����2->��������3->�ѷ�����4->�����ۣ�5->�����ۣ�6->�ѹر�')
    delivery_company = Column(VARCHAR(64), comment='������˾(���ͷ�ʽ)')
    delivery_sn = Column(VARCHAR(64), comment='��������')
    receiver_name = Column(VARCHAR(100), nullable=False, comment='�ջ�������')
    receiver_phone = Column(VARCHAR(32), nullable=False, comment='�ջ��˵绰')
    receiver_post_code = Column(VARCHAR(32), comment='�ջ����ʱ�')
    receiver_province = Column(VARCHAR(32), comment='ʡ��/ֱϽ��')
    receiver_city = Column(VARCHAR(32), comment='����')
    receiver_region = Column(VARCHAR(32), comment='��')
    receiver_detail_address = Column(VARCHAR(200), comment='��ϸ��ַ')
    note = Column(VARCHAR(500), comment='������ע')
    confirm_status = Column(INTEGER(11), comment='ȷ���ջ�״̬��0->δȷ�ϣ�1->��ȷ��')
    delete_status = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='ɾ��״̬��0->δɾ����1->��ɾ��')
    payment_time = Column(DateTime, comment='֧��ʱ��')
    delivery_time = Column(DateTime, comment='����ʱ��')
    receive_time = Column(DateTime, comment='ȷ���ջ�ʱ��')
    comment_time = Column(DateTime, comment='����ʱ��')

    member = relationship('UmsMember')


class PmsProduct(Base):
    __tablename__ = 'pms_product'
    __table_args__ = {'comment': '��Ʒ��Ϣ'}

    id = Column(BIGINT(20), primary_key=True)
    brand_id = Column(ForeignKey('pms_brand.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_category_id = Column(ForeignKey('pms_product_category.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    feight_template_id = Column(ForeignKey('pms_feight_template.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_attribute_category_id = Column(ForeignKey('pms_product_attribute_category.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    name = Column(VARCHAR(64), nullable=False)
    pic = Column(VARCHAR(255))
    product_sn = Column(VARCHAR(64), nullable=False, comment='����')
    delete_status = Column(INTEGER(11), comment='ɾ��״̬��0->δɾ����1->��ɾ��')
    publish_status = Column(INTEGER(11), comment='�ϼ�״̬��0->�¼ܣ�1->�ϼ�')
    new_status = Column(INTEGER(11), comment='��Ʒ״̬:0->������Ʒ��1->��Ʒ')
    recommand_status = Column(INTEGER(11), comment='�Ƽ�״̬��0->���Ƽ���1->�Ƽ�')
    verify_status = Column(INTEGER(11), comment='���״̬��0->δ��ˣ�1->���ͨ��')
    sort = Column(INTEGER(11), comment='����')
    sale = Column(INTEGER(11), comment='����')
    price = Column(DECIMAL(10, 2))
    sub_title = Column(VARCHAR(255), comment='������')
    description = Column(TEXT, comment='��Ʒ����')
    original_price = Column(DECIMAL(10, 2), comment='�г���')
    stock = Column(INTEGER(11), comment='���')
    low_stock = Column(INTEGER(11), comment='���Ԥ��ֵ')
    unit = Column(VARCHAR(16), comment='��λ')
    weight = Column(DECIMAL(10, 2), comment='��Ʒ������Ĭ��Ϊ��')
    preview_status = Column(INTEGER(11), comment='�Ƿ�ΪԤ����Ʒ��0->���ǣ�1->��')
    service_ids = Column(VARCHAR(64), comment='�Զ��ŷָ�Ĳ�Ʒ����1->�����˻���2->�����˿3->��Ѱ���')
    keywords = Column(VARCHAR(255))
    note = Column(VARCHAR(255))
    album_pics = Column(VARCHAR(255), comment='����ͼƬ������ƷͼƬ����Ϊ5�ţ��Զ��ŷָ�')
    detail_title = Column(VARCHAR(255))
    detail_desc = Column(TEXT)
    detail_html = Column(TEXT, comment='��Ʒ������ҳ����')
    detail_mobile_html = Column(TEXT, comment='�ƶ�����ҳ����')
    brand_name = Column(VARCHAR(255), comment='Ʒ������')
    product_category_name = Column(VARCHAR(255), comment='��Ʒ��������')
    shop_id = Column(ForeignKey('pms_shop.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    brand = relationship('PmsBrand')
    feight_template = relationship('PmsFeightTemplate')
    product_attribute_category = relationship('PmsProductAttributeCategory')
    product_category = relationship('PmsProductCategory')
    shop = relationship('PmsShop')


class PmsProductAttribute(Base):
    __tablename__ = 'pms_product_attribute'
    __table_args__ = {'comment': '��Ʒ���Բ�����'}

    id = Column(BIGINT(20), primary_key=True)
    product_attribute_category_id = Column(ForeignKey('pms_product_attribute_category.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    name = Column(VARCHAR(64))
    select_type = Column(INTEGER(11), comment='����ѡ�����ͣ�0->Ψһ��1->��ѡ��2->��ѡ')
    input_type = Column(INTEGER(11), comment='����¼�뷽ʽ��0->�ֹ�¼�룻1->���б���ѡȡ')
    input_list = Column(VARCHAR(255), comment='��ѡֵ�б��Զ��Ÿ���')
    sort = Column(INTEGER(11), comment='�����ֶΣ���ߵĿ��Ե����ϴ�ͼƬ')
    filter_type = Column(INTEGER(11), comment='����ɸѡ��ʽ��1->��ͨ��1->��ɫ')
    search_type = Column(INTEGER(11), comment='�������ͣ�0->����Ҫ���м�����1->�ؼ��ּ�����2->��Χ����')
    related_status = Column(INTEGER(11), comment='��ͬ���Բ�Ʒ�Ƿ������0->��������1->����')
    hand_add_status = Column(INTEGER(11), comment='�Ƿ�֧���ֶ�������0->��֧�֣�1->֧��')
    type = Column(INTEGER(11), comment='���Ե����ͣ�0->���1->����')

    product_attribute_category = relationship('PmsProductAttributeCategory')


class UmsMemberReceiveAddres(Base):
    __tablename__ = 'ums_member_receive_address'
    __table_args__ = {'comment': '��Ա�ջ���ַ��'}

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(ForeignKey('ums_member.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    name = Column(VARCHAR(100), comment='�ջ�������')
    phone_number = Column(VARCHAR(64))
    default_status = Column(SMALLINT(6), comment='�Ƿ�ΪĬ��')
    post_code = Column(VARCHAR(100), comment='��������')
    province = Column(VARCHAR(100), comment='ʡ��/ֱϽ��')
    city = Column(VARCHAR(100), comment='����')
    region = Column(VARCHAR(100), comment='��')
    detail_address = Column(VARCHAR(128), comment='��ϸ��ַ(�ֵ�)')

    member = relationship('UmsMember')


class UmsMemberStatisticsInfo(Base):
    __tablename__ = 'ums_member_statistics_info'
    __table_args__ = {'comment': '��Աͳ����Ϣ'}

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(ForeignKey('ums_member.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    consume_amount = Column(DECIMAL(10, 2), comment='�ۼ����ѽ��')
    order_count = Column(INTEGER(11), comment='��������')
    comment_count = Column(INTEGER(11), comment='������')
    return_order_count = Column(INTEGER(11), comment='�˻�����')
    login_count = Column(INTEGER(11), comment='��¼����')
    attend_count = Column(INTEGER(11), comment='��ע����')
    fans_count = Column(INTEGER(11), comment='��˿����')
    recent_order_time = Column(DateTime, comment='���һ���¶���ʱ��')

    member = relationship('UmsMember')


class OmsCartItem(Base):
    __tablename__ = 'oms_cart_item'
    __table_args__ = {'comment': '���ﳵ��'}

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(ForeignKey('pms_product.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_sku_id = Column(BIGINT(20))
    member_id = Column(ForeignKey('ums_member.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    quantity = Column(INTEGER(11), comment='��������')
    price = Column(DECIMAL(10, 2), comment='��ӵ����ﳵ�ļ۸�')
    product_pic = Column(VARCHAR(1000), comment='��Ʒ��ͼ')
    product_name = Column(VARCHAR(500), comment='��Ʒ����')
    product_sub_title = Column(VARCHAR(500), comment='��Ʒ�����⣨���㣩')
    product_sku_code = Column(VARCHAR(200), comment='��Ʒsku����')
    member_nickname = Column(VARCHAR(500), comment='��Ա�ǳ�')
    create_date = Column(DateTime, comment='����ʱ��')
    modify_date = Column(DateTime, comment='�޸�ʱ��')
    delete_status = Column(INTEGER(11), server_default=text("'0'"), comment='�Ƿ�ɾ��')
    product_category_id = Column(ForeignKey('pms_product_category.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='��Ʒ����')
    product_brand = Column(ForeignKey('pms_brand.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_sn = Column(VARCHAR(200))
    product_attr = Column(VARCHAR(500), comment='��Ʒ��������:[{"key":"��ɫ","value":"��ɫ"},{"key":"����","value":"4G"}]')
    max_number = Column(INTEGER(11))
    checked = Column(SMALLINT(1))

    member = relationship('UmsMember')
    pms_brand = relationship('PmsBrand')
    product_category = relationship('PmsProductCategory')
    product = relationship('PmsProduct')


class OmsOrderItem(Base):
    __tablename__ = 'oms_order_item'
    __table_args__ = {'comment': '����������������Ʒ'}

    id = Column(BIGINT(20), primary_key=True)
    order_id = Column(ForeignKey('oms_order.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='����id')
    order_sn = Column(VARCHAR(64), comment='�������')
    product_id = Column(BIGINT(20))
    product_pic = Column(VARCHAR(500))
    product_name = Column(VARCHAR(200))
    product_brand = Column(VARCHAR(200))
    product_sn = Column(VARCHAR(64))
    product_price = Column(DECIMAL(10, 2), comment='���ۼ۸�')
    product_quantity = Column(INTEGER(11), comment='��������')
    product_sku_id = Column(BIGINT(20), comment='��Ʒsku���')
    product_sku_code = Column(VARCHAR(50), comment='��Ʒsku����')
    product_category_id = Column(BIGINT(20), comment='��Ʒ����id')
    product_attr = Column(VARCHAR(500), comment='��Ʒ��������:[{"key":"��ɫ","value":"��ɫ"},{"key":"����","value":"4G"}]')

    order = relationship('OmsOrder')


class PmsComment(Base):
    __tablename__ = 'pms_comment'
    __table_args__ = {'comment': '��Ʒ���۱�'}

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(ForeignKey('pms_product.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    member_nick_name = Column(VARCHAR(255))
    product_name = Column(VARCHAR(255))
    star = Column(INTEGER(11), comment='����������0->5')
    create_time = Column(DateTime)
    show_status = Column(INTEGER(11))
    product_attribute = Column(VARCHAR(255), comment='����ʱ����Ʒ����')
    collect_count = Column(INTEGER(11))
    read_count = Column(INTEGER(11))
    content = Column(TEXT)
    pics = Column(VARCHAR(1000), comment='�ϴ�ͼƬ��ַ���Զ��Ÿ���')
    member_icon = Column(VARCHAR(255), comment='�����û�ͷ��')
    member_id = Column(ForeignKey('ums_member.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    member = relationship('UmsMember')
    product = relationship('PmsProduct')


class PmsProductAttributeValue(Base):
    __tablename__ = 'pms_product_attribute_value'
    __table_args__ = {'comment': '�洢��Ʒ������Ϣ�ı�'}

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(ForeignKey('pms_product.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_attribute_id = Column(ForeignKey('pms_product_attribute.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    value = Column(VARCHAR(64), nullable=False, comment='�ֶ���ӹ��������ֵ��������ֵ������ж��ʱ�Զ��Ÿ���')
    picture = Column(VARCHAR(255))

    product_attribute = relationship('PmsProductAttribute')
    product = relationship('PmsProduct')


class PmsProductCategoryAttributeRelation(Base):
    __tablename__ = 'pms_product_category_attribute_relation'
    __table_args__ = {'comment': '��Ʒ�ķ�������ԵĹ�ϵ���������÷���ɸѡ������ֻ֧��һ�����ࣩ'}

    id = Column(BIGINT(20), primary_key=True)
    product_category_id = Column(ForeignKey('pms_product_category.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    product_attribute_id = Column(ForeignKey('pms_product_attribute.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    product_attribute = relationship('PmsProductAttribute')
    product_category = relationship('PmsProductCategory')


class PmsSkuStock(Base):
    __tablename__ = 'pms_sku_stock'
    __table_args__ = {'comment': 'sku�Ŀ��'}

    id = Column(BIGINT(20), primary_key=True, nullable=False)
    product_id = Column(ForeignKey('pms_product.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    sku_code = Column(VARCHAR(64), primary_key=True, nullable=False, comment='sku����')
    price = Column(DECIMAL(10, 2))
    stock = Column(INTEGER(11), server_default=text("'0'"), comment='���')
    low_stock = Column(INTEGER(11), comment='Ԥ�����')
    pic = Column(VARCHAR(255), comment='չʾͼƬ')
    sale = Column(INTEGER(11), comment='����')
    sp_data = Column(VARCHAR(500), comment='��Ʒ�������ԣ�json��ʽ')

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
