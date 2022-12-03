#include <stdio.h>
#include <stdlib.h>

#define MAX_LEN 10

int main(void)
{
    FILE *f1;
    
    int calories = 0, max_cal[3] = {0, 0, 0}, total = 0;

    

    for (int i = 0; i < 3; i += 1)
    {
        char txt1[MAX_LEN];
        f1 = fopen("input.txt", "r");
        while (fgets(txt1, MAX_LEN, f1))
        {

            if (txt1[0] == '\n')
            {

                if (i == 2)
                {
                    if (calories != max_cal[1] )
                    {
                        if (calories > max_cal[i])
                        {
                            max_cal[i] = calories;
                        }
                    }
                }
                else if (i == 1)
                {

                    if (calories != max_cal[0])
                    {
                        if (calories > max_cal[i])
                        {
                            max_cal[i] = calories;
                            
                        }
                        
                    }
                    
                }
                else
                {
                    if (calories > max_cal[i])
                    {
                        max_cal[i] = calories;
                    }
                }

                calories = 0;
            }
            else
            {
                calories += atoi(txt1);
            }

            
        }

        
        fclose(f1);
        
    }

    for (int k = 0; k < 3; k++)
    {
        total += max_cal[k];
        printf("Max calories: %d\n", max_cal[k]);
    }

        printf("Total calories: %d\n", total);
    

    return 0;
}

// int file_read(FILE *file, int a, int count);

// int main(void)
// {
//     FILE *f1;

//     int elf = 0;
//     int calories = 0, max_cal = 0;

//     f1 = fopen("input.txt", "r");

//     printf("No of elves %d", elf);

//     fclose(f1);

//     return 0;
// }

// int file_read(FILE *file, int a, int count)
// {
//     char txt1[MAX_LEN];
//     int elf = 0;
//     while (fgets(txt1, MAX_LEN, file))
//     {

//         if (a == 0)
//         {
//             if (txt1[0] == '\n')
//             {
//                 elf += 1;
//             }
//         } else if (a == 1) {
//         }
//     }
// }
