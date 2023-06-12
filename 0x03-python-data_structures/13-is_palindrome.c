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
	int size = 0, x = 0, i;
	listint_t *tmp;

	if (head == NULL)
		return (1);

	tmp = (*head);
	if (tmp == NULL)
		return (1);

	while (*head)
	{
		size++;
		(*head) = (*head)->next;
	}

	int arr[size];

	while (tmp)
	{
		arr[x] = tmp->n;
		tmp = tmp->next;
		x++;
	}

	i = (size);
	for (x = 0; x < size; x++)
	{
		if (arr[x] != arr[i])
		{
			return (0);
		}
		i--;
	}

	return (1);
}
