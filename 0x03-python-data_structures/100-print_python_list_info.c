#include "/usr/include/python3.4.3/Python.h"
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
	int x;

	len = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", len);

	for (x = 0; x < size; x++)
	{
		tmp = PyList_GetItem(p, x);
		type = Py_TYPE(tmp);
		printf("Element %d: %s\n", x, type->tp_name);
	}
}
