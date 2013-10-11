import png
import math

width = raw_input("What is the total width of your pattern? > ")
height = raw_input("What is the total height of your pattern? > ")
print("No we are going to look at your swatch.")
swidth = raw_input("What is the measure width of your swatch? > ")
scol = raw_input("How many stitches is that? > ")
sheight = raw_input("What is the measure height of your swatch? > ")
srow = raw_input("How many rows is that? > ")

wratio = float(scol)/float(swidth) #stitches/unit
hratio = float(srow)/float(sheight) #rows/unit
totalstitches = int(math.ceil(wratio * float(width))) #total number of stitches per row
totalrows = int(math.ceil(hratio * float(height))) #total number of rows
ratio = hratio/wratio #ratio of height/width
pixwidth = 40 #standard width of a cell
pixheight = pixwidth / ratio #(adjusted) height of a cell
bordersize = 2
picwidth = int(math.ceil(totalstitches * pixwidth + bordersize))
picheight = int(math.ceil(totalrows * pixheight + bordersize))

print("Your pattern is going to be "+ str(totalstitches) +" stitches wide and "+ str(totalrows) + " rows high.")
path = raw_input("What name do you want to give the resulting grid? > ")

print("The picture is going to be " + str(picheight) + " pixels high")
print("And "+ str(picwidth) +" pixels wide")

print("Calculation: " + str(totalstitches) + " stitches * " + str(pixwidth) + " cellwidth + " + str(totalstitches+1) + " * " + str(bordersize) + " = " + str(picwidth))
print("Height: " + str(totalrows) + " rows * " + str(pixheight) + " cellheight + " + str(totalrows+1) + " * " + str(bordersize) + " = " + str(picheight))

pixels = list()
for i in range (0,picheight) :
	#build rows
	pixels.append([])
	if i%pixheight<bordersize:
		#this row should be black entirely
		for c in range(0,picwidth) :
			pixels[i].append(0) #black
			pixels[i].append(255)
	else:
		for c in range(0,picwidth) :
			#build columns
			if c%pixwidth<bordersize:
				pixels[i].append(0) #black
				pixels[i].append(255)
			else:
				pixels[i].append(255) #black
				pixels[i].append(0)

png.from_array(pixels, 'LA').save(path)
