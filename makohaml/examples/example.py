from makohaml import makohaml

f = open("example.hamlpy")
haml = f.read()
f.close()
print haml
parser = makohaml.Compiler()
result = parser.process(haml)
print "="*30
print result
