#include "lists.h"

/***/

listint_t *reverse(listint_t **head)
{
    listint_t *current = *head;
    listint_t *next = NULL:
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


