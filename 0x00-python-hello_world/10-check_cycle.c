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

	if (list == NULL || list->link == NULL)
		return (0);

	lower = list->link;
	super = list->link->link;

	while (lower && super && super->link)
	{
		if (lower == super)
			return (1);

		lower =lower->link;
		super = super->link->link;
	}

	return (0);
}
