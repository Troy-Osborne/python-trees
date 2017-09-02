from __future__ import division
from PIL import Image,ImageDraw
from math import cos,sin,pi
class flower:
        def __init__(self,PetalCount,PetalColour,CentreColour,CentreSize=.2):
                self.PetalCount=PetalCount
                self.PetalColour=PetalColour
                self.CentreColour=CentreColour
                self.CentreSize=CentreSize
        def frontview(self,Res1d):
                petals=[]
                (W,H)=(Res1d,Res1d)
                im=Image.new("RGB",(W,H),(0,0,0))
                dr=ImageDraw.Draw(im)
                PC=self.PetalCount/2
                PL=1-self.CentreSize
                MID=(W/2,H/2)
                for i in range(7200):
                        ang=i/3600*pi
                        PV=self.CentreSize+abs(sin(ang*PC))*PL
                        pos=(MID[0]+cos(ang)*W/2*PV,MID[1]+sin(ang)*H/2*PV)
                        petals.append(pos)
                dr.polygon(petals,fill=self.PetalColour)
                dr.ellipse((MID[0]-MID[0]*self.CentreSize,MID[1]-MID[1]*self.CentreSize,MID[0]+MID[0]*self.CentreSize,MID[1]+MID[1]*self.CentreSize),fill=self.CentreColour)
                return im
flower(6,(160,120,170),(96,56,16),.3).frontview(1000).show()
