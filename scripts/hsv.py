import Image
import sys


def toHSV(im):
	hsv = Image.new("RGB", im.size)
	pix = im.load()
	hsvPix = hsv.load()
	epsilon = 0.00001
	for y in range(im.size[1]):
		for x in range(im.size[0]):
			r,g,b =  pix[x, y]
			r,g,b = [v/255.0 for v in (r,g,b)]
			#print r,g,b	
			cmax = max(r,g,b)
			cmin = min(r,g,b)		
			delta = cmax-cmin
			#print cmin, cmax, delta			
			h = 0
			if delta > 0:
				if cmax >= r-epsilon and cmax <= r+epsilon :
					v = (g-b)/delta
					h = 60*(v-6*(int(v)/6))
				elif cmax >= g-epsilon and cmax <= g+epsilon :
					h = 60*(((b-r)/delta) +2)
				else:
					h = 60*(((r-g)/delta) +4)
			s = 0
			if cmax > 0:
				s = delta/cmax
			v = cmax
			#print h,s,v
			hsvPix[x,y] = (int(h*2.55/3.6), int(s*255),int(v*255))
	return hsv

def toRGB(im):
	rgb = Image.new("RGB", im.size)
	pix = im.load()
	rgbPix = rgb.load()
	epsilon = 0.00001
	for Y in range(im.size[1]):
		for X in range(im.size[0]):
			h,s,v = pix[X,Y]
			h*= 3.6/2.55
			s = s/255.0
			v = v/255.0
			c = v*s
			val = h/60.0
			x = c*(1.0- abs((val-2*(int(val)/2)) - 1.0))
			m = v-c		
			r,g,b = c,x,0
			if 60<=h and h<120:  r,g,b = x,c,0
			elif 120<=h and h<180:  r,g,b = 0,c,x
			elif 180<=h and h<240:  r,g,b = 0,x,c
			elif 240<=h and h<300:  r,g,b = x,0,c
			elif 300<=h :  r,g,b = c,0,x
			r,g,b = [int((p+m)*255) for p in (r,g,b) ]
			rgbPix[X,Y] = r,g,b
	return rgb


if __name__ == "__main__":
	im = Image.open(sys.argv[1])
	im.show()
	hsv = toHSV(im)
	hsv.show()
	rgb = toRGB(hsv)
	rgb.show()
