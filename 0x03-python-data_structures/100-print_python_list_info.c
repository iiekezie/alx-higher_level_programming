#include <Python.h>

void print_python_list_info(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t size, allocated, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "Object is not a list\n");
        return;
    }

    list = (PyListObject *)p;

    size = PyList_GET_SIZE(list);
    allocated = list->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GET_ITEM(list, i);

        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
