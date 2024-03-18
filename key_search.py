import yaml
import re

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


# define YAML file.
example = 'example.yml'

# load file
with open(example, 'r') as f:
    things = yaml.load(f, Loader=Loader)


# define target key search
target = 'target'
       


def key_search(d):
    for k, v in d.items():
        if target in k:
            print(True)
        else:
            if isinstance(v, dict):
                print(False)
                key_search(v)

    




