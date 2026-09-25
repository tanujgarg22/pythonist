PYTHON LIST AND DICTIONARY LABS
================================

This folder contains beginner Python exercises for practicing lists,
dictionaries, loops, conditions, tuples, and built-in functions.

The examples are written as separate files so that each exercise can be
run and studied independently.


LIST LABS
=========

Lab_List1.py - Sum list values
--------------------------------
Demonstrates how to calculate the sum of all numbers in a list using the
built-in sum() function. It also demonstrates how to sum only integer
values from a mixed list by using isinstance().

Lab_List2.py - Find the largest integer
---------------------------------------
Finds the largest integer in a list that contains both numbers and strings.
The example filters the list with isinstance() before using max().

Lab_List3.py - Remove duplicate values
--------------------------------------
Removes duplicate values from a list while preserving the original order.
It uses a separate list and checks whether each item has already been added.

Lab_List4.py - Check whether a list has duplicates
---------------------------------------------------
Checks whether a list contains duplicate values by comparing the length of
the original list with the length of a list containing unique values.
The function returns True when duplicates are found and False otherwise.

Lab_List5.py - Fast duplicate check
-----------------------------------
Checks for duplicate values and returns immediately when a duplicate is
found. This demonstrates an early-exit loop. The current example uses a
list for storing previously seen values.

Lab_List6.py - Reverse a list manually
--------------------------------------
Reverses a list by copying the original list and assigning each item to its
reverse index. It demonstrates enumerate(), list indexes, list.copy(), and
zero-based indexing.

Lab_List7.py - Count even and odd numbers
----------------------------------------
Counts the even and odd values in a list. The function returns both counts
as a tuple.

Lab_List8.py - Maximum consecutive difference
---------------------------------------------
Calculates the largest absolute difference between two consecutive numbers
in a list. The program compares each item with the next item and keeps the
largest difference found.

Lab_List9.py - Merge and sort two lists
---------------------------------------
Combines two lists and returns their values in sorted order. It demonstrates
list concatenation, sort(), and sorted().

Lab_List10.py - Circular list rotation
--------------------------------------
Rotates a list so that the selected key index becomes the first position.
The solution uses a reverse-based rotation technique and demonstrates
swapping list values by index.


DICTIONARY LAB
==============

dictionarylab.py - Create a dictionary from two lists
------------------------------------------------------
Demonstrates two ways to combine two lists into a dictionary.

1. The first function uses zip() to pair keys and values.
2. The second function uses enumerate() and a for loop to assign each
   value to its corresponding dictionary key.

Example result:
    {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}


HOW TO RUN A LAB
=================

Open a terminal in this Lab1 folder and run a file with:

    python Lab_List1.py

Replace Lab_List1.py with the file you want to run. For example:

    python Lab_List6.py
    python dictionarylab.py

If you are using a virtual environment, activate it first from the
Mission1 folder:

    .\.venv\Scripts\Activate.ps1

Then move to the Lab1 folder or run the files using their relative path.


TOPICS PRACTICED
=================

- Lists and list indexes
- List copying and concatenation
- Loops and enumerate()
- Conditional statements
- isinstance()
- sum(), max(), abs(), sort(), and sorted()
- zip() and dictionaries
- Tuples
- Duplicate detection
- List reversal and rotation
