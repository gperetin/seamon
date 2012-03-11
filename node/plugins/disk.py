#!/usr/bin/python
import json
import subprocess

class Plugin():
    @staticmethod
    def data():
        data = subprocess.check_output('df')
        dict_data = []

        for line in data.split('\n'):
            if line.startswith('/'):
                name, size, used, available, percent, mount = line.strip().split()
                dict_data.append({
                    'name': name,
                    'size': int(size),
                    'used': int(used),
                    'available': int(available),
                    'percent': percent,
                    'mount': mount
                })

        return dict_data

def main():
    print json.dumps(Plugin.data())

if __name__ == '__main__':
    main()
