# Algorithms and Data Structure in Python

[![Build Status](https://travis-ci.org/maurobaraldi/python-algorithms.svg?branch=master)](https://travis-ci.org/maurobaraldi/python-algorithms)
[![codecov](https://codecov.io/gh/maurobaraldi/python-algorithms/branch/master/graph/badge.svg)](https://codecov.io/gh/maurobaraldi/python-algorithms)
[![Requirements Status](https://requires.io/github/maurobaraldi/python-algorithms/requirements.svg?branch=master)](https://requires.io/github/maurobaraldi/python-algorithms/requirements/?branch=master)

This project was inspired by [JavaScript Algorithms and Data Structures](https://github.com/trekhleb/javascript-algorithms/) Thanks Oleksii Trekhleb for the initiative.

This repository contains implementations of the most common algorithms and data structures for computer science. Some of them may have mulitple possible soluitons.

## Motivation

I started this repository for study and improve my programming skills. 

Besides, I often get to know people who have have a lot of questions related to algorithms and data structures. But actualy people post answers they are used to work with. Sometimes, people have even more questions after reading the solution, than before.

I hope this repoistory may help people understand in an easy way some of the fundamental concepts of programming computer.

## Organization

This repository is divided mainly by [Algorithms](https://github.com/maurobaraldi/python-algorithms/tree/master/algorithms/README.md) and [Data Structures](https://github.com/maurobaraldi/python-algorithms/tree/master/data_structures/README.md). Every implementation has its [test cases](https://github.com/maurobaraldi/python-algorithms/tree/master/tests).

## Prepare and Tests

All the code were made using only Python standard lib, and most of the implementations uses only builtin modules.

The only external lib used is [pytest](https://docs.pytest.org/en/latest/), but I do not use pytest resources for testing just to keep things clear and easy to understand. "Simple is better than complex." - The Zen of Python

To install pytest run

`pip3 install pytest`

or install from requirements

`pip3 install -r requirements.txt`

If you are using Linux Powershell or OSX, you can run:

`make install`

#### Running Tests

If you're using pytest, and I sugest you to use it, you can run all test suite running:

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
