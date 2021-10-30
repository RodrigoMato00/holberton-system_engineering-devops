#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 *infinite_while - infinite while loop
 *Return: 0
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
 *main - zombie process
 *Return: 0
 */
int main(void)
{
	pid_t zombie;
	char iterador = 0;

	while (iterador < 5)
	{

		zombie = fork();

		if (zombie > 0)
		{

			printf("Zombie process created, PID: %d\n", zombie);
			sleep(1);
			iterador++;

		}

		else

			exit(0);

	}

	infinite_while();
	return (EXIT_SUCCESS);
}
