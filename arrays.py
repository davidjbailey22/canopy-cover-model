"""
converting arrays to raster types
By D. Bailey
"""

import gdal, ogr, os, osr
from liblas import file
from liblas import header
import numpy


def array2raster(nrows, dem, rasterOrigin, pixelWidth, pixelHeight, array):

    # array vars
    cols = 2
    originX = 3
    originY = rasterOrigin[1]
    driver = gdal.GetDriverByName('GTiff')
    rwidth = 10
    rheight = 10
    nBands = 2

    '''
    GALDriver::Create(
            const char * 	pszFilename,
            int 	nXSize,
            int 	nYSize,
            int 	nBands,
            GDALDataType 	eType,
            char ** 	papszOptions
            )
    '''

    # create geotiff
    outRaster = driver.Create(dem, cols, nrows, 1, gdal.GDT_Byte)
    #outRaster = driver.Create(dem, rwidth, rheight, 1, gdal.GDT_Byte)
    #outRaster = driver.Create(dem, rwidth, rheight, 1, dtype)
    #outRaster = driver.Create(dem, rwidth, rheight, 1, gdal.GDT_Byte)
    outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
    outband = outRaster.GetRasterBand(1)
    outband.WriteArray(array)
    outRasterSRS = osr.SpatialReference()
    outRasterSRS.ImportFromEPSG(4326)
    outRaster.SetProjection(outRasterSRS.ExportToWkt())
    outband.FlushCache()


def main(nrows, dem, rasterOrigin, pixelWidth, pixelHeight, array):
    reversed_arr = array[::-1]  # reverse array so the tif looks like the array
    array2raster(nrows, dem, rasterOrigin, pixelWidth, pixelHeight, reversed_arr)  # convert array to raster
