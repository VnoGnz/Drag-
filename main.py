import sys,shutil

runtah=["vnognz/__pycache__","modul/__pycache__","wibu/__pycache__","vnognz/ngewe/__pycache__"]

if sys.version[0]!="3":
	exit(" ! harap gunakan python3")

from vnognz import awokawokawok
try: [shutil.rmtree(x) for x in runtah]
except: pass
awokawokawok()
