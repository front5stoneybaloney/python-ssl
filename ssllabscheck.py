

import ssllabsscanner
import sys
domain = sys.argv[1]

fullinfo = ssllabsscanner.newScan(domain)

#print(fullinfo)
#print(fullinfo['endpoints'][1]['statusMessage'])

certgrade = fullinfo['endpoints'][1]['grade']
print(f'Certificate grade: {certgrade}')

haswarn = fullinfo['endpoints'][1]['hasWarnings']
print(f'Hash warnings: {haswarn}')

commonnames = fullinfo['endpoints'][1]['details']['cert']['commonNames']
print(f'Common names: {commonnames}')

altNames = fullinfo['endpoints'][1]['details']['cert']['altNames']
print(f'Alternative names: {altNames}')

expirydate = fullinfo['endpoints'][1]['details']['cert']['notAfter']
print(f'Expiration date: {expirydate}')

sigalgorithm = fullinfo['endpoints'][1]['details']['cert']['sigAlg']
print(f'Signature algorithm: {sigalgorithm}')

certissues = fullinfo['endpoints'][1]['details']['cert']['issues']
print(f'Certificate issues: {certissues}')

certkeysize = fullinfo['endpoints'][1]['details']['key']['size']
print(f'Certificate keysize: {certkeysize}')

chain1keysize = fullinfo['endpoints'][1]['details']['chain']['certs'][1]['keySize']
print(f'Chain 1 keysize: {chain1keysize}')

chain1issues = fullinfo['endpoints'][1]['details']['chain']['certs'][1]['issues']
print(f'Chain 1 issues: {chain1issues}')

#chain2keysize = fullinfo['endpoints'][1]['details']['chain']['certs'][2]['keySize']
#print(f'Chain 2 keysize: {chain2keysize}')

chain2issues = fullinfo['endpoints'][1]['details']['chain']['issues']
print(f'Chain 2 issues: {chain2issues}')
