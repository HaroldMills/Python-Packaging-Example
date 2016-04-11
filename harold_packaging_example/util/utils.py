import os.path

import yaml


def _load_translations():
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, 'translations.yaml')
    with open(file_path, 'rt') as file_:
        text = file_.read()
    return yaml.load(text)


_translations = _load_translations()


def translate(s):
    return _translations.get(s, s)
    