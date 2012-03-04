# -*- coding: utf-8 -*-
from node.test.base_test import BaseTestCase
from node.plugins.hostname import Plugin
from mock import Mock, patch

class HostnameTest(BaseTestCase):

    def set_up_mock(self, filemock):
        fs_mock = Mock()
        filemock.return_value = fs_mock
        fs_mock.readline.return_value = 'test_hostname'
        data = Plugin.data()
        return data

    @patch('__builtin__.file')
    def test_plugin_open_hostname_file(self, filemock):
        fs_mock = Mock()
        filemock.return_value = fs_mock
        fs_mock.read.return_value = 'test_hostname'
        Plugin.data()
        filemock.assert_called_with('/proc/sys/kernel/hostname')

    @patch('__builtin__.file')
    def test_plugin_correct_pase_hostname_file(self, filemock):
        data = self.set_up_mock(filemock)
        self.assertEqual(data, 'test_hostname')

    @patch('__builtin__.file')
    def test_plugin_generate_correct_output(self, filemock):
        data = self.set_up_mock(filemock)
        self.assertTrue(isinstance(data, str))
