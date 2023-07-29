#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>

/**
 * infinite_while - Infinite while loop zombie process
 * Return: exit 0 success
 */
int infinite_while(void)
{
	while (1)
		sleep(1);

	return (0);
}

/**
 * main - The entry point into the program
 * Return: Exit 0 success
 */
int main(void)
{
	pid_t child_pd;
	int process_num = 1;

	for (process_num = 1; process_num <= 5; process_num++)
	{
		child_pd = fork();
		if (child_pd > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pd);
			sleep(1);
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
