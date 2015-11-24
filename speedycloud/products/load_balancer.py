# -*- coding: utf-8 -*-
from speedycloud.products import AbstractProductAPI


class LoadBalancerAPI(AbstractProductAPI):
    BASE_PATH = '/api/v1/products/load_balancers/'

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def list(self):
        return self.post(self.BASE_PATH)

    def create_load_balance(self, available_zone, isp, bandwidth):
        # 创建负载均衡
        configurations = {
            # 可用数据中心
            'az': available_zone,
            # 数据中心支持的网络运营商
            'isp': isp,
            # 带宽
            'bandwidth': bandwidth,
        }
        path = self._get_path("provision")
        return self.post(path, configurations)

    def add_backend_cloud_server(self, load_balancer_id, cloud_server_id, weight, ip_address):
        params = {
            # 云主机id
            'cloud_server_id': cloud_server_id,
            # 权重
            'weight': weight,
            # ip地址
            'ip_address': ip_address,
        }
        path = self._get_path(str(load_balancer_id) + '/backends/add')
        return self.post(path, params)

    def add_backend_database(self, load_balancer_id, database_id, weight, ip_address):
        params = {
            # 数据库id
            'database_id': database_id,
            # 权重
            'weight': weight,
            # ip地址
            'ip_address': ip_address,
        }
        path = self._get_path(str(load_balancer_id) + '/backends/add')
        return self.post(path, params)

    def add_backend_cache(self, load_balancer_id, cache_id, weight, ip_address):
        params = {
            # 缓存id
            'database_id': cache_id,
            # 权重
            'weight': weight,
            # ip地址
            'ip_address': ip_address,
        }
        path = self._get_path(str(load_balancer_id) + '/backends/add')
        return self.post(path, params)

    def update_backend(self, load_balancer_id, back_id, weight, ip_address):
        # load_balancer_id:负载均衡id
        # back_id:后端服务器id
        path = self._get_path(str(load_balancer_id) + '/backends/' + str(back_id) + '/update')
        params = {
            # 权重
            'weight': weight,
            # ip地址
            'ip_address': ip_address,
        }
        return self.post(path, params)

    def delete_backend(self, load_balancer_id, back_id):
        # load_balancer_id:负载均衡id
        # back_id:后端服务器id
        path = self._get_path(str(load_balancer_id) + '/backends/' + str(back_id) + '/delete')
        return self.post(path)

    def add_application(self, load_balancer_id, frontend, backend, protocol, strategy, check_interval, rise_times,
                        fall_times):
        # load_balancer_id:负载均衡id
        params = {
            # 前端端口
            'frontend': frontend,
            # 后端端口
            'backend': backend,
            # 协议
            'protocol': protocol,
            # 负载均衡策略
            'strategy': strategy,
            # 健康检查间隔
            'check_interval': check_interval,
            # 下线监测阀值
            'rise_times': rise_times,
            # 在线监测阀值
            'fall_times': fall_times
        }
        path = self._get_path(str(load_balancer_id) + '/applications/add')
        return self.post(path, params)

    def detail(self, load_balancer_id):
        # load_balancer_id:负载均衡id
        path = self._get_path(str(load_balancer_id))
        return self.post(path)

    def update_application(self, load_balancer_id, application_id, frontend, backend, protocol, strategy,
                           check_interval, rise_times, fall_times):
        # load_balancer_id:负载均衡id
        # application_id:应用id
        params = {
            # 前端端口
            'frontend': frontend,
            # 后端端口
            'backend': backend,
            # 协议
            'protocol': protocol,
            # 负载均衡策略
            'strategy': strategy,
            # 健康检查间隔
            'check_interval': check_interval,
            # 下线监测阀值
            'rise_times': rise_times,
            # 在线监测阀值
            'fall_times': fall_times
        }
        path = self._get_path(str(load_balancer_id) + '/applications/' + str(application_id) + '/update')
        return self.post(path, params)

    def delete_application(self, load_balancer_id, application_id):
        # load_balancer_id:负载均衡id
        # application_id:应用id
        path = self._get_path(str(load_balancer_id) + '/applications/' + str(application_id) + '/delete')
        return self.post(path)
