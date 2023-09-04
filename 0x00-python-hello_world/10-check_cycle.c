#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - looks for a circle.
 * @list: Pointer to the linked list.
 * Return:0 if (success)
 */
int check_cycle(listint_t *list)
{
	listint_t *lower, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	lower = list->next;
	fast = list->next->next;

	while (lower && fast && fast->next)
	{
		if (lower == fast)
			return (1);

		lower = lower->next;
		fast = fast->next->next;
	}

	return (0);
}
