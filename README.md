# LeetCode-20.-Valid-Parentheses

We add every opening paranthesis to a heap. Then when we cross a closing parantesis we check if the last element in heap is the corresponding opening paranthesis.
If true, we pop the last element in heap.
If the first closing tag is encountered as the first element in the string we return False, as it is impossible to be a valid paranthesis.
Finallly if the is any elements left in the heap, we conclude as the string is not a valid paranthesis string and return False.