# -*- coding: utf-8 -*-
import struct
from phone import Phone as SourcePhone
from model import Region, Phone, Session


class ParsePhone(SourcePhone):
    """
    解析phone.dat phone数据
    """

    def __init__(self):
        super(ParsePhone, self).__init__()
        self.session = Session()

    def get_data_mapping(self):
        mapping = {}
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
            mapping[start_offset] = r.id
            start_offset = end_offset + 1
        return mapping

    def get_phone_data(self, mapping):
        current_offset = self.first_phone_record_offset

        while current_offset < len(self.buf):
            buffer = self.buf[current_offset:current_offset + self.phone_fmt_length]
            number, region_offset, phone_type = struct.unpack(self.phone_fmt, buffer)
            p = Phone(number=number, type=phone_type,
                      region_id=mapping[region_offset])
            self.session.add(p)
            self.session.commit()
            current_offset += self.phone_fmt_length
        return None

    def main(self):
        mapping = self.get_data_mapping()
        self.get_phone_data(mapping)


if __name__ == '__main__':
    ParsePhone().main()
