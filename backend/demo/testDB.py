from sqlalchemy import create_engine, Integer
from model import *
from config_kk import mysql_path
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接:
engine = create_engine(mysql_path)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def db_get_category():
    s = DBSession()
    resAll = s.query(PmsProductCategory).all()
    res = []
    for cat in resAll:
        if cat.nav_status and cat.show_status:
            if cat.level == 1:
                res.append({"id": cat.id, "title": cat.name, "children": []})
                for cati in resAll:
                    if cati.parent_id == cat.id and cati.level == 2:
                        res[-1]['children'].append({"id": cati.id,
                                                    "title": cati.name, "picUrl": cati.icon})
    # for cat in resAll:
    #       if cat.nav_status and cat.show_status:
    #         if cat.level== 2:
    #           res.append({"id":cat.id,"title":cat.title,"children":[]})
    s.close()
    print(res)

# db_get_category()

