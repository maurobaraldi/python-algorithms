# Algorithms and Data Structure in Python

This project was inspired by [JavaScript Algorithms and Data Structures](https://github.com/trekhleb/javascript-algorithms/) Thanks Oleksii Trekhleb for the initiative.

This repository contains implementations of the most common algorithms and data structures for computer science. Some of then has more than one way to do it.

## Motivation

I started this repository for study and improve my programming skills. 

Also, often I see people starting study programming computer, having a lot of questions related to algorithms and data structures, but most of the answers is biased in experience of who is answering. Sometimes, people have more questions after ask, than has before ask.

I hope this repoistory may help people understand easy way some of fundamental concepts of programming computer.

## Organization

This repository is divided mainly by [Algorithms](https://github.com/maurobaraldi/python-algorithms/tree/master/algorithms/README.md) and [Data Structures](https://github.com/maurobaraldi/python-algorithms/tree/master/data_structures/README.md). Every implementation has it's [test cases](https://github.com/maurobaraldi/python-algorithms/tree/master/tests).

## Prepare and Tests

All code where made using only Python standard lib, and most of the implementations uses only builtin modules.

The only external lib used is [pytest](https://docs.pytest.org/en/latest/), but I do not uses pytest resources for testing just to keep things clear and easy to understand. "Simple is better than complex." - The Zen of Python

To install pytest run

`pip3 install pytest`

or install from requirements

`pip3 install -r requirements.txt`

If you are using Linux Powershell or OSX, you can run:

`make install`

#### Running Tests

If you're uisng pytest, and I sugest you to use it, you can run all test suite running:

`make test`

To run only algorithms or data structure category run:

`make test categ="algorithms"`

or

`make test categ="data_structure"`

To run some especific algorithm for example run

`make test categ="algorithms" sub="math"`

### Implementations

Here is a list of algorithms and data structures implemented.

```
├── algorithms
│   ├── data_structures
│   │   └── linked_lists
│   ├── math
│   │   ├── fatorial
│   │   ├── fibonacci
│   │   ├── gcd
│   │   ├── lcm
│   │   └── primes
│   ├── sets
│   │   ├── cartesian_product
│   │   ├── combinations
│   │   ├── longest_common_subsequence
│   │   └── shuffle
│   └── sorting
│       └── bubble_sort
└── data_structures
    ├── linked_lists
    ├── queue
    ├── stack
    └── tree
```
