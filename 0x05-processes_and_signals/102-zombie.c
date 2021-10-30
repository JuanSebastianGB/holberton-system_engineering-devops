#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Main function to create 5 zombie processes
 * Return: Always 0 - Exit success
 *
 */

int main(void)
{
	int i = 5;
	pid_t pid;

	while (i--)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %i\n", pid);
			sleep(2);
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}

/**
 * infinite_while - execute an inifite while
 * Return: Always 0
 *
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
