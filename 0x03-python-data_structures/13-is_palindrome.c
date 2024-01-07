#include "lists.h"

/***/

listint_t *reverse(listint_t *head)
{
	listint_t *current = head;
	listint_t *next;
	listint_t *previous = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	return (previous);

}

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *midnode = NULL;
	int res = 1;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		midnode = slow;
		slow = slow->next;
	}
	slow = reverse(slow);
	fast = *head;

	while (slow != NULL)
	{
		if (fast->n != slow->n)
		{
			res = 0;
			break;
		}

		fast = fast->next;
		slow = slow->next;
	}

	slow = reverse(slow);

	if (midnode != NULL)
	{
		prev_slow->next = midnode;
		midnode->next = slow;
	}
	else
		prev_slow->next = slow;

	return res;
}

