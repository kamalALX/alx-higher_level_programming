#include "lists.h"

/**
*  insert_node- a function that adds a new node at the beginning of
*	listint_t list.
* @head: Pointer a pointer to the list.
* @number: an element of the linked list.
*
* Return: the address of the new element, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
