#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

const char* input = "409 194 207 470 178 454 235 333 511 103 474 293 525 372 408 428 \n4321 2786 6683 3921 265 262 6206 2207 5712 214 6750 2742 777 5297 3764 167 \n3536 2675 1298 1069 175 145 706 2614 4067 4377 146 134 1930 3850 213 4151 \n2169 1050 3705 2424 614 3253 222 3287 3340 2637 61 216 2894 247 3905 214 \n99 797 80 683 789 92 736 318 103 153 749 631 626 367 110 805 \n2922 1764 178 3420 3246 3456 73 2668 3518 1524 273 2237 228 1826 182 2312 \n2304 2058 286 2258 1607 2492 2479 164 171 663 62 144 1195 116 2172 1839 \n114 170 82 50 158 111 165 164 106 70 178 87 182 101 86 168 \n121 110 51 122 92 146 13 53 34 112 44 160 56 93 82 98 \n4682 642 397 5208 136 4766 180 1673 1263 4757 4680 141 4430 1098 188 1451 \n158 712 1382 170 550 913 191 163 459 1197 1488 1337 900 1182 1018 337 \n4232 236 3835 3847 3881 4180 4204 4030 220 1268 251 4739 246 3798 1885 3244 \n169 1928 3305 167 194 3080 2164 192 3073 1848 426 2270 3572 3456 217 3269 \n140 1005 2063 3048 3742 3361 117 93 2695 1529 120 3480 3061 150 3383 190 \n489 732 57 75 61 797 266 593 324 475 733 737 113 68 267 141 \n3858 202 1141 3458 2507 239 199 4400 3713 3980 4170 227 3968 1688 4352 4168 \n";


int char_count(const char *in, const char COI)
{
    int i, len, count;

    len = strlen(in);
    count = 0;

    for(i = 0; i < len; i++) {
        if (in[i] == COI) {
            count += 1;
        }
    }

    return count;
}


int puzzle1(void)
{
    int max, min, sum, len, num;
    char* local_input;
    char* orig_input;
    char* EON; // pointer to end of number
    char* EOL; // pointer to end of line

    sum = 0;
    min = INT_MAX;
    max = 0;
    len = strlen(input);
    local_input = (char*)malloc(len + 1);
    orig_input = local_input;
    memcpy(local_input, input, len); // We want a local copy of the input string that we can manipulate

    EOL = strchr(local_input, '\n');

    while (EOL != NULL) {
        EON = strchr(local_input, ' ');
        while(EON < EOL && EON != NULL) {
            *EON = '\0';
            num = atoi(local_input);

            if (num < min) min = num;
            if (num > max) max = num;

            local_input = EON + 1;
            EON = strchr(local_input, ' ');
        }
        sum += max - min;
        max = 0;
        min = INT_MAX;

        local_input = EOL + 1;
        EOL = strchr(local_input, '\n');
    }

    free(orig_input);
    return sum;
}


int puzzle2(void)
{
    int sum, len, num, rows, i, j, k;
    char* local_input;
    char* orig_input;
    char* EON; // Pointer to end of number
    char* EOL; // Pointer to end of line
    int** matrix;

    sum = 0;
    len = strlen(input);
    local_input = (char*)malloc(len + 1);
    orig_input = local_input;
    rows = 0;

    memcpy(local_input, input, len); // We want a local copy of the input string that we can manipulate
    EOL = strchr(local_input, '\n');
    matrix = (int**)malloc(sizeof(int*) * char_count(local_input, '\n'));

    while (EOL != NULL) {
        EON = strchr(local_input, ' ');

        *EOL = '\0'; // Terminate string at the end of the line
        matrix[rows] = (int*)malloc(sizeof(int) * (char_count(local_input, ' ') + 1));
        *EOL = '\n'; // Restore the string to its previous state
        i = 0;

        while(EON < EOL && EON != NULL) {
            *EON = '\0'; // Terminate string for atoi()
            num = atoi(local_input);
            matrix[rows][i] = num;
            i += 1;

            local_input = EON + 1;
            EON = strchr(local_input, ' ');
        }

        matrix[rows][i] = 0; // Each row will be appended with a 0
        rows++;
        local_input = EOL + 1;
        EOL = strchr(local_input, '\n');
    }
    free(orig_input);

    // At this point we have matrix populated with all the numbers from our input string

    for(i = 0; i < rows; i++) {
        for(j = 0; matrix[i][j]; j++) {
            for(k = j; matrix[i][k]; k++) {
                if (matrix[i][k] > matrix[i][j] && matrix[i][k] % matrix[i][j] == 0 ) {
                    sum += matrix[i][k] / matrix[i][j];
                    break;
                } else if (matrix[i][k] < matrix[i][j] && matrix[i][j] % matrix[i][k] == 0 ) {
                    sum += matrix[i][j] / matrix[i][k];
                    break;
                }
            }
        }
        free(matrix[i]);
    }

    free(matrix);
    return sum;
}


int main(void)
{
    printf("1: %i\n", puzzle1());
    printf("2: %i\n", puzzle2());
    return 0;
}
