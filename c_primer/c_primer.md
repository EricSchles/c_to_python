#C Primer

Welcome to the C programming language.  In this tutorial we'll be going through the primitives of C.  

What we'll cover:

* Primitives
  * Printing to the Screen
  * Basic Math
  * Variables - storing state
  * for/while loops
  * functions
* Data Structures
  * Arrays
  * Structs
  * Pointers
    * Basic Pointers
    * Array Pointers
    * Function Pointers
  * Linked Lists
    * Singly Linked Lists
    * Doubly Linked Lists
    * Skip Lists
    * Stacks/Queues 
  * Trees
    * Binary Search Trees
    * Red/Black Trees, AVL Trees
  * Heaps
    * Priority Queues
  * Graphs
  * HashMaps
* Algorithms
  * Sorting
  * List Traversal
  * Graph Traversal
  * Shortest Path
  * Numerical Methods and computations

##Primitives

The C language has great primitives.  In fact after only understanding the basic data structures you are ready to make use of all of the power of the C language - blazing speed.

###Printing to the Screen
  
Printing to the screen is very powerful.  This is the most primitive form of debugging, and often the easiest.  Of course, other tools are better, but at the cost of ease.  

`hello.c`:

```
#include <stdio.h>

int main(){

    printf("Hello there\n");
    return 0;
}
```

To compile this program simply open a terminal, navigate to the directory you saved the file in, and then type:

`gcc hello.c -o hello`

This creates a binary (named hello) from the source file hello.c  To execute this file simply type the following:

`./hello`

This will execute the binary file.

###Basic Math

Basic math is easily expressible in C.  Here, we'll cover the basics.

####Addition:

`add.c`

```
#include <stdio.h>

int main(){
    
    int x = 5;
    int y = 6;
    printf("%d",x+y);
    
    return 0;
}

```

As you can see, adding two numbers is very easy.  We simply make use of the `+` operator.  The digit number 


  * Variables - storing state
  * for/while loops
  * functions


  
