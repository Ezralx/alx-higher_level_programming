#include <stdio.h>
#include <string.h>


/**
 * print_python_string - prints a python string in C
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t p_len;
	char *str;

	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
	{
		p_len = PyUnicode_GET_LENGTH(p);
		str = PyBytes_AsString(PyUnicode_AsUTF8String(p));
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		printf("  length: %zd\n  value: %s\n", p_len, str);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
	fflush(stdout);
}
