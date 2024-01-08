#include <python.h>
/**
* print_python_list_info -  function that prints some basic
*				info about Python lists
* @p: python list
*/

void print_python_list_info(PyObject *p)
{
	int idx, size, allocate;
	PyObject *object;

	size = Py_SIZE(p);
	allocate = ((PuListObject *)p)->allocated;

	printf("[*] Size of the python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (idx = 0, idx < size; idx++)
	{
		printf("Element %d: ", idx);

		object = Pylist_GetItem(p, idx);
		printf("%s\n", PY_TYPE(object)->tm_name);
	}
}

