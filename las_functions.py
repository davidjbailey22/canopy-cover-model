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

def array2raster(newRasterfn, rasterOrigin, pixelWidth, pixelHeight, array):
    # other vars
    nrows = las_points.nrows
    cols = 3
    rasterOrigin = (-123.25745, 45.43013)
    originX = 3
    originY = rasterOrigin[1]
    pixelWidth = 10
    pixelHeight = 10
    driver = gdal.GetDriverByName('GTiff')

    # create geotiff
    outRaster = driver.Create(dem, cols, nrows, 1, gdal.GDT_Byte)
    outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
    outband = outRaster.GetRasterBand(1)
    outband.WriteArray(array)
    outRasterSRS = osr.SpatialReference()
    outRasterSRS.ImportFromEPSG(4326)
    outRaster.SetProjection(outRasterSRS.ExportToWkt())
    outband.FlushCache()


def main(newRasterfn, rasterOrigin, pixelWidth, pixelHeight, array):
    reversed_arr = array[::-1]  # reverse array so the tif looks like the array
    array2raster(newRasterfn, rasterOrigin, pixelWidth, pixelHeight, reversed_arr)  # convert array to raster
