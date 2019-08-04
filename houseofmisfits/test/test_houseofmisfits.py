"""
This file is in place to make sure commits don't suddenly break the server bots.

"""
import os
import unittest

import yaml


class TestHouseOfMisfits(unittest.TestCase):

    def test_valid_yaml_syntax(self):
        rules_dir = os.getenv('WORKSPACE') + '/rules'
        for file in os.listdir(rules_dir):
            with open(rules_dir + '/' + file, 'r') as yaml_file:
                try:
                    yaml.safe_load(yaml_file)
                except Exception as e:
                    self.fail("Uh oh, looks like the rules file {} has a bad syntax.\n\nException:\n{}".format(file, e))
