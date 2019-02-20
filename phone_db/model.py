# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine, \
    Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

db_path = os.path.join(os.path.dirname(__file__), 'phone.db')
engine = create_engine('sqlite:///' + db_path)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Region(Base):
    """归属地"""
    __tablename__ = 'regions'
    id = Column(Integer, primary_key=True)
    province = Column(String)
    city = Column(String)
    zip_code = Column(String)
    area_code = Column(String)
    phones = relationship('Phone', lazy='dynamic', backref='region')

    def content(self):
        return {
            'province': self.province,
            'city': self.city,
            'zip_code': self.zip_code,
            'area_code': self.area_code,
        }


class Phone(Base):
    """手机号段"""
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, index=True)
    type = Column(Integer)
    region_id = Column(Integer, ForeignKey('regions.id'))

    @staticmethod
    def get_phone_no_type(no):
        if no == 4:
            return '电信虚拟运营商'
        if no == 5:
            return '联通虚拟运营商'
        if no == 6:
            return '移动虚拟运营商'
        if no == 3:
            return '电信'
        if no == 2:
            return '联通'
        if no == 1:
            return '移动'

    def detail(self):
        return (
            self.number,
            self.get_phone_no_type(self.type),
            self.region.content()
        )


Base.metadata.create_all(engine)
