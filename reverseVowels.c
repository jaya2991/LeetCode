/*Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".*/
void swap(char *a, char *b){
    char temp;
    
    temp = *a;
    *a = *b;
    *b = temp;
}

int isVowel(char a){
    if(a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u' || a == 'A' || a == 'E' || a == 'I' || a == 'O' || a == 'U'){
        return 1;
    }
    return 0;
}

char* reverseVowels(char* s) {
    int i = 0;
    int j = strlen(s) - 1;
    
    while(i <= j){
        if(!isVowel(s[i])){
            i++;
        }
        else if(!isVowel(s[j])){
            j--;
        }
        else{
            swap(&s[i], &s[j]); 
            i++;
            j--;
        }
        
    }
    return s;
}
