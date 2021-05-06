#include "lists.h"

/**
 * is_palindrome - check if an listint_t list is a palindromo.
 * @head: pointer to the head of the linked list.
 *
 * Return: 1 if the list is a palindromo, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i = 0, j = 0, numbers[1024] = {0};

	if (!head || !(*head))
		return (1);

	current = *head;
	/* travel the list to found its length */
	while (current)
	{
		numbers[i++] = current->n;
		current = current->next;
	}

	i--;

	while (j < i)
		if (numbers[j++] != numbers[i--])
			return (0);

	return (1);
}
