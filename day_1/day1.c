#include <stdio.h>
#include <stdlib.h>

#define MAX_LEN 10

int main(void) {
    FILE *f1;
    char txt1[MAX_LEN];
    int elf = 0;
    int calories = 0, max_cal = 0;

    f1 = fopen("input.txt", "r");
    while(fgets(txt1, MAX_LEN, f1)) {
        
        if (txt1[0] == '\n') {
            elf += 1;

            if (calories > max_cal) {
                max_cal = calories;
            }

            calories = 0;
            
        } else {
            calories += atoi(txt1);
        }
        
    }

    printf("Max calories: %d", max_cal);
    

    fclose(f1);

    return 0;
}