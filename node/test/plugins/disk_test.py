# -*- coding: utf-8 -*-
from node.test.base_test import BaseTestCase
from node.plugins.disk import Plugin
from mock import Mock, patch

class CPUTest(BaseTestCase):

    def set_up_mock(self, subprocessmock):
        subprocessmock.return_value = """
Filesystem           1K-blocks      Used Available Use%% Mounted on
/dev/sda5             40116616   6168760  31910048  17% /
/dev/sda1                  145        32        54  29% /opt
udev                    473120        12    473108   1% /dev
none                    480128       160    47996"""
        data = Plugin.data()
        return data

    @patch('subprocess.check_output')
    def test_plugin_call_df(self, subprocessmock):
        Plugin.data()
        subprocessmock.assert_called_with('df')

    @patch('subprocess.check_output')
    def test_plugin_get_correct_disk_list(self, subprocessmock):
        data = self.set_up_mock(subprocessmock)
        self.assertEqual(data[0]['name'], '/dev/sda5')
        self.assertEqual(data[1]['name'], '/dev/sda1')
        self.assertEqual(len(data), 2)

    @patch('subprocess.check_output')
    def test_plugin_get_correct_dev_sda1_value(self, subprocessmock):
        data = self.set_up_mock(subprocessmock)
        self.assertEqual(data[1]['used'], 32)
        self.assertEqual(data[1]['percent'], '29%')
        self.assertEqual(data[1]['mount'], '/opt')
        self.assertEqual(data[1]['available'], 54)