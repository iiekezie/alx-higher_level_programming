#include <stdlib.h>
#include "lists.h"

/*
 * File: 13-insert_number.c
 * Auth: Ifeanyi I Ekezie
 */

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to the head of the list
 * @number: the number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *new;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    new = *head;
    while (new->next != NULL && new->next->n < number)
    {
        new = new->next;
    }

    new_node->next = new->next;
    new->next = new_node;

    return (new_node);
}
