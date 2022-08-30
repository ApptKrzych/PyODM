import gdal
import osr 

file_name = './results/odm_orthophoto/odm_orthophoto.tif'
input_raster = gdal.Open(file_name)
proj = osr.SpatialReference(wkt=input_raster.GetProjection())
print(proj.GetAttrValue('AUTHORITY',1))

output_raster = './results/odm_orthophoto/odm_orthophoto.tif'
warp = gdal.Warp(output_raster,input_raster,dstSRS='EPSG:4326')
warp = None # Closes the files

input_raster = gdal.Open(file_name)
proj = osr.SpatialReference(wkt=input_raster.GetProjection())
print(proj.GetAttrValue('AUTHORITY',1))
