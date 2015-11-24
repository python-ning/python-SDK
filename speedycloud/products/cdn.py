# -*- coding: utf-8 -*-
from speedycloud.products import AbstractProductAPI
import json
from datetime import datetime


class CDNAPI(AbstractProductAPI):
    BASE_PATH = "/api/v1/products/cdns/"

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def list(self):
        # 域名列表
        return self.get(self.BASE_PATH)

    def detail(self, id):
        # 域名信息
        path = self._get_path(id)
        return self.get(path)

    def modify(self, id, domain, origin_ip, cache_type, cdn_type='cdn_type_static', cache_rules=None,
               cdn_status='CNAME'):
        # 修改域名
        path = self._get_path("%s/modify" % str(id))
        params = {
            'domain': domain,
            'origin_ip': origin_ip,
            'cache_type': cache_type,
            'cdn_type': cdn_type,
            'cache_rules': cache_rules,
            'cdn_status': cdn_status
        }
        return self.post(path, {'params': json.dumps(params)})

    def pause(self, id):
        # 暂停域名加速
        path = self._get_path("%s/pause" % id)
        return self.post(path)

    def resume(self, id):
        # 恢复域名加速
        path = self._get_path("%s/resume" % id)
        return self.post(path)

    def logs(self, id, start_date, end_date):
        # 日志文件列表
        params = {
            'id': id,
            'start_date': datetime.strftime(start_date, '%Y-%m-%d'),
            'end_date': datetime.strftime(end_date, '%Y-%m-%d')
        }
        path = self._get_path("%s/logs" % id)
        return self.post(path, params)

    def refresh_list(self):
        # 刷新纪录列表
        path = self._get_path("refreshes/")
        return self.get(path)

    def add_refresh(self, refresh_type, refresh_url_list):
        # 添加文件目录刷新
        path = self._get_path("refreshes/add_refresh")
        params = {
            'refresh_type': refresh_type,
            'refresh_urls': json.dumps(refresh_url_list)
        }
        return self.post(path, params)

    def redo_refresh(self, refresh_id):
        # 重新刷新文件目录
        path = self._get_path("refreshes/redo")
        params = {"refresh_id": refresh_id}
        return self.post(path, params)

    def delete_refresh(self, id_list):
        # 删除刷新纪录
        path = self._get_path("refreshes/delete")
        params = {"id_list": json.dumps(id_list)}
        return self.post(path, params)

    def preload_list(self):
        # 预加载纪录列表
        path = self._get_path("preload/")
        # params = {"type": json.dumps(preload_list_type)}
        return self.get(path)

    def add_preload(self, preload_urls):
        # 添加文件预加载
        path = self._get_path("preload/add_preload")
        params = {
            'preload_urls': json.dumps(preload_urls),
        }
        return self.post(path, params)

    def redo_preload(self, preload_id):
        # 重新提交文件预加载
        path = self._get_path("preload/redo")
        params = {"preload_id": preload_id}
        return self.post(path, params)

    def delete_preload(self, id_list):
        # 删除预加载纪录
        path = self._get_path("preload/delete")
        params = {"id_list": json.dumps(id_list)}
        return self.post(path, params)

    def set_group(self, id, group):
        # 为域名设置分组
        path = self._get_path("%s/group" % str(id))
        return self.post(path, {'group': group})

    def get_bandwidth(self, ids, duration=None):
        # 获取带宽数据
        params = {
            'ids': ids,
            'duration': duration
        }
        path = self._get_path("get_bandwidth")
        return self.post(path, params)
