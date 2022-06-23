import json
import glob
from tqdm import tqdm


# import urllib2

result_dir = '/home/richael/oyente-master/oyente/contract2'

result_files = glob.glob(result_dir + '/*.json')

# cjson = {}
#
# print("Loading contracts...")
#
# for cfile in tqdm(cfiles):
# 	cjson.update(json.loads(open(cfile).read()))

results = {}
result_final = {}

# contracts = cjson.keys()

# if os.path.isfile('results.json'):
# 	old_res = json.loads(open('results.json').read())
# 	old_res = old_res.keys()
# 	contracts = [c for c in contracts if c not in old_res]


for c in tqdm(result_files):
    c = c[c.rfind('/') + 1:]

    file = 'contract2/' + c

    results[c] = json.loads(open(file).read())
    if len(results[c]['vulnerabilities']['reentrancy']) != 0:
        result_final[c] = results[c]


with open('resultsWithoutFilters.json', 'w') as of:
    of.write(json.dumps(results, indent=1))

with open('result_finalWithoutFilters.json', 'w') as of:
    of.write(json.dumps(result_final, indent=1))
print(len(result_final))
print("Completed.")
