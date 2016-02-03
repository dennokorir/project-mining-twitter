#encoding test
import sys

print(sys.stdout.encoding)
print(u"Stöcker".encode(sys.stdout.encoding, errors='replace'))
print(u"Стоескер".encode(sys.stdout.encoding, errors='replace'))
