"""
functions for working with las file
By D. Bailey
"""

import gdal, ogr, os, osr
from liblas import file
from liblas import header
import numpy

def las_points(las_file):
    las_file = file.File(las_file, mode='r')
    header = las_file.header
    nrows = header.point_records_count
    return nrows

def las2narray(las_file):
    las_file = file.File(las_file, mode='r')
    for p in las_file:
        print p.x, p.y, p.z
