#include "lists.h"

/**
 * check_cycle - a function that finds the loop in a linked list.
 * @list: pointer to the head of the list.
 *
 * Return: The address of the node where the loop starts,
 *		or NULL if there is no loop
*/

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			while (slow != fast)
			{
				slow = slow->next;
				fast = fast->next;
			}
			return (1);
		}
	}
	return (0);
}
