---
layout: default
---
# Final Examples

## Classes

* Example codes may be provided later (or may be not :)...

{:.q}
> Q: (Template) Give the equivalent of the following class definition which is in language A, in languages B and C.

## Haskell

* List Comprehensions ([link](http://learnyouahaskell.com/starting-out#im-a-list-comprehension) to book chapter)

{:.q}
> Q: Solve question 2 given in our [first lab exercise](http://ceng.mu.edu.tr/~pembeci/ceng2002/lab1.html) by using list
comprehensions.

{:.q}
> Q: Give the values of the following expressions:
>
> {% highlight haskell%}
exp1 = [x+y | x <- [3..6], y <- drop x [10,13..30]]
exp2 = [x+y | x <- [3..6], y <- drop x [10,13..30]]
-- to be used in exp3
letters = ['A'..'E']
nums    = [1..5]
--
f letter num = [ (letters !! (i-1), nums !! (j-1))
                   | i <- nums, j <- nums,
                     abs(x-i) == abs(y-j),
                     (x,y) /= (i,j)
               ]
    where
     x = case letter of
          'A' -> 1
          'B' -> 2
          'C' -> 3
          'D' -> 4
          'E' -> 5
          _   -> error "wrong arg"
     y = if num >= 1 && num <= 5 then num else error "wrong arg"
--
exp3 = f 'B' 2
{% endhighlight %}

* Syntax in functions ([link](http://learnyouahaskell.com/syntax-in-functions) to book chapter)

{:.q}
> Q: Give the output of each application of function `patrQ`. If there would be an error, state that as well.
> {% highlight haskell %}
-- Patterns in function
-- Function definition
patrQ [] (y:ys) = ys ++ [y]
patrQ (x:xs) (y:[]) = [x] ++ y:xs
patrQ (x:[]) (y:ys) = [y] ++ ys ++ [x]
patrQ (x1:x2:xs) (y1:y2:[]) = x2:y2:y1:x1:xs
patrQ xs (y:ys) = [head ys] ++ y:tail xs
patrQ xs _  = xs ++ xs
-- Applications
patrQ "ABCDE" "12"
patrQ "ABCDE" "1234"
patrQ "A" "123"
patrQ "A" "1"
patrQ "ABC" "1"
patrQ "ABCDEF" "12"
patrQ "AB" "12"
patrQ "AB" "123"
patrQ "" ""
patrQ "" "123"
patrQ "ABC" ""
{% endhighlight %}

{:.q}
> Q: Give 7 different calls of function `guardQ` where each call will produce a different value ("Answer1" through "Answer7").
> Don't forget to specify which call produces which value.
> {% highlight haskell %}
-- Guards, if and case expressions
guardQ x y
  | x < y  = if even x then "Answer1"
                        else (if odd y then "Answer2" else "Answer3")
  | x > y  = case x+y of
               10 -> "Answer4"
               15 -> "Answer5"
               _  -> "Answer6"
  | otherwise = "Answer7"
{% endhighlight %}

* Polymorphism and Type Inference ([link](http://learnyouahaskell.com/types-and-typeclasses) to book chapter)

{:.q}
> Q: For each of the following functions give its type signature. Don't forget to include type
> constraints like `Num t => ...` or `Ord a => ...`.
> {% highlight haskell %}
t1 x y = (y, x, y)
t2 x y = (y, x, if x == y then x else y)
t3 x y = (y, x - 1, if x == y then x else y)
t4 x y = (y, x - 1.5, if x == y then x else y)
t5 x y = (y, x, if x < y then x else y)
t6 x y = x ++ y
t7 x y = x ++ y ++ "XYZ"
t8 x y = (x, y ++ "XYZ")
t9 x y = (x ++ tail y, y ++ "XYZ")
t10 x y = x ++ y ++ [(head y - 2.5)]
t11 (x:xs) (y:ys) = xs ++ ys
t12 (x:xs) (y:ys) = xs ++ y
t13 (x:xs) (y:ys) = take x ys
t14 (x:xs) (y:ys) = take (x-y) ys
t15 (x:xs) (y:ys) = (take x ys) ++ "ABC"
t16 (x:xs) (y:ys) (z:zs)= (take x ys) ++ zs
t17 (x:xs) (y:ys) (z:zs)= (take x ys) ++ z
t18 (x:xs) (y:ys) (z:zs)= (take x ys) ++ z ++ [head z - x]
{% endhighlight %}

## Higher Order Functions in Haskell ([link](http://learnyouahaskell.com/higher-order-functions) to book chapter)

{:.q}
> Q: What will be the value of `result_` expressions below:
>
> {% highlight haskell %}
c x y z = 3*x + 5*y - z
c1 = c 10
c2 = c 3 3
result1 = c1 2 4
result2 = c2 4
result3 = map (c 4 3) [1,4,9]
result4 = map (\x -> c x 10 5) [1,4,9]
result5 = map (\f -> f 10) (map (\ (x,y) -> c x y) (zip [1,2,10] [4,5,4]))
{% endhighlight %}

## Haskell and other languages

{:.q}
> Q: Implement the quicksort algorithm in Python, Javascript, and Java as close to as its Haskell definition below
(see the related book [section](http://learnyouahaskell.com/recursion#quick-sort) if you don't get how it works):
>
> {% highlight haskell %}
quicksort :: (Ord a) => [a] -> [a]  
quicksort [] = []  
quicksort (x:xs) =
    let smallerSorted = quicksort [a | a <- xs, a <= x]  
        biggerSorted = quicksort [a | a <- xs, a > x]  
    in  smallerSorted ++ [x] ++ biggerSorted
{% endhighlight %}


### That's all folks for now. I may add more examples later. See you at the final...
