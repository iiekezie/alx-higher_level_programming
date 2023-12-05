/*
 * File: 13-is_palindrome.c
 * Auth: Ifeanyi I Ekezie
 */

#include "lists.h"
#include <stddef.h>

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a linked list.
 * @head: Pointer to pointer of first node of listint_t list.
 *
 * Return: Pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = NULL;
    int palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (palindrome);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        // Reverse the first half of the list
        listint_t *next = slow->next;
        slow->next = prev_slow;
        prev_slow = slow;
        slow = next;
    }

    // If the number of elements is odd, move slow one step forward
    if (fast != NULL)
        slow = slow->next;

    // Compare the reversed first half with the second half
    while (prev_slow != NULL && slow != NULL)
    {
        if (prev_slow->n != slow->n)
        {
            palindrome = 0;
            break;
        }
        prev_slow = prev_slow->next;
        slow = slow->next;
    }

    return (palindrome);
}
