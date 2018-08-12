from lib.spark.Test import Test
from lib.spark.Controller import Controller
import sys



# Class: Spark
# Purpose: The main spark driver
# Written By: Dane Hixson
# Last updated By: Dane Hixson
# Last updated: 02/11/2016
class Spark(object):
    """Run commands to aid in development"""

    def __init__(self, command):
        """Initialize options and execute command"""
        options = {
            'test': Test,
            'controller': Controller,
        }

        comm = command.split(':')
        if len(comm) > 2:
            print "Error: too many arguments provided"
            return None
        elif len(comm) is 0:
            print options
            return None
        elif len(comm) is 1:
            comm.append(None)
        options[comm[0]](comm[1])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        Test.options()
        Controller.options()
    else:
        Spark(sys.argv[1])
