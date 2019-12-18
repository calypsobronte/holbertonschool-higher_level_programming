#include "lists.h"
int is_palindrome(listint_t **head)
{
int len = 0, i, j, array[10204];
if (head == NULL || *head == NULL || (*head)->next == NULL)
{
return (1);
}
while (*head)
{
array[len] = (*head)->n;
*head = (*head)->next;
len++;
}
j = len - 1;
for (i = 0; j < len / 2 + 1; i++, j--)
{
if (array[i] != array[j])
{
return (0);
}
}
return (1);
}
