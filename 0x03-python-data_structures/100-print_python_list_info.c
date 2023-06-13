#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - function that,
 * prints basic info about python lists
 *
 * @p: This is a type which contains the,
 * information Python needs to treat a pointer,
 * to an object as an object
 *
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t len;
	PyObject *tmp;
	PyTypeObject *type;
	PyListObject *list;
	int x;

	len = PyList_GET_SIZE(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (x = 0; x < len; x++)
	{
		tmp = PyList_GetItem(p, x);
		type = Py_TYPE(tmp);
		printf("Element %d: %s\n", x, type->tp_name);
	}
}
