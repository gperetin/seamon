# -*- coding: utf-8 -*-
from node.test.base_test import BaseTestCase
from node import plugins
from node.node import Node
from mock import Mock, patch

class NodeTest(BaseTestCase):
    @patch('os.listdir')
    def test_correct_number_of_plugins(self, dirlist):
        dirlist.return_value = ['memory.py', 'cpu.py', '__init__.py']
        node = Node()
        self.assertEqual(len(node.listPlugins()), 2)

    @patch('os.listdir')
    def test_node_detect_right_plugins(self, dirlist):
        dirlist.return_value = ['memory.py', 'disk.py', '__init__.py']
        node = Node()
        self.assertTrue('memory' in node.listPlugins())
        self.assertTrue('disk' in node.listPlugins())

    def test_node_check_if_plugin_exist_before_execute(self):
        node = Node()
        self.assertTrue(node.getPluginData('memory'))
        self.assertFalse(node.getPluginData('this_plugin_does_not_exist'))

    def test_node_execute_right_plugin(self):
        # TODO: sedlanje :); treba mockat subprocess
        node = Node()
        data = node.getPluginData('memory')
        self.assertTrue('memory_total' in data)