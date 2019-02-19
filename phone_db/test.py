# -*- coding: utf-8 -*-
import unittest
from model import Session, Phone, Region


class TestModel(unittest.TestCase):

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        pass

    def test_phone(self):
        p = self.session.query(Phone).filter_by(number=1761166).first()
        res = p.detail()
        self.assertEqual(res[0], 1761166)
        self.assertEqual(res[1], '联通')
        self.assertEqual(res[2]['zip_code'], '100000')
        self.assertEqual(res[2]['area_code'], '010')
        self.assertEqual(res[2]['city'], '北京')
        self.assertEqual(res[2]['province'], '北京')

    def test_region(self):
        p = self.session.query(Region).filter_by(zip_code='100000').first()
        res = p.content()
        self.assertEqual(res['zip_code'], '100000')
        self.assertEqual(res['area_code'], '010')
        self.assertEqual(res['city'], '北京')
        self.assertEqual(res['province'], '北京')


if __name__ == '__main__':
    unittest.main()
