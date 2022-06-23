import json
import glob
from tqdm import tqdm
import os
import sys
# import urllib2

contract_dir = '/home/richael/oyente-master/oyente/contract1'

cfiles = glob.glob(contract_dir+'/*.sol')

# cjson = {}
#
# print("Loading contracts...")
#
# for cfile in tqdm(cfiles):
# 	cjson.update(json.loads(open(cfile).read()))

results = {}
missed = []

print("Running analysis...")

# contracts = cjson.keys()

# if os.path.isfile('results.json'):
# 	old_res = json.loads(open('results.json').read())
# 	old_res = old_res.keys()
# 	contracts = [c for c in contracts if c not in old_res]

cores = 0
job = 0

# if len(sys.argv) >= 3:
# 	cores = int(sys.argv[1])
# 	job = int(sys.argv[2])
# 	cfiles = cfiles[(len(cfiles)/cores)*job:(len(cfiles)/cores)*(job+1)]
# 	print("Job %d: Running on %d contracts..." % (job, len(cfiles)))

for c in tqdm(cfiles):

	os.system('python3 oyente.py -ll 200 -s ' + c+' -j')
	# c = c[c.rfind('/')+1:]
	# file = 'contract/' + c
	# try:
	#
	# 	# results[c] = json.loads(open(file+'.json').read())
	# except:
	# 	missed.append(c)
	# with open('results.json', 'a') as of:
	# 	of.write(json.dumps(results[c], indent=1))
	# with open('missed.json', 'w') as of:
	# 	of.write(json.dumps(missed, indent=1))
	# urllib2.urlopen('https://dweet.io/dweet/for/oyente-%d-%d?completed=%d&missed=%d&remaining=%d' % (job,cores,len(results),len(missed),len(cfiles)-len(results)-len(missed)))

print ("Completed.")
