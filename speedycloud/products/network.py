# -*- coding: utf-8 -*-
from speedycloud.products import AbstractProductAPI


class NetworkAPI(AbstractProductAPI):
    BASE_PATH = "/api/v1/products/networks/"

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def create(self, availability_zone):
        # 创建网络
        path = self._get_path("create")
        return self.post(path, {'az': availability_zone})

    def list(self):
        # 网络列表
        return self.get(self.BASE_PATH)

    def detail(self, network_id):
        # 网络信息
        # network_id:网络id
        path = self._get_path(network_id)
        return self.get(path)

    def delete(self, network_id):
        # 删除网络
        # network_id:网络id
        path = self._get_path("%s/delete" % str(network_id))
        return self.post(path)

    def set_alias(self, network_id, alias):
        # 为网络设置别名
        # network_id:网络id
        # alias:别名
        path = self._get_path("%s/alias" % str(network_id))
        return self.post(path, {'alias': alias})

    def set_group(self, network_id, group):
        # 为网络设置分组
        # group:组名
        path = self._get_path("%s/group" % str(network_id))
        return self.post(path, {'group': group})

    def groups(self):
        # 网络分组列表
        path = self._get_path('groups')
        return self.get(path)

    def create_database(self, available_zone, isp, image, memory, disk, bandwidth):
        # 创建数据库
        configurations = {
            # 可用数据中心
            'az': available_zone,
            # 内存大小
            'memory': memory,
            # 硬盘大小
            'disk': disk,
            # 带宽
            'bandwidth': bandwidth,
            # 数据中心支持的运营商
            'isp': isp,
            # 数据库镜像
            'image': image,
        }
        return self.post("/api/v1/products/databases/provision", configurations)

    def create_cache(self, available_zone, isp, image, memory, disk, bandwidth):
        # 创建缓存
        configurations = {
            # 可用数据中心
            'az': available_zone,
            # 内存大小
            'memory': memory,
            # 硬盘大小
            'disk': disk,
            # 带宽
            'bandwidth': bandwidth,
            # 数据中心支持的运营商
            'isp': isp,
            # 数据库镜像
            'image': image,
        }
        return self.post("/api/v1/products/caches/provision", configurations)
