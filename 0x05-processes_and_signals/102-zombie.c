#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - This function loops infinitely with a second delay
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - This program creates 5 zombie processes and displays its PID
 * Return: Exit Status
 */
int main(void)
{
	int i = 0;
	pid_t child_pid = 0;

	for (i = 0 ; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", child_pid);
	}
	infinite_while();

	return (0);
}
