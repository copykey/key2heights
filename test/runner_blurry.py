import os
import sys

fs = os.listdir("out")
o = 0
for i in range(0, len(fs)):
	print("")
	print(fs[i])
	os.system("python3 is_blurry.py ./out/" + fs[i])
