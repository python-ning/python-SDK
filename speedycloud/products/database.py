# -*- coding: utf-8 -*-
from speedycloud.products import AbstractProductAPI


class DatabaseAPI(AbstractProductAPI):
    def list(self):
        return self.get('/api/v1/products/databases/')
