#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Manage.py script for the CarPool web application."""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carpool.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

#check 
# team CRESCENT TITAN
