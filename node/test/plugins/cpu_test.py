# -*- coding: utf-8 -*-
from node.test.base_test import BaseTestCase
from node.plugins.cpu import Plugin
from mock import Mock, patch

class CPUTest(BaseTestCase):

    def set_up_mock(self, filemock):
        fs_mock = Mock()
        filemock.return_value = fs_mock
        fs_mock.read.return_value = '0.12 0.16 0.23 1/123 3444'
        data = Plugin.data()
        return data

    @patch('__builtin__.file')
    def test_plugin_open_loadavg(self, filemock):
        fs_mock = Mock()
        filemock.return_value = fs_mock
        fs_mock.read.return_value = '0.12 0.16 0.23 1/123 3444'
        Plugin.data()
        filemock.assert_called_with('/proc/loadavg')

    @patch('__builtin__.file')
    def test_plugin_get_correct_cpu_load_values(self, filemock):
        data = self.set_up_mock(filemock)
        self.assertEqual(data['load_1'], 0.12)
        self.assertEqual(data['load_5'], 0.16)
        self.assertEqual(data['load_15'], 0.23)

    @patch('__builtin__.file')
    def test_plugin_get_correct_load_5_value(self, filemock):
        data = self.set_up_mock(filemock)
        self.assertEqual(data['load_5'], 0.16)

    @patch('__builtin__.file')
    def test_plugin_generate_correct_output(self, filemock):
        data = self.set_up_mock(filemock)
        self.assertTrue('load_1' in data)
        self.assertTrue('load_5' in data)
        self.assertTrue('load_15' in data)