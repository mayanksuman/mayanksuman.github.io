---
layout: post
title: Natural Numbers
date: 2021-06-25
category: Maths
tag: real_analysis
---

Natural numbers are numbers that follows Peano axioms.

### Peano Axiom

1. 1 is a natural number.
2. If $n$ is a natural number then $n++$ is also a natural number.
3. 1 is not a successor of any natural number. Hence, $n++\neq 1$ for every natural number $n$.
4. For two natural numbers $m$ and $n$: if $m\neq n$ then $m++\neq n++$ or if $m=n$ then $m++=n++$.
5. Principle of mathematical induction: Let $P(n)$ be any property pertaining to natural number $n$. Suppose that $P(1)$ is true and suppose that whenever $P(n)$ is true, $P(n++)$ is also true. Then $P(n)$ is true for every natural number $n$.


## Operations of Natural numbers
From Peano Axioms only one operation (*i.e.* increment) is defined on natural number. The repeated application of this operation can used to define other operations on natural numbers like addition and multiplication.

### Addition
Definition: For a natural number $m$, we define $m++ = m+1$ and by induction if this addition operation can be defined for $n++$ as $m+n++ = (m+n)++ = m+(n+1)$

Based on this definition of addition, following properties of addition can be established:

1. Addition is commutative. *i.e.* $n+m = m+n$
2. Addition is associative. *i.e.* $(a+b)+c = a+(b+c)$
3. Cancellation law: if $a+b=a+c$, then $b=c$.

These properties can be proved by using principle of mathematical induction (the last Peano axiom). Moreover, the operation of addition also lead to ordering in natural number.

#### Definition of zero and whole number
Zero (written as 0) is a number whose successor is 1 and for any natural number $a$, $a+0=a$. If we include 0 in the set of natural number then the set is called whole number.

#### Ordering of natural numbers
Definition: Let $n$ and $m$ are natural numbers. We say that $n$ is equal or greater than $m$ and write it $n\geq m$ (or $m\leq n$), iff we have $n=m+a$ for some whole number $a$. We say that $n$ is strictly greater than $m$ (written as $n>m$) iff $n\geq m$ and $n\neq m$.

Using mathematical induction, following properties of ordering in whole numbers can be established ($a$, $b$, and $c$ are whole numbers):

1. Order is reflexive. $a\geq a$
2. Order is transitive. If $a\geq b$ and $b\geq c$, then $a\geq c$.
3. Order is anti-symmetric. If $a\geq b$ and $b\geq a$, then $a=b$.
4. Addition preserves order. If $a\geq b$, then $a+c \geq b+c$.
5. $a<b$ iff $a++\geq b$.
6. $a<b$ iff $b = a + d$ for some natural number d.

**Proposition 1**: Trichotomy of order for whole numbers: If $a$ and $b$ are whole numbers then exatly one of the following statements is true: $a<b$, $a=b$, or $a>b$.

**Proposition 2**: Strong principle of mathematical induction: let $m_0$ be a whole number, and let $P(m)$ be a property pertaining to an arbitrary whole number $m$. Suppose that for each $m\geq m_0$, we have the following implication: if $P(m')$ is true for all natural numbers $m_0\geq m' \geq m$, then $P(m)$ is also true. (In particular, this means that $P(m_0)$ is true, since in this case the hypothesis is vacuous.) Then we can conclude that $P(m)$ is true for all natural numbers $m\geq m_0$.
