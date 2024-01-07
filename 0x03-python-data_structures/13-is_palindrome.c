#include "lists.h"

/**
 * reverse - Function to reverse a linked list
 * @head: pointer to he list to reverse
 *
 * Return: reversed list
*/

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

/**
 * is_palindrome - Function to check if a linked list is a palindrome
 *
 * @head: pointer to the head of the list
 *
 * Return: Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *midnode = NULL;

	if (*head == NULL)
		return (1);
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
			return (0);
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
	return (1);
}

