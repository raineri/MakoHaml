from hamlpy import hamlpy

f = open("example.hamlpy")
haml = f.read()
f.close()
print haml
parser = hamlpy.Compiler()
result = parser.process(haml)
print "="*30
print result
