from __future__ import division
from math import cos,sin,pi
from random import random
from PIL import Image,ImageDraw
def npoint(branch,dist):
	p1=branch[0]
	p2=branch[1]
	return (p1[0]+(p2[0]-p1[0])*dist,p1[1]+(p2[1]-p1[1])*dist)
	
def leafdir(count,leaf,direction,spread=pi/2):
	if count%2:
		b=-.5
	else:
		b=1/count/2-.5
	return(leaf/count+b)*spread+direction

def makebranches2d(branch,length,ang,rule,pattern,n,it):
	if it:
		out=[]
		for i in range(rule[0]):
			curang=ang+rule[1][i]
			curlength=length*rule[2][i]
			dist=rule[3][i]
			point=npoint(branch,dist)
			curbranch=(point,(point[0]+cos(curang)*curlength,point[1]+sin(curang)*curlength),curang)
			out.append([curbranch]+makebranches2d(curbranch,curlength,curang,pattern[n%len(pattern)],pattern,n+1,it-1))
		return out
	else:
		return [None]
		
def cartoonleaf(point,ang,dr,scale):
	for i in range(scale):
		e=(30/scale*i*4)**.6-20/scale*i/1.5
		for i2 in range(int(e)):
			i2=i2-e/2
			p=(point[0]+cos(ang)*i+cos(ang-pi/2)*i2,point[1]+sin(ang)*i+sin(ang-pi/2)*i2)
			dr.point(p,fill=(90,164,80))
		
	
		
class Tree_2d_Cartoon:
	def __init__(self,length,startingangle,pattern,leaf,leafcount=4,iterations=8):
		self.trunk=((0,0),(cos(startingangle)*length,sin(startingangle)*length))
		self.branches=[self.trunk]+makebranches2d(self.trunk,length,startingangle,pattern[0],pattern,0,iterations)
		self.leaf=leaf
		self.leafcount=leafcount
		self.length=length
	def draw(self,colour,size):
		im=Image.new("RGBA",size,(0,0,0,255))
		dr=ImageDraw.Draw(im)
		start=(size[0]/2,size[1])
		def drawbranch(branch):
			dr.line((branch[0][0][0]+start[0],branch[0][0][1]+start[1],branch[0][1][0]+start[0],branch[0][1][1]+start[1]),width=2,fill=colour)
			if branch[1]:
				for i in branch[1:]:
					drawbranch(i)
			else:
				for i in range(self.leafcount):
					self.leaf((lambda x:(x[0]+start[0],x[1]+start[1]))(branch[0][1]),leafdir(self.leafcount,i,branch[0][2]),dr,self.length/10)
		drawbranch(self.branches)
		return im

def randompattern():
	out=[]
	for i in range(int(random()*5+1)):
		num=int(random()*3+1)
		pattern=[num,[pi/(int(random()*12)+1)*(-1 if random()>.5 else 1) for f in range(num)],[random() for f in range(num)],[random() for f in range(num-1)]+[1]]
		out.append(pattern)
	return out
#[2,[-.1,.1],[.5,.5],[1,.9]]
def randomtree(size):
	pattern=randompattern()
	return Tree_2d_Cartoon(size,-pi/2,pattern,cartoonleaf)
for i in range(1000):
	s=str(i)
	randomtree(160).draw((190,168,128),(640,480)).save('tree/'+'0'*(4-len(s))+s+'.png')
