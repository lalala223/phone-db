# -*- coding: utf-8 -*-
import unittest
from sqlalchemy.orm.dynamic import AppenderQuery
from model import Session, Phone, Region


class TestModel(unittest.TestCase):

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        pass

    def test_phone(self):
        p = self.session.query(Phone).filter_by(number=1761166).first()
        self.assertEqual(p.number, 1761166)
        self.assertEqual(p.type, 2)
        self.assertIsInstance(p.region, Region)

    def test_region(self):
        r = self.session.query(Region).filter_by(zip_code='100000').first()
        self.assertEqual(r.zip_code, '100000')
        self.assertEqual(r.area_code, '010')
        self.assertEqual(r.city, '北京')
        self.assertEqual(r.province, '北京')
        self.assertIsInstance(r.phones, AppenderQuery)


if __name__ == '__main__':
    unittest.main()
