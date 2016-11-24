/* Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
*/
void swap(char *a, char *b){
    char temp;
    
    temp = *a;
    *a = *b;
    *b = temp;
}
char* reverseString(char* s) {
    
    int i = 0;
    int j = strlen(s) - 1;
    
    while(i <= j){
        swap(&s[i], &s[j]);
        i++;
        j--;
    }
    return s;
    
}
