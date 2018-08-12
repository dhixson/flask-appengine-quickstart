import os
import subprocess
import sys
import time
import re
import fileinput

# Class: Controller
# Purpose: Create Controllers
# Created By: Dane Hixson
# Last Updated By: Dane Hixson
# Last Updated: 11/10/2017
class Controller(object):
    """Run unit tests in the tests directory"""

    def __init__(self, command):
        self.package_path = os.path.dirname(os.path.realpath(__file__)) + '/../../app/src/controllers/__init__.py'
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/../../app/src/controllers/'
        """Gather command and execute the proper test function"""
        if command is None:
            print "Error: no controller command given"
            return None
        elif command == "create":
            try:
                self.create(sys.argv[2])
            except IndexError:
                print "Error: no new controller name given"
                return None
        else:
            print "Error: Not a valid controller commad"

    def create(self, name):
        """Create a new controller file in the app/controllers directory"""
        file_bin = os.path.dirname(os.path.realpath(__file__)) + '/../../assets/templates/'
        with open(file_bin + 'controller.py') as f:
            template = f.read().replace('<_name_>', name)
        if template == "":
            print "File does not exist"
            return None
        with open(self.path + name + "_controller"'.py', 'w') as w:
            w.write(template)
        newlines = ""
        for line in fileinput.input(self.package_path):
            if "# ==== End Controller Imports ====" in line:
                newlines += "import %s_controller" % name
                newlines += "\n# ==== End Controller Imports ===="
        with open(self.package_path, 'w') as f:
            f.write(newlines)
        print "Controller %s created" % name

    @staticmethod
    def options():
        """Display command options"""
        print "###Controllers###"
        print "controller:create <name> => creates a new controller and registers its blueprint"
        print ""
