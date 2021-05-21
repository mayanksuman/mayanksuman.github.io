---
layout: post
date: 21-05-2021
title: Closure Functions
Category: Programming
Tags: first-class functions, python, luajit, javascript
---

Closure are higher-order functions which return lower-order function (usually first-order function) with its environment. Defining closure functions is possible in languages which has [first-class functions](|filename|first_class_functions.md) like Python, JavaScript, Lua, Scheme, and others.

## Example
```python
def divisiblity_check(divisor):
	"""Factory for producing functions that check divisiblity with divisor."""
	def inner_func(divident):
		return (divident % divisor == 0)

	return inner_func
```

This closure function (`divisiblity_check`) is return another function as evident by syntax. It should be noted that environment for inner function (***i.e.***, the variable `divisor`) is also saved with the returned function. Hence, following line of codes work:

```python
div_by_7 = divisiblity_check(7)
div_by_19 = divisiblity_check(19)

div_by_7(38)  # return false
div_by_19(38) # return true
div_by_7(35)  # return true
div_by_19(35) # return false
```

Here, although the functions `div_by_7` and `div_by_19` are returned by same closure function; however they have different environment attached to them and hence produce different results. The example closure function (***i.e.***, `divisiblity_check`) can also be defined using anonymous function.

```python
def divisiblity_check(divisor):
	"""Factory for producing functions that check divisiblity with divisor."""

	return lambda divident: (divident % divisor == 0)
```

This usage is sometimes called anonymous closure function.
