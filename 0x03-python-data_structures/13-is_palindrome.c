#include "lists.h"
int is_palindrome(listint_t **head)
{
int len = 0, i;
if (head == NULL || *head == NULL || (*head)->next == NULL)
{
return (1);
}
while (head[len] != NULL)
{
len++;
}
for (i = 0; i < len; i++)
{
if ((*head[i]).n != (*head[len - 1 - i]).n)
{
return (1);
}
}
return (1);
}