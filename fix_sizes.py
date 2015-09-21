import maya.cmds as mc

#file_list = "C:/projects/Perforce/Alex_Workspace1/Asset-Master/Michael Foods/Michael Foods Project Joey/Test Cell 1/Assets/HighRes/measurements.txt"
#file_dir = "C:/projects/Perforce/Alex_Workspace1/Asset-Master/Michael Foods/Michael Foods Project Joey/Test Cell 1/Assets/HighRes/"
file_list = "U:/Craig.LaMorte/Fix_size" #file path for the document containing the products and resizes
file_dir = "U:/Craig.LaMorte/Fix_size/models/" #file path for the maya files

product_keys = []
desired_heights = []
desired_widths = []
desired_depths = []


try:
    dimensions = open(file_list, "rb") #opens file with all the resizes
except IOError:
    print 'File path or document name is inccorect' #if it does not see the file then it closes
    exit()

for line in dimensions: #loops through document and breaks up sizes and key into lists
	try:
		fields = line.split()
		product_keys.append(fields[0] + '_hr')
		desired_heights.append(fields[1])
		desired_widths.append(fields[2])
		desired_depths.append(fields[3])
	except IndexError:
		break 
dimensions.close()

for i in range(len(product_keys)): #cycles through each maya file to change

	#gather values for current product
	product_key = product_keys[i]
	desired_height = float(desired_heights[i])
	desired_width = float(desired_widths[i])
	desired_depth = float(desired_depths[i])


	#construct the path to the file
	file_path = file_dir + product_key + '/' + product_key + '.mb'


	#open the file
	try:
	    mc.file(file_path, force = True, open = True)
	except RuntimeError: # if it does not see the maya files then it closes
	    print 'Could not find maya file ' + product_key
	    break

    #Set units to meters
	mc.currentUnit(linear = 'm')

    #select mesh
	mc.select(product_key)

	#fix scale factors (make them all 1
	mc.makeIdentity(apply = True, scale = True)

    #get the current size of the mesh
	object_width = mc.getAttr(product_key + '.boundingBoxSizeX')
	object_height = mc.getAttr(product_key + '.boundingBoxSizeY')
	object_depth = mc.getAttr(product_key + '.boundingBoxSizeZ')
	
    #figures out from its current size how much you need to resize it to get to desired size
	width_factor = desired_width / object_width
	height_factor = desired_height / object_height
	depth_factor = desired_depth / object_depth
	
    #Sets the size to equal desired size
	mc.setAttr (product_key + ".scaleX", width_factor)
	mc.setAttr(product_key + ".scaleY", height_factor)
	mc.setAttr(product_key + ".scaleZ", depth_factor)

    #freeze scale
	mc.makeIdentity(apply = True, scale = True)

    #close file
	mc.file(force = True, save = True )
