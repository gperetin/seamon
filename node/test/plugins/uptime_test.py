# -*- coding: utf-8 -*-
from node.test.base_test import BaseTestCase
from node.plugins.uptime import Plugin
from mock import Mock, patch

class UptimeTest(BaseTestCase):

    def set_up_mock(self, filemock):
        fs_mock = Mock()
        filemock.return_value = fs_mock
        fs_mock.readline.return_value = '344.12 422.12\n'
        data = Plugin.data()
        return data

    @patch('__builtin__.file')
    def test_plugin_open_uptime_file(self, filemock):
        fs_mock = Mock()
        filemock.return_value = fs_mock
        fs_mock.readline.return_value = '342.11 423.12\n'
        Plugin.data()
        filemock.assert_called_with('/proc/uptime')

    @patch('__builtin__.file')
    def test_plugin_correct_parse_uptime_file(self, filemock):
        data = self.set_up_mock(filemock)
        self.assertEqual(data, 344.12)

    @patch('__builtin__.file')
    def test_plugin_generate_correct_output(self, filemock):
        data = self.set_up_mock(filemock)
        self.assertTrue(isinstance(data, float))
