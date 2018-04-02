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
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/../../app/controllers/'
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
        for line in fileinput.input(self.path + '../main.py'):
            if "# ==== End Controller Imports ====" in line:
                newlines += "from controllers.%s_controller import %s_controller as %s\n" % (3*(name,))
            if "# ==== End Controllers ====" in line:
                newlines += "app.register_blueprint(%s, url_prefix='/%s')\n" % (name, name.lower())
            newlines += line
        with open(self.path + '../main.py', 'w') as f:
            f.write(newlines)
        print "Controller %s created" % name
