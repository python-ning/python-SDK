# -*- coding: utf-8 -*-
from speedycloud.storage import AbstractProductAPI
from lxml import etree


class ObjectStorageAPI(AbstractProductAPI):
    BASE_PATH = '/'

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def list(self, bucket):
        '''
        查询桶内对象列表
        参数:
            bucket: 桶名
        注意： bucket参数为''时，可查看所有桶
        '''
        # dicts = {}
        # contentss = []
        # owner_dict = {}
        # path = self._get_path('%s' % bucket)
        # xml = self.get(path)
        # root = etree.fromstring(xml)
        # xml_ns = "./{http://s3.amazonaws.com/doc/2006-03-01/}%s"
        # dicts['Name'] = root.find(
        #     xml_ns % ("Name")).text
        # dicts['Prefix'] = root.find(
        #     xml_ns % ("Prefix")).text
        # dicts['Marker'] = root.find(
        #     xml_ns % ("Marker")).text
        # dicts['MaxKeys'] = root.find(
        #     xml_ns % ("MaxKeys")).text
        # dicts['IsTruncated'] = root.find(
        #     xml_ns % ("IsTruncated")).text
        # contents = root.findall(
        #     xml_ns % ("Contents"))
        # for content in contents:
        #     content_dict = {}
        #     content_dict['Key'] = content.find(
        #         xml_ns % ('Key')).text
        #     content_dict['LastModified'] = content.find(
        #         xml_ns % ('LastModified')).text
        #     content_dict['ETag'] = content.find(
        #         xml_ns % ('ETag')).text
        #     content_dict['Size'] = content.find(
        #         xml_ns % ('Size')).text
        #     content_dict['StorageClass'] = content.find(
        #         xml_ns % ('StorageClass')).text
        #     owners = content.find(
        #         xml_ns % ('Owner'))
        #     owner_dict['ID'] = owners.find(
        #         xml_ns % ('ID')).text
        #     owner_dict['DisplayName'] = owners.find(
        #         xml_ns % ('DisplayName')).text
        #     content_dict['Owner'] = owner_dict
        #     contentss.append(content_dict)
        # dicts['Content'] = contentss
        path = self._get_path('%s' % bucket)
        return self.get(path)
        # return dicts

    def create_bucket(self, bucket):
        '''
        创建存储桶
        参数:
            bucket: 桶名
        '''
        path = self._get_path('%s' % bucket)
        return self.put(path)

    def delete_bucket(self, bucket):
        '''
        注意： 在桶内没有对象的时候才能删除桶
        删除存储桶
        参数:
            bucket: 桶名
        '''
        path = self._get_path('%s' % bucket)
        return self.delete(path)

    def query_bucket_acl(self, bucket):
        '''
        查询桶的权限
        参数:
            bucket: 桶名
        '''
        path = self._get_path('%s?acl' % bucket)
        return self.get(path)

    def delete_object_data(self, bucket, key):
        '''
        删除桶内对象
        注意： 删除成功不是返回200
        参数:
            bucket: 桶名
            key: 对象名
        '''
        path = self._get_path('%s/%s' % (bucket, key))
        return self.delete(path)

    def query_object_version(self, bucket, key):
        '''
        查询存储桶内对象的版本信息
        参数:
            bucket: 桶名
            key: 对象名
        '''
        path = self._get_path('%s/%s?versioning' % (bucket, key))
        return self.get(path)

    def download_object_data(self, bucket, key):
        '''
        下载桶内对象的数据
        参数:
            bucket: 桶名
            key: 对象名
        '''
        path = self._get_path('%s/%s' % (bucket, key))
        return self.get(path)

    def update_bucket_acl(self, bucket, header_params={}):
        '''
        修改桶的权限
        参数:
            bucket: 桶名
            header_params: 请求头参数， 是一个字典
                {'x-amz-acl':test}
                    test: 允许值
                        private：自己拥有全部权限，其他人没有任何权限
                        public-read：自己拥有全部权限，其他人拥有读权限
                        public-read-write：自己拥有全部权限，其他人拥有读写权限
                        authenticated-read：自己拥有全部权限，被授权的用户拥有读权限
        '''
        path = self._get_path('%s?acl' % bucket)
        return self.put(path, params=header_params)

    def update_object_acl(self, bucket, key, header_params={}):
        '''
        修改桶内对象的权限
        参数:
            bucket: 桶名
            key: 对象名
            header_params: 请求头参数， 是一个字典
                {'x-amz-acl':test}
                    test: 允许值
                        private：自己拥有全部权限，其他人没有任何权限
                        public-read：自己拥有全部权限，其他人拥有读权限
                        public-read-write：自己拥有全部权限，其他人拥有读写权限
                        authenticated-read：自己拥有全部权限，被授权的用户拥有读权限
        '''

        path = self._get_path('%s/%s?acl' % (bucket, key))
        return self.put(path, params=header_params)

    def storing_object_data(self, bucket, key, update_data, update_type, header_params={}):
        '''
        创建存储桶内对象
        参数:
            bucket: 桶名
            key: 对象名
            update_data: 对象的内容（文件的路径/字符串）
            update_type: 对象内容类型 允许值 'file','string'
        '''
        path = self._get_path('%s/%s' % (bucket, key))
        if update_type == 'file':
            update_content = open(str(update_data), 'rb').read()
        elif update_type == 'string':
            update_content = update_data
        return self.put(path, update_content, header_params)

    def upload_big_data_one(self, bucket, key):
        '''
        上传大数据第一步
        参数:
            bucket: 桶名
            key: 对象名
        '''
        path = self._get_path('%s/%s?uploads' % (bucket, key))
        xml = self.post(path)
        root = etree.fromstring(xml)
        upload_id = root.find(
            ".//{http://s3.amazonaws.com/doc/2006-03-01/}UploadId").text
        return upload_id

    def upload_big_data_two(self, bucket, key, update_data, update_type, part_number, upload_id):
        '''
        上传大数据第二步
        参数:
            bucket: 桶名
            key: 对象名
            update_data: 对象的内容（文件的路径/字符串）
            update_type: 对象内容类型 允许值 'file','string'
            part_number: 上传的第几部分，分几部分就运行几次本函数
            upload_id: 上传大数据第一步返回的uploadID
        注意：将返回的etag保存，在大数据上传第三步使用
        '''
        if update_type == 'file':
            update_content = open(str(update_data), 'rb').read()
        elif update_type == 'string':
            update_content = update_data
        path = self._get_path('%s/%s?partNumber=%s&uploadId=%s' % (
            bucket, key, int(part_number), str(upload_id)))
        request, header = self.upload_big_data_put(path, update_content)
        return self.parseheader(header)

    def parseheader(self, header):
        for info in header:
            if info[0] == "etag":
                return info[1]
        return ""

    def upload_big_data_three(self, bucket, key, update_data, update_type, upload_id):
        '''
        上传大数据第三步
        参数:
            bucket: 桶名
            key: 对象名
            update_data: 对象的内容（文件的路径/字符串）
            update_type: 对象内容类型 允许值 'file','string'
            upload_id: 上传大数据第一步返回的uploadID

        '''
        path = self._get_path('%s/%s?uploadId=%s' %
                              (bucket, key, str(upload_id)))
        if update_type == 'file':
            update_content = open(str(update_data), 'rb').read()
        elif update_type == 'string':
            update_content = update_data
        return self.post(path, update_content)
