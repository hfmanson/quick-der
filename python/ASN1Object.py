#DONE# share the bindata and ofslen structures with sub-objects
#TODO# add the packer data to the ASN1Object
#TODO# add a der_pack() method
#TODO# generate rfc1234.TypeName classes (or modules, or der_unpack functions)
#TODO# deliver ASN1Object from the der_unpack() called on rfc1234.TypeName


# The ASN1Object is a nested structure of class, accommodating nested fields.
# Nesting instances share the bindata and ofslen structures, which they modify
# to retain sharing.  The reason for this is that a future der_pack() on the
# class must use changes made in the nested objects as well as the main one.

class ASN1Object (object):

	def __init__ (self, der_packer='\x00', structure={}, ofslen=[], bindata=['']):
		ASN1Object.der_packer = der_packer
		ASN1Object.structure = structure
		ASN1Object.ofslen = ofslen
		ASN1Object.bindata = bindata
		for (k,v) in structure.items ():
			if type (k) != type (""):
				raise Exception ("ASN.1 structure keys can only be strings")
			if type (v) == type (13):
				ASN1Object.structure [k] = v
			elif type (v) == type ({}):
				ASN1Object.structure [k] = ASN1Object (
							bindata,
							structure [k],
							ofslen )
			else:
				raise Exception ("ASN.1 structure values can only be int or dict")

	def __setattr__ (self, name, val):
		if not ASN1Object.structure.has_key (name):
			raise AttributeError (name)
		val = str (val)
		siz = len (val)
		ofs = sum (map (len, ASN1Object.bindata))
		ASN1Object.ofslen [ASN1Object.structure [name]] = (ofs,siz)
		ASN1Object.bindata.append (val)

	def __getattr__ (self, name):
		if not ASN1Object.structure.has_key (name):
			raise AttributeError (name)
		idx = ASN1Object.structure [name]
		(ofs,siz) = ASN1Object.ofslen [ASN1Object.structure [name]]
		elm = 0
		while ofs >= len (ASN1Object.bindata [elm]):
			ofs = ofs - len (ASN1Object.bindata [elm])
			elm = elm + 1
		return ASN1Object.bindata [elm] [ofs:ofs+siz]


# class LDAPMessage (ASN1Object):
if True:

	der_packer = '\x00'
	structure = { 'hello': 0, 'world': 1 }
	ofslen = [ (0,5), (6,5) ]
	bindata = ['Hello World']

	# def unpack (self):
	# 	return ASN1Object (bindata=self.bindata, ofslen=self.ofslen, structure=self.structure)

	def unpack ():
		return ASN1Object (der_packer=der_packer, bindata=bindata, ofslen=ofslen, structure=structure)


# 
# class LDAPMessage2 (ASN1Object):
# 
# 	bindata = 'Hello World'
# 	ofslen = [ (0,5), (6,5) ]
# 	structure = { 'hello': 0, 'world': 1 }
# 
# 	def __init__ (self):
# 		super (LDAPMessage2,self).__init__ (
# 			bindata='Hello World',
# 			ofslen=[ (0,5), (6,5) ],
# 			structure={ 'hello':0, 'world':1 })
# 
# 
# # a1 = ASN1Wrapper (bindata, ofslen, structure)
# # a1 = ASN1Object (bindata, ofslen, structure)
# # a1 = LDAPMessage ()
# a1 = LDAPMessage2 ()

a1=unpack()

print 'Created a1'

print a1.hello, a1.world

a1.world = 'Wereld'
a1.hello = 'Motjo'

print a1.hello, a1.world

