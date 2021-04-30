#include "lists.h"

/**
 * insert_node - adds a new node at the ordered listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node, *new_node;

	/* create the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	/* insert the new node */
	current_node = *head;
	if (current_node == NULL)
	{/* if no exists nodes */
		*head = new_node;
	}
	else if (current_node->n >= number)
	{/* if the ne node < the first node */
		new_node->next = current_node;
		*head = new_node;
	}
	else
	{/* in other case */
		current_node = *head;
		while (current_node->next != NULL)
		{
			if (current_node->next->n >= number)
				break;
			current_node = current_node->next;
		}
		new_node->next = current_node->next;
		current_node->next = new_node;
	}
	return (new_node);
}

