---
date: 2021-05-27
title: Peculiar case for modular powers
status: hidden
--

When modular power is raised to a integer coprime with divisor then there are
less possible number of remainder (hence less congruent classes).

```python
{i**1%15 for i in range(1, 16)}  # returns {0, 1, 2, 3, ..., 14}
{i**2%15 for i in range(1, 16)}  # returns {0, 1, 4, 6, 9, 10}
{i**3%15 for i in range(1, 16)}  # returns {0, 1, 2, 3, ..., 14}
{i**4%15 for i in range(1, 16)}  # returns {0, 1, 6, 10}
{i**5%15 for i in range(1, 16)}  # returns {0, 1, 2, 3, ..., 14}

# similarly
{i**1%35 for i in range(1, 36)}   #{0, 1, 2, ..., 34}
{i**2%35 for i in range(1, 36)}   #{0, 1, 4, 9, 11, 14, 15, 16, 21, 25, 29, 30}
{i**3%35 for i in range(1, 36)}   #{0, 1, 6, 7, 8, 13, 14, 15, 20, 21, 22, 27, 28, 29, 34}
{i**4%35 for i in range(1, 36)}   #{0, 1, 11, 15, 16, 21, 25, 30}
{i**5%35 for i in range(1, 36)}   #{0, 1, 2, ..., 34}
{i**6%35 for i in range(1, 36)}   #{0, 1, 14, 15, 21, 29}
{i**7%35 for i in range(1, 36)}   #{0, 1, 2, ..., 34}
{i**8%35 for i in range(1, 36)}   #{0, 1, 11, 15, 16, 21, 25, 30}
```
