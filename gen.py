s = ""
n = 2 # Camp Number
w = 15 # weeks
h = 8 # hours

for i in range(1,w+1):
    if i == 1:
        req = None
    else:
        req = f"{n} - {i-1}"
    if i == w:
        next = None
    else:
        next = f"Scala {n} - {i+1}"
    s += f"""
# Module: Scala {n} - {i}    

## Length: {h}h 

## Prerequisites: {req}

## Learning objectives

## Activities

## Demonstration

## Practice

## Assessment



## Resources
[Scala Docs](https://docs.scala-lang.org/)

[Programming in Scala](https://www.oreilly.com/library/view/programming-in-scala/9780981531687/)

## Required for {next}

<div style="page-break-after: always;"></div>   
    
"""

with open(f'scala_{n}_{w*h}h.md', mode='w') as f:
    f.write(s)