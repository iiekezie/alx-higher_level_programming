#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints information about Python lists
 * @p: Pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;

	printf("[*] Python list info\n");

	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++)
		{
			printf("Element %ld: ", i);
			print_python_bytes(PyList_GetItem(p, i));
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Prints information about Python bytes
 * @p: Pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *str;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
		printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
		str = ((PyBytesObject *)p)->ob_sval;
		for (i = 0; i < size + 1 && i < 10; i++)
			printf("%02x ", str[i] & 0xFF);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - Prints information about Python float objects
 * @p: Pointer to PyObject
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");

	if (PyFloat_Check(p))
	{
		printf("  value: %lf\n", ((PyFloatObject *)p)->ob_fval);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
}
