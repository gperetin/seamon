# -*- coding: utf-8 -*-
from node.test.base_test import BaseTestCase
from node.plugin_handler import PluginHandler
from node import service
import requests

class ServiceTest(BaseTestCase):
    def test_accepte_all_get_request(self):
        # TODO: problem s testiranjem jer za pokretanje su potrebne root ovlasti
        pass