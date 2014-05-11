#! /usr/bin/python
# -*- coding: utf-8 -*-

import string
from types import *

#nomFich="sample.csv"
#nomFich="sample-coords.csv"
#nomFich="sample-short.csv"
nomFich="geoflar-reduced-sansCorse.csv"
outFich="geoflar-coord-pop.lat.csv"
#outFich="geoflar-coord-pop.long.csv"

def avg(pouet):
 somme = 0
 lenLi = len(pouet)
 for x in pouet:
  somme+=x[0]
 print somme/lenLi

def Eastmost(myset):
# file = open(nomFich, 'r')
# set = file.readline()
 set0 = myset[0]
 xcoords = []
 for x in set0:
  xcoords += [x[0]]
 print max(xcoords)
# file.close()

def Eastmost():
 file = open(nomFich, 'r')
 file2 = open(outFich, 'w')
 line = file.readline()
 stripline = line.strip()
 while stripline:
  blob = stripline.split(";")
#  print blob
  blub = blob[0].split(":")[2]
#  print blub
#  print "StripedLine: "+stripline
  stripline2 = blub.replace('[', "").replace(']', "").replace("}", "").replace(", ", ",")
#  print "StripedLine2: "+stripline2
  set0 = stripline2.split(",")
#  set0Bis = set0.replace(" ", "")
#  print set0
  setX = []
  for i in range(0, len(set0), 2):
   setX+=[float(set0[i])]
#  print setX
  file2.write(str(max(setX))+" "+blob[1]+"\n")
  stripline = file.readline().strip()
 file.close()
 file2.close()


def Northmost():
 file = open(nomFich, 'r')
 file2 = open(outFich, 'w')
 line = file.readline()
 stripline = line.strip()
 while stripline:
  blob = stripline.split(";")
#  print blob
  blub = blob[0].split(":")[2]
#  print blub
#  print "StripedLine: "+stripline
  stripline2 = blub.replace('[', "").replace(']', "").replace("}", "").replace(", ", ",").replace('"', "")
#  print "StripedLine2: "+stripline2
  set0 = stripline2.split(",")
#  set0Bis = set0.replace(" ", "")
#  print set0
  setX = []
  for i in range(1, len(set0), 2):
   setX+=[float(set0[i])]
#  print setX
  file2.write(str(max(setX))+" "+blob[1]+"\n")
  stripline = file.readline().strip()
 file.close()
 file2.close()
