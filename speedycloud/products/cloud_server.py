# -*- coding: utf-8 -*-
from speedycloud.products import AbstractProductAPI


class CloudServerAPI(AbstractProductAPI):
    BASE_PATH = '/api/v1/products/cloud_servers/'

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def list(self):
        # 云主机列表
        return self.get(self.BASE_PATH)

    def detail(self, id):
        # 云主机信息
        path = self._get_path(str(id))
        return self.get(path)

    def backups(self, id):
        # 云主机备份列表
        path = self._get_path("%s/backups" % str(id))
        return self.get(path)

    def jobs(self, id):
        # 云主机任务列表
        path = self._get_path("%s/jobs" % str(id))
        return self.get(path)

    def provision(self, availability_zone, isp, image, cpu, memory, disk, bandwidth):
        # create cloud server/创建云主机
        path = self._get_path('provision')
        configurations = {
            # 数据中心
            'az': availability_zone,
            # 运营商
            'isp': isp,
            # 镜像
            'image': image,
            # cpu核心数
            'cpu': cpu,
            # 内存大小
            'memory': memory,
            # 硬盘大小
            'disk': disk,
            # 带宽
            'bandwidth': bandwidth,
        }
        return self.post(path, configurations)

    def start(self, cloud_server_id):
        # 启动云主机
        return self._cloud_server_simple_operations('start', cloud_server_id)

    def restart(self, cloud_server_id):
        # 重启云主机
        return self._cloud_server_simple_operations('restart', cloud_server_id)

    def stop(self, cloud_server_id):
        # 关闭云主机
        return self._cloud_server_simple_operations('stop', cloud_server_id)

    def suspend(self, cloud_server_id):
        # 挂起云主机
        return self._cloud_server_simple_operations('suspend', cloud_server_id)

    def resume(self, cloud_server_id):
        # 恢复云主机
        return self._cloud_server_simple_operations('resume', cloud_server_id)

    def backup(self, cloud_server_id, name):
        # 备份云主机
        path = self._get_path("%s/backup" % str(cloud_server_id))
        return self.post(path, {'name': name})

    def restore_backup(self, cloud_server_id, name):
        # 回复云主机备份
        path = self._get_path("%s/backups/%s/restore" % (str(cloud_server_id), name))
        return self.post(path)

    def delete_backup(self, cloud_server_id, name):
        # 删除云主机备份
        path = self._get_path("%s/backups/%s/delete" % (str(cloud_server_id), name))
        return self.post(path)

    def set_tag(self, id, tag):
        # 为云主机设置标签
        path = self._get_path("%s/tag" % str(id))
        return self.post(path, {'tag': tag})

    def set_alias(self, cloud_server_id, alias):
        # 为云主机设置别名
        path = self._get_path("%s/alias" % str(cloud_server_id))
        return self.post(path, {'alias': alias})

    def set_group(self, cloud_server_id, group):
        # 为云主机设置分组
        path = self._get_path("%s/group" % str(cloud_server_id))
        return self.post(path, {'group': group})

    def change_image(self, cloud_server_id, image_name):
        # 变更操作系统
        # cloud_server_id:
        path = self._get_path("%s/change_image" % str(cloud_server_id))
        return self.post(path, {'image': image_name})

    def attach_disk(self, cloud_server_id, volume_name):
        # 挂载云硬盘
        # volume_name:挂载的硬盘名
        path = self._get_path("%s/attach/%s" % (str(cloud_server_id), volume_name))
        return self.post(path)

    def detach_disk(self, cloud_server_id, volume_name):
        # 卸载云硬盘
        # cloud_server_id:云主机id
        # volume_name:卸载的硬盘名
        path = self._get_path("%s/detach/%s" % (str(cloud_server_id), volume_name))
        return self.post(path)

    def _cloud_server_simple_operations(self, operation, cloud_server_id):
        path = self._get_path("%s/%s" % (str(cloud_server_id), operation))
        return self.post(path)
