# -*- coding: utf-8 -*-
from node.test.base_test import BaseTestCase
from node.plugins.cpu import Plugin
from mock import Mock, patch

class CPUTest(BaseTestCase):

    def set_up_mock(self, osmock):
        osmock.return_value = (0.12, 0.16, 0.23)
        data = Plugin.data()
        return data

    @patch('os.getloadavg')
    def test_plugin_get_correct_cpu_load_values(self, osmock):
        data = self.set_up_mock(osmock)
        self.assertEqual(data['load_1'], 0.12)
        self.assertEqual(data['load_5'], 0.16)
        self.assertEqual(data['load_15'], 0.23)

    @patch('os.getloadavg')
    def test_plugin_get_correct_load_5_value(self, osmock):
        data = self.set_up_mock(osmock)
        self.assertEqual(data['load_5'], 0.16)

    @patch('os.getloadavg')
    def test_plugin_generate_correct_output(self, osmock):
        data = self.set_up_mock(osmock)
        self.assertTrue('load_1' in data)
        self.assertTrue('load_5' in data)
        self.assertTrue('load_15' in data)