#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

listint_t *reverse_linked_list(listint_t **head);
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

	i = (size - 1);
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

/**
 * reverse_linked_list - function to reverse linked list
 *
 * @head: pointer to pointer to linked list
 *
 * Return: pointer to linked list
 */

listint_t *reverse_linked_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = (*head);
	listint_t *next = NULL;

	while (current != NULL)
	{
		/** store next */
		next = current->next;

		/** reverse current node pointer */
		current->next = prev;

		/** move pointers one position ahead */
		prev = current;
		current = next;
	}

	(*head) = prev;

	return (*head);
}
