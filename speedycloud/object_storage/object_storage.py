# -*- coding: utf-8 -*-
from speedycloud.object_storage import AbstractProductAPI
from lxml import etree


class ObjectStorageAPI(AbstractProductAPI):
    BASE_PATH = '/'

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def list(self, bucket, data=None, header_params={}):
        # 查询桶内对象列表
        path = self._get_path('%s' % bucket)
        return self.get(path, data, header_params)

    def create_bucket(self, bucket, data=None, header_params={}):
        # 创建存储桶
        path = self._get_path('%s' % bucket)
        return self.put(path, data, header_params)

    def delete_bucket(self, bucket, data=None, header_params={}):
        # 删除存储桶
        path = self._get_path('%s' % bucket)
        return self.delete(path, data, header_params)

    def query_bucket_acl(self, bucket, data=None, header_params={}):
        # 查询桶的权限
        path = self._get_path('%s?acl' % bucket)
        return self.get(path, data, header_params)

    def delete_object_data(self, bucket, key, header_params={}):
        # 删除桶内对象
        path = self._get_path('%s/%s' % (bucket, key))
        return self.delete(path, params=header_params)

    def query_object_version(self, bucket, key, header_params={}):
        # 查询存储桶内对象的版本信息
        path = self._get_path('%s?versioning' % (bucket, key))
        return self.get(path, header_params)

    def download_object_data(self, bucket, key, header_params={}):
        # 下载桶内对象的数据
        path = self._get_path('%s/%s' % (bucket, key))
        return self.get(path, params=header_params)

    def update_bucket_acl(self, bucket, header_params={}):
        # 修改桶的权限
        path = self._get_path('%s?acl' % bucket)
        return self.put(path, params=header_params)

    def update_object_acl(self, bucket, key, header_params={}):
        # 修改桶内对象的权限
        path = self._get_path('%s/%s?acl' % (bucket, key))
        return self.put(path, params=header_params)

    def storing_object_data(self, bucket, key, update_data, update_type, header_params={}):
        # 创建存储桶内对象
        path = self._get_path('%s/%s' % (bucket, key))
        if update_type == 'file':
            update_content = open(str(update_data), 'rb').read()
        elif update_type == 'string':
            update_content = update_data
        return self.put(path, update_content, header_params)

    def upload_big_data_one(self, bucket, key, header_params={}):
        # 上传大数据第一步
        path = self._get_path('%s/%s?uploads' % (bucket, key))
        xml = self.post(path, params=header_params)
        # print xml
        root = etree.fromstring(xml)
        upload_id = root.find(
            ".//{http://s3.amazonaws.com/doc/2006-03-01/}UploadId").text
        return upload_id

    def upload_big_data_two(self, bucket, key, update_data, update_type, part_number, upload_id, header_params={}):
        '''
            upload big data two
            params:
                bucket string ....
            return:
                ...
        '''
        # 上传大数据第二步
        # for i in range(part_number):
        if update_type == 'file':
            update_content = open(str(update_data), 'rb').read()
        elif update_type == 'string':
            update_content = update_data
        path = self._get_path('%s/%s?partNumber=%s&uploadId=%s' % (
            bucket, key, int(part_number), str(upload_id)))
        etag = self.put(path, update_content, header_params)
        return etag

    def upload_big_data_three(self, bucket, key, update_data, update_type, upload_id, header_params={}):
        # 上传大数据第三步
        path = self._get_path('%s/%s?uploadId=%s' %
                              (bucket, key, str(upload_id)))
        if update_type == 'file':
            update_content = open(str(update_data), 'rb').read()
        elif update_type == 'string':
            update_content = update_data
        # print self.post(path, params)
        return self.post(path, update_content, header_params)
