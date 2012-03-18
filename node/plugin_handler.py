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
            # TODO: maybe extract this to some config
            # currently, plugins dir MUST be in same dir as plugin_handler
            this_dir = os.path.dirname(__file__)
            output = subprocess.check_output('%s/plugins/%s.py' % (this_dir, plugin)).strip()
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
