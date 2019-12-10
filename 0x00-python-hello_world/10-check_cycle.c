#include "lists.h"
/**
 * check_cycle - function check list
 * @list: list
 * Return: 0
 */
int check_cycle(listint_t *list)
{
listint_t *temp1, *temp2;

temp1 = list;
temp2 = list->next;

if (list == NULL || list->next == NULL)
return (0);
while (temp1 != NULL && temp2->next != NULL && temp2 != NULL)
{
if (temp1 == temp2)
{
return (1);
}
temp1 = temp1->next;
if (temp2->next->next != NULL)
temp2 = temp2->next->next;
else
break;
}
return (0);
}
