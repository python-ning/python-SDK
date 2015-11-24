# -*- coding: utf-8 -*-
from speedycloud.products import AbstractProductAPI


class RouterAPI(AbstractProductAPI):
    BASE_PATH = "/api/v1/products/routers"

    def _get_path(self, suffix):
        return "%s/%s" % (self.BASE_PATH, suffix)

    def list(self):
        path = self.BASE_PATH
        return self.get(path)

    def detail(self, id):
        path = self._get_path(str(id))
        return self.post(path)

    def edit_nat_role(self, id, port, protocol, target_ip, target_port):
        # 编辑NAT规则
        params = {
            'port': port,
            'protocol': protocol,
            'target_ip': target_ip,
            'target_port': target_port
        }
        path = self._get_path("%s/edit_nat" % str(id))
        return self.post(path, params)

    def delete_nat_role(self, id, port, protocol):
        # 删除NAT规则
        params = {
            'port': port,
            'protocol': protocol
        }
        path = self._get_path("%s/delete_nat" % str(id))
        return self.post(path, params)

    def create_nat_role(self, id, port, protocol, target_ip, target_port):
        # 添加NAT规则
        params = {
            'port': port,
            'protocol': protocol,
            'target_ip': target_ip,
            'target_port': target_port
        }
        path = self._get_path("%s/create_nat" % str(id))
        return self.post(path, params)

    def set_group(self, id, group_name):
        path = self._get_path("%s/set_group" % str(id))
        return self.post(path, {"group": group_name})

    def groups(self):
        path = self._get_path('groups')
        return self.get(path)

    def set_alias(self, id, alias):
        path = self._get_path("%s/alias" % str(id))
        return self.post(path, {'alias': alias})

    def stop(self, id):
        path = self._get_path("%s/stop" % str(id))
        return self.post(path)

    def start(self, id):
        path = self._get_path("%s/start" % str(id))
        return self.post(path)

    def jobs(self, id):
        path = self._get_path("%s/jobs" % str(id))
        return self.get(path)

    def support_features(self, id):
        path = self._get_path("%s/support_features" % str(id))
        return self.get(path)

    def join(self, id, network, ip, mask):
        netcfg = {
            'name': network,
            'ip': ip,
            'mask': mask
        }
        path = self._get_path("%s/join/%s" % (str(id), network))
        return self.post(path, netcfg)

    def toggle_private_network(self, id):
        # 默认内网开关
        path = self._get_path("%s/toggle_private_network" % str(id))
        return self.post(path)

    def reload(self, id):
        path = self._get_path("%s/reload" % str(id))
        return self.post(path)

    def rejoin(self, id, network, ip, mask):
        netcfg = {
            'name': network,
            'ip': ip,
            'mask': mask
        }
        path = self._get_path("%s/rejoin/%s" % (str(id), network))
        return self.post(path, netcfg)

    def leave(self, id, network):
        path = self._get_path("%s/leave/%s" % (str(id), network))
        return self.post(path)
