import os
import sys

fs = os.listdir("inpv")
o = 0
for i in range(0, len(fs)):
	if ".png" in fs[i]:
		#st = fs[i].split("_")[2].split(".")[0]
		st = fs[i].split(".")[0]
		while len(st) < 6:
			st = "0" + st
		print(st)
		os.system("python3 opencv.py inpv/" + fs[i] + " " + st)
		o+=1
