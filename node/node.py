# -*- coding: utf-8 -*-
import os
import subprocess

class Node(object):
    def listPlugins(self):
        dirList = os.listdir('./plugins/')
        retVal = []
        for filename in dirList:
            if ((filename.endswith('.py')) and not filename == '__init__.py'):
                retVal.append(os.path.splitext(filename)[0])     
        return retVal

    def getPluginData(self, plugin):
        output = False
        if plugin in self.listPlugins():
            try:
                output = subprocess.check_output('./plugins/%s.py' % plugin)
            except:
                pass
        return output