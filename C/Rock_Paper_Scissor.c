#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
char* var_for_return;
int playerpoint, opponentpoint;
char* playerwin()
{
    return "\nYou Win\n+1 Points To You\n";
    playerpoint++;
}
char* playerlose()
{
    return "\nYou Lose\n+1 Points To Your Opponent\n";
    opponentpoint++;
}
char* tie()
{
    return "\nTie\nNo Points To Anyone\n";
}
int generaterandom()
{
    srand(time(NULL));
    return rand()%3;
}
void gamelayout()
{
    int playerchoice, opponent_choice;
    
        printf("\nEnter Your Choice : \n");
        printf("1 For Rock\n");
        printf("2 For Paper\n");
        printf("3 For Scissor\n");
        scanf("%d", &playerchoice);
        opponent_choice = generaterandom();
        if (playerchoice == 1)
        {
            if (opponent_choice == 1)
            {
                printf("Opponent\'s Choice : Rock\n");
                var_for_return = tie();
                printf("%s", var_for_return);
            }
            else if (opponent_choice == 2)
            {
                printf("Opponent\'s Choice : Paper\n");
                var_for_return = playerlose();
                printf("%s", var_for_return);
            }
            else
                {
                    printf("Opponent\'s Choice : Scisssor\n");
                    var_for_return = playerwin();
                    printf("%s", var_for_return);
                }
        }
        else if (playerchoice == 2)
        {
            if (opponent_choice == 1)
            {
                printf("Opponent\'s Choice : Rock\n");
                var_for_return = playerwin();
                printf("%s", var_for_return);
            }
            else if (opponent_choice == 2)
            {
                printf("Opponent\'s Choice : Paper\n");
                var_for_return = tie();
                printf("%s", var_for_return);
            }
            else
                {
                    printf("Opponent\'s Choice : Scisssor\n");
                    var_for_return = playerlose();
                    printf("%s", var_for_return);
                }
        }
        else if (playerchoice == 3)
        {
            if (opponent_choice == 1)
            {
                printf("Opponent\'s Choice : Rock\n");
                var_for_return = playerlose();
                printf("%s", var_for_return);
            }
            else if (opponent_choice == 2)
            {
                printf("Opponent\'s Choice : Paper\n");
                var_for_return = playerwin();
                printf("%s", var_for_return);
            }
            else
                {
                    printf("Opponent\'s Choice : Scisssor\n");
                    var_for_return = tie();
                    printf("%s", var_for_return);
                }
        }
        else
        {
            printf("\nEnter A Valid Option.\n\n");
            gamelayout();
        }
}
int main()
{
    int number_of_rounds;
    char yourname;
    printf("Enter Your Name : ");
    scanf("%s", &yourname);
    printf("\nWelcome To Rock, Paper, Scissor Game\n");
    printf("Enter The Number Of Rounds You Want To Play : \n");
    scanf("%d", &number_of_rounds);
    for (int i = 0; i < number_of_rounds; i++)
    {
        gamelayout();
    }
}