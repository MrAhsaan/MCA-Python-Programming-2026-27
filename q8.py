#8. Write a Python program to accept three sides of a triangle, determine whether they form a valid triangle, and if valid, classify it as Equilateral, Isosceles, or Scalene.

s1 = int(input("Enter side1 of Triangle "))
s2 = int(input("Enter side2 of Triangle "))
s3 = int(input("Enter side3 of Triangle "))

if (s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1):
    print("valid Triangle...")
    if s1==s2==s3:
        print("Equilateral Triangle")
    elif s1==s2!=s3 or s2==s3!=s1 or s3==s1!=s2:
        print("Isosceles Triangle")
    else:
        print("Scalane Triangle")
else:
    print("Not Valid Triangle!!")

