/* Custom wrappers for Python/C interface to Quick DER.
 *
 * The Quick DER support in Python defines packages to represent ASN.1 specs,
 * classes to represent types and their DER unpackers, and instances to
 * represent parsed data.  Instances may be edited to accommodate future
 * packing or unpacking.
 *
 * The routines below make der_pack() and der_unpack() operations callable
 * from Python.  This is usually done from Python code generated by
 * asn2quickder to accommodate the ASN.1 input specifications.
 *
 * The resulting code does not present packer coding explicitly to the
 * end user, but wraps it inside appropriately named classes.  Under these
 * considerations, it may be expected that the resulting code is safe.
 *
 * It is also possible to manually define wrappers, but in that case a risk
 * of crashing the C backend arises when structures are not properly sized
 * or when their offsets are out of range.  We may be able to fix that in a
 * future version.
 *
 * The routines currently provide no parsing support, such as mappings for
 * INTEGER values.  We may be able to provide for such helps in a future
 * version.
 *
 * From: Rick van Rein <rick@openfortress.nl>
 */


#include <Python.h>

#include <quick-der/api.h>


/* _quickder.quickder_unpack (pck, bin, numcursori) -> cursori */
static PyObject *quickder_unpack (PyObject *self, PyObject *args) {
puts ("Welcome to der_unpack()");
	char *pck;
	int pcklen;
	char *bin;
	int binlen;
	int numcursori;
	//
	// Parse the arguments
	PyObject *retval = NULL;
puts ("Parsing args");
	if (!PyArg_ParseTuple (args, "s#s#i", &pck, &pcklen, &bin, &binlen, &numcursori)) {
		return NULL;
	}
puts ("Parsed fine");
	//
	// Allocate the dercursor array TODO:TEST
	dercursor cursori [numcursori];
	dercursor binput;
	binput.derptr = bin;
	binput.derlen = binlen;
	if (der_unpack (&binput, pck, cursori, 1)) {
		//TODO// Raise OSError()
		//TODO// refctr
		return NULL;
	}
puts ("Unpacked properly");
	//
	// Construct the structure of cursori to be returned
	retval = PyList_New (numcursori);
	if (retval == NULL) {
		//TODO// refctr
		return NULL;
	}
puts ("Created return list");
	while (numcursori-- > 0) {
		PyObject *elem;
		if (cursori [numcursori].derptr == NULL) {
			elem = Py_None;
		} else {
printf ("Creating string \"%.*s\" of size %d\n", cursori [numcursori].derlen, cursori [numcursori].derptr, cursori [numcursori].derlen);
			elem = PyString_FromStringAndSize (cursori [numcursori].derptr, cursori [numcursori].derlen);
			if (elem == NULL) {
				//TODO// refctr
				return NULL;
			}
		}
puts ("Setting return list item");
		if (PyList_SetItem (retval, numcursori, elem)) {
			//TODO// refctr
			return NULL;
		}
puts ("Set     return list item");
	}
	//
	// Cleanup and return
	//TODO// refctr
puts ("Returning");
	return retval;
}


/* _quickder.quickder_pack (pck, crsvals) -> bin */
static PyObject *quickder_pack (PyObject *self, PyObject *args) {
puts ("Welcome to quickder_pack");
	char *pck;
	int pcklen;
	PyObject *bins;
	Py_ssize_t binslen;
	//TODO:TEST// dercursor *cursori;
	PyObject *retval = NULL;
	//
	// Parse arguments, generally
puts ("Parse tuple");
	if (!PyArg_ParseTuple (args, "s#O", &pck, &pcklen, &bins)) {
		return NULL;
	}
puts ("Parsed fine");
	if (!PyList_Check (bins)) {
		//TODO// refctr
		return NULL;
	}
puts ("Got a list");
	binslen = PyList_Size (bins);
puts ("Got list size");
	//
	// Collect cursori, the dercursor array for der_pack()
	//TODO:TEST// cursori = malloc (sizeof (dercursor) * binslen);
	//TODO:TEST// if (cursori == NULL) {
		//TODO// refctr
		//TODO:TEST// return NULL;
	//TODO:TEST// }
	dercursor cursori [binslen];
	while (binslen-- > 0) {
		PyObject *elem = PyList_GetItem (bins, binslen);
		if (elem == Py_None) {
			memset (&cursori [binslen], 0, sizeof (*cursori));
puts ("Got a NULL cursor");
		} else if (PyString_Check (elem)) {
			char *buf;
			Py_ssize_t buflen;
			//TODO// Retval from following call?  Can it go wrong?
			PyString_AsStringAndSize (elem, &buf, &buflen);
			cursori [binslen].derptr = buf;
			cursori [binslen].derlen = buflen;
puts ("Got a cursor");
		} else {
			//TODO// refctr
			//TODO:TEST// free (cursori);
			return NULL;
		}
	}
	//
	// Determine the length of the packed string
	//TODO:TEST// uint8_t *packed = NULL;
	size_t packedlen = der_pack (pck, cursori, NULL);
printf ("Got packed data length %d\n", (int) packedlen);
	//TODO:TEST// packed = malloc (packedlen);
	//TODO:TEST// if (!packed) {
		//TODO:TEST// //TODO:TEST// free (cursori);
		//TODO:TEST// //TODO// refctr
		//TODO:TEST// return NULL;
	//TODO:TEST// }
	uint8_t packed [packedlen];
printf ("Allocated bytes at %p\n", packed);
	der_pack (pck, cursori, packed + packedlen);
puts ("Got packed data");
	retval = PyString_FromStringAndSize (packed, packedlen);
	//TODO:TEST// free (packed);
	//
	// Cleanup and return
	//TODO:TEST// free (cursori);
	//TODO// refctr
puts ("Returning a value");
	return retval;
}


static PyMethodDef der_methods [] = {
	{ "der_unpack", quickder_unpack, METH_VARARGS, "Unpack from DER encoding with Quick DER" },
	{ "der_pack",   quickder_pack,   METH_VARARGS, "Pack into DER encoding with Quick DER" },
	{ NULL, NULL, 0, NULL }
};


PyMODINIT_FUNC init_quickder () {
	PyObject *mod;
	mod = Py_InitModule ("_quickder", der_methods);
	if (mod == NULL) {
		return;
	}
}

