from node.test.base_test import BaseTestCase
# -*- coding: utf-8 -*-
from node.plugins.memory import Plugin
from mock import Mock, patch
import subprocess

class MemoryTest(BaseTestCase):

    @patch('__builtin__.file')
    def test_plugin_open_meminfo(self, filemock):
        # fs_mock = Mock()
        # filemock.return_value = fs_mock
        # fs_mock.read.return_value = 'MemTotal: 1234 kB\nMemFree: 544 kB\nBuffers: 654 kB\n'
        # Plugin.data()
        # self.assertTrue(filemock.assert_called_with('/proc/meminfo'))
        pass

    def setUpMock(self, filemock):
        fs_mock = Mock()
        filemock.return_value = fs_mock
        fs_mock.read.return_value = 'MemTotal: 1234 kB\nMemFree: 544 kB\nBuffers: 654 kB\n'
        data = Plugin.data()
        return data

    @patch('__builtin__.file')
    def test_plugin_get_correct_memory_total_value(self, filemock):
        data = self.setUpMock(filemock)
        self.assertEqual(data['memory_total'], 1234)

    @patch('__builtin__.file')
    def test_plugin_get_correct_free_value(self, filemock):
        data = self.setUpMock(filemock)
        self.assertEqual(data['memory_free'], 544)

    @patch('__builtin__.file')
    def test_plugin_generate_correct_output(self, filemock):
        data = self.setUpMock(filemock)
        self.assertTrue('memory_free' in data)
        self.assertTrue('memory_total' in data)