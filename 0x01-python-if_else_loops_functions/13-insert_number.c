#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - function to add new node to a sorted list
 *
 * @head: struct listint_t
 * @number: value for new node
 *
 * Return: address to new node else return null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp, *next_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	tmp = malloc(sizeof(listint_t));
	if (new_node == NULL || tmp == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	while (*head)
	{
		if ((*head)->n < new_node->n && (*head)->next == NULL)
			break;
		if ((*head)->n < new_node->n && (*head)->next->n >= new_node->n)
			break;
		add_nodeint_end(&tmp, (*head)->n);
		(*head) = (*head)->next;
	}
	while (*head)
	{
		if ((*head)->n < new_node->n && (*head)->next == NULL)
		{
			(*head)->next = new_node;
			return (*head);
		}
		if ((*head)->n < new_node->n && (*head)->next->n >= new_node->n)
		{
			next_node = (*head)->next;
			new_node->next = next_node;
			(*head)->next = new_node;
			tmp->next = (*head);
			return (tmp);
		}
		(*head) = (*head)->next;
	}

	return (*head);
}
