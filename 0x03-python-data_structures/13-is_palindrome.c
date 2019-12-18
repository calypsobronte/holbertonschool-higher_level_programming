#include "lists.h"
int is_palindrome(listint_t **head)
{
int len = 1, i, array[10];
listint_t *tem2 = *head, *tem1 = *head;
if (head == NULL || *head == NULL || (*head)->next == NULL)
{
return (1);
}
while (tem2 != NULL)
{
tem2 = tem2->next;
len++;
}
for (i = 0; i < len; i++)
{
array[i] = tem1->n;
tem1 = tem1->next;
len++;
}
for (i = 0; i < len; i++)
{
if (array[i] != array[len - 1 - i])
{
return (0);
}
}
return (1);
}
