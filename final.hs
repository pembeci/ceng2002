import Data.List

exp1 = [if w1>w2 then w1 ++ " " ++ w2
                 else w2 ++ " " ++ w1
            | w1 <- ["ali", "mavi", "topu", "bana", "at"],
              w2 <- ["oya", "nabersin", "lan"],
              odd (length (w1++w2))
       ]
exp2 = [x+y | x <- [3..6], y <- drop x [10,13..30]]

-- to be used in exp3

letters = ['A'..'E']
nums    = [1..5]

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

exp3 = f 'B' 2

-- Patterns and guards

patrQ [] (y:ys) = ys ++ [y]
patrQ (x:xs) (y:[]) = [x] ++ y:xs
patrQ (x:[]) (y:ys) = [y] ++ ys ++ [x]
patrQ (x1:x2:xs) (y1:y2:[]) = x2:y2:y1:x1:xs
patrQ xs (y:ys) = [head ys] ++ y:tail xs
patrQ xs _  = xs ++ xs

guardQ x y
  | x < y  = if even x then "Answer1" else (if odd y then "Answer2" else "Answer3")
  | x > y  = case x+y of
               10 -> "Answer4"
               15 -> "Answer5"
               _  -> "Answer6"
  | otherwise = "Answer7"

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

c x y z = 3*x + 5*y - z
c1 = c 10
c2 = c 3 3
result1 = c1 2 4
result2 = c2 4
result3 = map (c 4 3) [1,4,9]
result4 = map (\x -> c x 10 5) [1,4,9]
result5 = map (\f -> f 10) (map (\ (x,y) -> c x y) (zip [1,2,10] [4,5,4]))
