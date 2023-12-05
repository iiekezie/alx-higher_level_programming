#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current;
    int *stack;
    int top, i;

    if (head == NULL || *head == NULL)
        return (1);

    current = *head;
    stack = malloc(sizeof(int));
    if (stack == NULL)
        return (0);

    top = 0;
    while (current != NULL)
    {
        top++;
        stack = realloc(stack, sizeof(int) * top);
        if (stack == NULL)
            return (0);
        stack[top - 1] = current->n;
        current = current->next;
    }

    current = *head;
    i = top - 1;
    while (i >= top / 2)
    {
        if (stack[i] != current->n)
        {
            free(stack);
            return (0);
        }
        current = current->next;
        i--;
    }

    free(stack);
    return (1);
}

