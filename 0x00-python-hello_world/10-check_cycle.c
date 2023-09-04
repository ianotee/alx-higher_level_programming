#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - looks for a circle.
 * @list: Pointer to the linked list.
 * Return:0 if (success)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
