#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
		return (NULL);
	}
	else
	{
		newnode->n = number;
		newnode->next = *head;
		*head = newnode;
	}
	return (newnode);
}
