import random

SmallAlpa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",   "t", "u", "v", "w", "x", "y", "z"]

BigAlpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

Nums = ["1","2","3","4","5","6","7","8","9","0"]

SpecileChar = ["!","@","#","$","%","^","&","*","(",")","~","[","]","{","}","/","|"]


#Defind the Numbers of Password Characters...

snum = int(input("Enter No. of Small Character of Your Password:- "))
BNUM = int(input("Enter No. of Big Character of your Password:- "))
Number = int(input("Enter No. of Numbers of your password:- "))
Specile = int(input("Enter No. of Special Character of your Password:- "))


#Defind Password Length....!!!!

small = random.sample(SmallAlpa,snum)
big = random.sample(BigAlpha,BNUM)
nums = random.sample(Nums, Number)
spcl = random.sample(SpecileChar, Specile)

Final_Password = small+ big+nums+spcl

answer = "".join(Final_Password)

  
print(answer)
