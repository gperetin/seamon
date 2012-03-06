# -*- coding: utf-8 -*-
import os
import subprocess
import json

class PluginHandler(object):
    @staticmethod
    def plugins_list():
        list_dir = os.listdir('./plugins/')
        ret_val = []
        for filename in list_dir:
            if ((filename.endswith('.py')) and not filename == '__init__.py'):
                ret_val.append(os.path.splitext(filename)[0])     
        return ret_val

    @staticmethod
    def _get_plugin_data(plugin):
        try:
            output = subprocess.check_output('%s/plugins/%s.py' % (os.getcwd(), plugin)).strip()
            output = json.loads(output)
        except:
            output = False
        return output

    @staticmethod
    def get_data_from_all_plugins():
        data = {}
        for plugin in PluginHandler.plugins_list():
            plugin_data = PluginHandler._get_plugin_data(plugin)
            if not plugin_data == False:
                data.update({plugin: plugin_data})
        return json.dumps(data)
