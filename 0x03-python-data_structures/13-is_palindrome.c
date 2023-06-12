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
	listint_t *tmp, *rev;
	int x, size, mid;

	if (head == NULL)
		return (1);


	tmp = (*head);
	if (tmp == NULL)
		return (1);

	/** reverse linked list */
	rev = reverse_linked_list(head);
	if (rev == NULL)
		return (1);

	size = 0;
	while (*head)
	{
		size += 1;
		(*head) = (*head)->next;
	}

	mid = size / 2;
	while (tmp != NULL && rev != NULL && x >= mid)
	{
		x++;
		/**
		 * check if values in reverse are the,
		 * same with values in original list
		 */
		if (tmp->n != rev->n)
			return (0);

		tmp = tmp->next;
		rev = rev->next;
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
