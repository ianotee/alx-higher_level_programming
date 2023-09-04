#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - looks for a circle.
 * @list: Pointer to the linked list.
 * Return:0 if (success)
 */
int check_cycle(listint_t *list)
{
	listint_t *lower, *super;

	if (list == NULL || list->next == NULL)
		return (0);

	lower = list->next;
	super = list->next->next;

	while (lower && super && super->next)
	{
		if (lower == super)
			return (1);

		lower =lower->next;
		super = super->next->next;
	}

	return (0);
}
