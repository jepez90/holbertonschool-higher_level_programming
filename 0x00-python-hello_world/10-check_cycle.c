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
	const listint_t *current, *test;
	unsigned int n, m; /* number of nodes */

	current = list;
	for (n = 0; current != NULL; n++)
	{
		if (current == current->next)
			return (1);

		test = list;
		for (m = 0; m < n; m++)
		{
			if (current == test)
				return (1);

			test = test->next;
		}

		current = current->next;
	}

	return (0);
}
