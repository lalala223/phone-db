# phone-db
手机号码归属地SQLite数据库

#### 数据表结构

##### phones表
```sql
CREATE TABLE phones (
	id INTEGER NOT NULL, 
	number INTEGER, 
	type INTEGER, 
	region_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(region_id) REFERENCES regions (id)
)
```

##### regions表
```sql
CREATE TABLE regions (
	id INTEGER NOT NULL, 
	province VARCHAR, 
	city VARCHAR, 
	zip_code VARCHAR, 
	area_code VARCHAR, 
	PRIMARY KEY (id)
)
```

#### 使用：
```python
from phone_db import Session, Phone, Region
session = Session()
session.query(Phone).count()
```

#### 记录条数

415284 (updated:2019年2月)

#### 数据来源

[https://github.com/ls0f/phone](https://github.com/ls0f/phone)
