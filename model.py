"""
canopy cover model with lidar point clouds, dems and naip imagery as inputs
By D. Bailey
"""

import gdal, ogr, os, osr
from liblas import file
from liblas import header
import numpy
#import pdal
#from las_conversions import las_vars
import las_functions

def ccmodel():

    # input variables
    dem = "/Users/davidbailey/repos/github/geo/canopy-cover-model/test_data/dem.geotiff"
    dsm = "/Users/davidbailey/repos/github/geo/canopy-cover-model/test_data/dsm.geotiff"
    point_cloud_bare = '/Users/davidbailey/repos/github/geo/canopy-cover-model/test_data/points.las'
    point_cloud_first = ''
    naip = ""
    clip_boundary = ""
    rasterOrigin = (-123.25745, 45.43013)
    pixelWidth = 10
    pixelHeight = 10

    ## create DEM from bare earth las points

    # las to numpy array
    array = las_functions.las2narray(point_cloud_bare)

    # numpy array to geotiff (DEM)
    las_functions.array2raster(dem, rasterOrigin, pixelWidth, pixelHeight, array)

    ## create DSM from first return las points

    # las to numpy array

    # numpy array to geotiff (DSM)

    # subtract DSM from DEM

    # pull values > 10m

    ### create land cover type GeoTiff from NAIP imagery ###

    '''
    # convert MrSID file to GeoTIFF
    naip = gdal.Open('/Users/davidbailey/Downloads/output.idw.asc') #'/Users/davidbailey/Downloads/ortho_1-2_1n_s_co041_2011_1/ortho_1-2_1n_s_co041_2011_1.sid'
    format = "GTiff"
    driver = gdal.GetDriverByName(format)
    geotiff = '/Users/davidbailey/Downloads/output.tif'
    output_naip_geotiff = driver.CreateCopy(geotiff, naip, 0)

    naip = None #Properly close the datasets to flush to disk
    geotiff = None
    '''

    # pull out all but green values

    ### merge tree height GeoTiff with land cover GeoTiff ###

ccmodel()
