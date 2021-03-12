1. Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null. 
<br />
You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

Example, given the string `the quick brown fox jumps over the lazy dog` and `k = 10`, you should return: `["the quick", "brown fox", "jumps over", "the lazy", "dog"]`. No string in the list has a length of more than 10.

[sentence break](20.DCP/dcp_001.py)

----

This problem was asked by Google.

2. A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are `2, 3, and 5`.
<br />
These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.

[regular number](20.DCP/dcp_002.py)

----

This problem was asked by Facebook.

3. Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a mathematical expression to obtain the answer.
<br />
Don't use eval or a similar built-in parser.

For example, given `-1 + (2 + 3)`, you should return `4`.

[calculator](20.DCP/dcp_003.py)

----

This problem was asked by Stripe.

4. Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:
```
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
```
[flatten dictionary](20.DCP/dcp_004.py)

----
This problem was asked by Mozilla.

5. A bridge in a connected (undirected) graph is an edge that, if removed, causes the graph to become disconnected. Find all the bridges in a graph.

[bridges](20.DCP/dcp_005.py)

----

