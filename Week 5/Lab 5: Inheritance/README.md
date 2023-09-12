# Lab 5: Inheritance

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 5 - Lab 5: Inheritance](https://cs50.harvard.edu/x/2023/labs/5/). This program simulates the genetic inheritance of blood types for each member of a family. Blood types are determined by the combination of alleles inherited from parents. The program creates a family tree of individuals and their corresponding blood types based on genetic inheritance.

## Requirements

- A computer with a compatible C compiler.
- Basic understanding of genetic inheritance.

## How to Use

1. Compile the program: Open a terminal and navigate to the directory containing the "inheritance.c" file. Compile the program using the following command:

   ```
   gcc -o inheritance inheritance.c
   ```

2. Run the program: Execute the compiled program using the following command:

   ```
   ./inheritance
   ```

3. Output: The program will create a family tree of individuals, starting from a child in Generation 0. It will display each family member's blood type based on their genetic inheritance.

## Program Explanation

The program defines a `person` struct that represents an individual in the family. Each person has pointers to two parents and two alleles representing their blood type. The program uses recursion to build the family tree, assign alleles, and print the family's blood types.

- `create_family`: This function creates a family tree of a specified number of generations. It allocates memory for each person and assigns their alleles based on their parents' alleles. The function returns a pointer to the youngest generation's person.

- `free_family`: This function frees the memory allocated for the family tree. It uses recursion to traverse the tree and free memory for each person and their ancestors.

- `print_family`: This function prints the family tree and blood types for each person. It uses recursion to print each generation with appropriate indentation.

- `random_allele`: This function randomly selects an allele ('A', 'B', or 'O') for genetic inheritance.

## Testing

Upon running `./inheritance`, the program will display the family tree with blood types for each individual based on genetic inheritance. The output should adhere to the genetic inheritance rules described in the background section.

For example:

```
Child (Generation 0): blood type OO
    Parent (Generation 1): blood type AO
        Grandparent (Generation 2): blood type OA
        Grandparent (Generation 2): blood type BO
    Parent (Generation 1): blood type OB
        Grandparent (Generation 2): blood type AO
        Grandparent (Generation 2): blood type BO
```

## Conclusion

The "inheritance" program provides a visual representation of genetic blood type inheritance for a family tree. It demonstrates how genetic alleles are passed down from parents to children, resulting in different blood types for each family member. This simulation illustrates genetic concepts in an easily understandable manner.

Feel free to experiment with different values for the number of generations and observe how blood types are inherited throughout the family tree.