# -*- coding: utf-8 -*-
from node.test.base_test import BaseTestCase
from node.plugin_handler import PluginHandler
from mock import Mock, patch

class PluginHandlerTest(BaseTestCase):
    @patch('os.listdir')
    def test_detect_correct_number_of_plugins(self, dirlist):
        dirlist.return_value = ['memory.py', 'cpu.py', '__init__.py']
        self.assertEqual(len(PluginHandler.plugins_list()), 2)

    @patch('os.listdir')
    def test_detect_right_plugins(self, dirlist):
        dirlist.return_value = ['memory.py', 'disk.py', '__init__.py']
        self.assertTrue('memory' in PluginHandler.plugins_list())
        self.assertTrue('disk' in PluginHandler.plugins_list())

    def test_execute_right_plugin(self):
        # TODO: sedlanje :); treba mockat subprocess
        data = PluginHandler._get_plugin_data('memory')
        self.assertTrue('memory_total' in data)

    @patch.object(PluginHandler, 'plugins_list')
    @patch.object(PluginHandler, '_get_plugin_data')
    def test_node_collect_data_from_all_plugins(self, _get_plugin_data, plugins_list):
        plugin = Mock()
        plugins_list.return_value = [plugin]
        PluginHandler.get_data_from_all_plugins()
        _get_plugin_data.assert_called_with(plugin)