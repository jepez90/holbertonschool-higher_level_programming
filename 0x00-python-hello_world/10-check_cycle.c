#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: 1 if the list countain a cycle or 0 otherwise
 */
int check_cycle(listint_t *list)
{
	const listint_t *tortoise, *hare;

	if (list == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	while (hare)
	{
		if (hare == tortoise)
			return (1);

		if (hare->next)
			hare = hare->next->next;
		else
			break;

		tortoise = tortoise->next;
	}

	return (0);
}
