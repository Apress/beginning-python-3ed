%module palindrome

%{
#include <string.h>
%}

extern int is_palindrome(char *text);