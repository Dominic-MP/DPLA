import requests, json, argparse


parser = argparse.ArgumentParser()
parser.add_argument('--naid', dest='naid', metavar='NAID',
                    action='store')       

args = parser.parse_args()

naid = args.naid

if args.naid is None :
	naid = raw_input('----\n Enter exactly one NAID: ')
r = json.loads(requests.get('http://api.dp.la/items/?api_key=10b516949e8a7bdc64f25903ee1aefd3&sourceResource.identifier=' + naid).text)

print '\n DPLA item: ' + r['docs'][0]['id'] + '\n----'