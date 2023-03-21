#!/usr/bin/env python3

import sys

from osgeo.gdal import UseExceptionsAllModules, deprecation_warn

# import osgeo_utils.gdalcompare as a convenience to use as a script
from osgeo_utils.gdalcompare import *  # noqa
from osgeo_utils.gdalcompare import main

UseExceptionsAllModules()

deprecation_warn("gdalcompare")
sys.exit(main(sys.argv))
