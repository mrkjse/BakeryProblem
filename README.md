

## Bakery Problem

### Background:  

A bakery used to base the price of their produce on an individual item cost. So if a customer ordered 10 cross buns then they would be charged 10x the cost of single bun. The bakery has decided to start  selling their produce prepackaged in bunches and charging the customer on a per pack basis. So if the  shop sold vegemite scroll in packs of 3 and 5 and a customer ordered 8 they would get a pack of 3 and  a pack of 5. The bakery currently sells the following products:  

Name | Code | Packs 
-----|------|------
Vegemite Scroll | VS5 | 3 @ $6.99, 5 @ $8.99
Blueberry Muffin | MB11 | 2 @ $9.95, 5 @ $16.95, 8 @ $24.95
Croissant | CF | 3 @ $5.95, 5 @ $9.95, 9 @ $16.99 

### Task:  

Given a customer order you are required to determine the cost and pack breakdown for each product.  To save on shipping space each order should contain the minimal number of packs.  

### Input:  

Each order has a series of lines with each line containing the number of items followed by the product  code. An example input:

```
10 VS5  
14 MB11
13 CF    
```

### Output:  

A successfully passing test(s) that demonstrates the following output:


```
10 VS5 $17.98
 2 x 5 $8.99
14 MB11 $54.8
  1 x 8 $24.95
  3 x 2 $9.95  
13 CF $25.85
  2 x 5 $9.95
  1 x 3 $5.95
```


### Advice:

 - Choose whatever language you’re comfortable with
 - The input/output format is not important, do whatever feels reasonable
 - Make sure you include at least one test
 - We expect the see code which you would be happy to put in production
  If something is not clear don’t hesitate to ask or just make an assumption and go with it



## Bakery Packing Algorithm

The bakery packing algorithm is an implementation of the <a href='https://en.wikipedia.org/wiki/Change-making_problem'>coin change algorithm</a>. 

Given an positive integer *W*, find a set of non-negative integers from a set *S* = {x_1, x_2, x_3, ..., x_n} with each x_n representing how often the element is used that minimizes *W*. 

Find a function that minimizes *W* (*f(W)*)

![Equation 1](https://raw.githubusercontent.com/mrkjse/BakeryProblem/master/eq1.PNG)

subject to

![Equation 2](https://raw.githubusercontent.com/mrkjse/BakeryProblem/master/eq2.PNG)

This can be solved using *dynamic programming*. From Wikipedia:


> A classic dynamic programming strategy works upward by finding the combinations of **all smaller values that would sum to the current threshold.**[3] Thus, at each threshold, all previous thresholds are potentially considered to work upward to the goal amount W. For this reason, this dynamic programming approach may require a number of steps that is at least quadratic in the goal amount W.


But the elements in set *S* should be placed in an ascending order.

### Example

Given *W = 15*, find *f(W)* from *S* = {3, 5, 10}.

The goal is to find the *smallest* set with elements only coming from *S* that would add up to *W*.

Using dynamic programming will yield the following solution:

```python
Given:
W = 15
S = [3, 5, 10]

Result:
[3] = [3, 3, 3, 3, 3]
[3, 5] = None
[3, 5, 10] = None

[5] = [5, 5, 5]
[5, 10] = [5, 10]

[10] = None

Optimal Solution: [5, 10] with only 2 elements.
```



## Deployment Steps

### Prerequisites
This project is written in Python 3 and is programmed to run using Anaconda. You can download the latest version (with Python 3) <a href='https://www.anaconda.com/distribution/#download-section'> here.</a>

### Launching Steps

1. Open Anaconda prompt
2. Type the following commands:

```python
# Replace 'H:\BakeryProblem\environment.yml' with your own directory
conda env create -f H:\BakeryProblem\environment.yml
# If the warning '==> WARNING: A newer version of conda exists. <==' appears, press Enter
conda activate py4web2019
pushd H:\BakeryProblem\
python __init__.py
```

3. Open your web browser and go to: http://localhost:5000/

![Screenshot](https://raw.githubusercontent.com/mrkjse/BakeryProblem/master/sample1.PNG)

### Sample Run

![Screenshot](https://raw.githubusercontent.com/mrkjse/BakeryProblem/master/run1.PNG)


## Tests

A Python module called `testcases.py` is included that has some test cases for this project. To run, just open Anaconda prompt and execute the script: `python testcases.py`.


![TestCase screenshot](https://raw.githubusercontent.com/mrkjse/BakeryProblem/master/test1.PNG)
