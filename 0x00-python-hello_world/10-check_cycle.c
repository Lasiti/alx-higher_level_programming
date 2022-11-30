#include "lists.h"

/**
 * check_cycle - Checks if a  singly linked list has a cycle in it
 * @list: The single linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *hare = list, *tortoise = list;

if (list != NULL)
{
while (hare && hare->next)
{
hare = hare->next->next;
tortoise = tortoise->next;
if (tortoise == hare)
{
tortoise = list;
while (tortoise != hare)
{
tortoise = tortoise->next;
hare = hare->next;
}
return (1);
}
}
}
return (0);
}
