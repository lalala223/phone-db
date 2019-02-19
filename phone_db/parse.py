# -*- coding: utf-8 -*-
import os
import json
import struct
from phone import Phone as SourcePhone
from model import Region, Phone, Session


class ParseRegion(SourcePhone):
    """解析phone.dat region数据"""

    def __init__(self):
        super(ParseRegion, self).__init__()
        self.mapping = {}
        self.session = Session()

    def _save_mapping(self):
        file = os.path.join(os.path.dirname(__file__), "mapping.json")
        with open(file, 'w') as f:
            f.write(json.dumps(self.mapping))

    def get_region_data(self):
        start_offset = 8
        while True:
            end_offset = start_offset + self.buf[start_offset:-1].find(b'\x00')
            if not len(self.buf[start_offset:end_offset]) > 1:
                break
            record_content = self.buf[start_offset:end_offset].decode()
            province, city, zip_code, area_code = record_content.split('|')
            r = Region(province=province, city=city,
                       zip_code=zip_code, area_code=area_code)
            self.session.add(r)
            self.session.commit()
            self.mapping[start_offset] = r.id
            start_offset = end_offset + 1
        self._save_mapping()


class ParsePhone(SourcePhone):
    """解析phone.dat phone数据"""

    def __init__(self):
        super(ParsePhone, self).__init__()
        self.session = Session()

    def _read_mapping(self):
        file = os.path.join(os.path.dirname(__file__), "mapping.json")
        if not os.path.exists(file):
            raise RuntimeError('mapping.json is not exists')
        with open(file, 'r') as f:
            return json.load(f)

    def get_phone_data(self):
        mapping = self._read_mapping()
        current_offset = self.first_phone_record_offset

        while current_offset < len(self.buf):
            buffer = self.buf[current_offset:current_offset + self.phone_fmt_length]
            number, region_offset, phone_type = struct.unpack(self.phone_fmt, buffer)
            p = Phone(number=number, type=phone_type,
                      region_id=mapping[str(region_offset)])
            self.session.add(p)
            self.session.commit()
            current_offset += self.phone_fmt_length


if __name__ == '__main__':
    pr = ParseRegion()
    pr.get_region_data()
    pp = ParsePhone()
    pp.get_phone_data()
