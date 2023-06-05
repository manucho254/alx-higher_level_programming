#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - function to check if there is a cycle in linked list
 *
 * @list: pointer to linked list
 *
 * Return: 1 if there is a cycle else return 0
 */

int check_cycle(listint_t *list)
{
	int *vals, i, x, count = 0;

	if (list == NULL)
		return (0);

	vals = malloc(1 * sizeof(int));
	vals[0] = 0;
	while (list)
	{
		vals = realloc(vals, (i + 1) * sizeof(int));
		vals[i] = list->n;
		for (x = 0; x < i; x++)
		{
			if (vals[x] == vals[i])
			{
				count += 1;
			}
			if (count == 2)
			{
				free(vals);
				return (1);
			}
		}
		count = 0;
		i++;
		list = list->next;
	}

	free(vals);
	return (0);
}
