# phone-db
手机号码归属地SQLite数据库

#### 使用：
##### 查询数据库中手机号段总条数
```
>>> from phone_db import Session, Phone, Region
>>> session = Session()
>>> session.query(Phone).count()
415284
```

##### 查询北京市联通手机号段条数
```
>>> city = session.query(Region).filter_by(zip_code='100000').first()
>>> if city:
...     city.phones.filter_by(type=2).count()
...
6355
```

##### 查询指定手机号段归属地信息
```
>>> num = session.query(Phone).filter_by(number=1761166).first()
>>> if num:
...     num.detail()
...
(1761166, '联通', {'province': '北京', 'city': '北京', 'zip_code': '100000', 'area_code': '010'})
```

#### 数据表结构

##### phones表
```
id INTEGER NOT NULL,
number INTEGER,
type INTEGER,
region_id INTEGER,
PRIMARY KEY (id),
FOREIGN KEY(region_id) REFERENCES regions (id)
```

##### regions表
```
id INTEGER NOT NULL,
province VARCHAR,
city VARCHAR,
zip_code VARCHAR,
area_code VARCHAR,
PRIMARY KEY (id)
```

#### phones表type字段卡类型定义
```
* 1 移动
* 2 联通
* 3 电信
* 4 电信虚拟运营商
* 5 联通虚拟运营商
* 6 移动虚拟运营商
```

#### 数据可视化
下载[phone.db](https://raw.githubusercontent.com/lalala223/phone-db/master/phone_db/phone.db)文件，使用[sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser)查看

#### 记录条数

415284 (updated:2019年2月)

#### 数据来源

[https://github.com/ls0f/phone](https://github.com/ls0f/phone)
