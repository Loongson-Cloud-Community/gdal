#!/usr/bin/env python3

import sys

from osgeo.gdal import UseExceptionsAllModules, deprecation_warn

# import osgeo_utils.gdal_merge as a convenience to use as a script
from osgeo_utils.gdal_merge import *  # noqa
from osgeo_utils.gdal_merge import main

UseExceptionsAllModules()

deprecation_warn("gdal_merge")
sys.exit(main(sys.argv))
