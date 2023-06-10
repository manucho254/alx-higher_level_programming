#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - function to check if,
 * linked list is a palindrome.
 *
 * @head: linked list
 *
 * Return: 1 if palindrome, 0 if not palindrome
 */

int is_palindrome(listint_t **head)
{
	int size = 0, *arr, x, i;

	if (head == NULL)
		return (1);
	arr = malloc(sizeof(int));

	if (arr == NULL)
		return (0);

	while (*head)
	{
		arr = realloc(arr, (size + 1) * sizeof(int));
		arr[size] = (*head)->n;
		(*head) = (*head)->next;
		size++;
	}

	i = (size - 1);
	for (x = 0; x < size; x++)
	{
		if (arr[x] != arr[i])
			return (0);
		i--;
	}
	free(arr);

	return (1);
}
