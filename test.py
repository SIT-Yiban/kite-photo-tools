# import os
#
# import toml
#
# config_file = 'config.toml'
# if not os.path.exists(config_file):
#     open(config_file, 'w')
# filename = os.path.basename('images/pyq2.png')
# t = os.path.splitext(filename)
# print(t[0])
# file = toml.load(config_file)
# file[1] = 2
# print(file)
# print(file.get('pyq1'))
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--config-file',default='config.toml',type=str,help='photo locate config')
# parser.add_argument('--source',required=True,type=str,help='image-path')
# parser.add_argument('--content',required=True,type=str,help='association name')
# arc =  parser.parse_args()
# print(arc.source)
# print(arc.config_file)
# print(arc.content)
