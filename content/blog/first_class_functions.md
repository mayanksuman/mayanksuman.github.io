---
layout: post
date: 2021-05-20
title: First Class Functions
Category: Programming
Tags: first-class functions, python, luajit, javascript
---

In most programming languages, type, object, entity, or value is considered first-class object and hence can be returned from a function, modified or assigned to a variable. If a programming language considers functions as first-class object, then the programming language is said to have first-class functions. Hence, in such programming languages (like Python, JavaScript and others), a function can be assigned to variable, modified or returned from a higher order function. Usually such languages also supports anonymous functions.

First-class function is one of the necessity for functional programming; hence all functional programming languages (such as Haskell, Scala, Clojure etc.) have first-class functions.

## Example

```python
p = print
p("Hi! Check out this text.")
p.__call__("Hi! Check out this text.")
```

Here `print` function is assigned to variable `p` and then called using syntax `p(...)` similar to `print(...)`. It should be noted that the last line is specific to python only. In python almost every thing is a object. Functions are special object that `__call__` data structure function (or member) defined for them. This `__call__` member function have all the logic for the parent function; hence calling `print(...)` is same as `print.__call__(...)`.
