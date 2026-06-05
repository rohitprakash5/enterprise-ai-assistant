from typing import List, Dict

#!/usr/bin/env python3
"""
Basic Python learning script.
Run and pick options to see small examples of core concepts.
"""



def hello_world():
    print("Hello, world!")


def variables_and_types():
    name: str = input("Enter your name: ").strip() or "Anonymous"
    age: int = int(input("Enter your age: ") or 0)
    pi: float = 3.14159
    is_student: bool = True
    print(f"Name: {name}, Age: {age}, Pi ~ {pi}, Student? {is_student}")


def arithmetic_examples():
    a, b = 7, 3
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b:.2f}")
    print(f"{a} // {b} = {a // b} (floor div), {a} % {b} = {a % b} (mod)")


def control_flow_examples():
    n = int(input("Enter a number for loop examples: ") or 5)
    print("for loop:")
    for i in range(n):
        print(i, end=" ")
    print("\nwhile loop (count down):")
    while n > 0:
        print(n, end=" ")
        n -= 1
    print()


def functions_and_recursion():
    def factorial(n: int) -> int:
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    num = int(input("Factorial of? ") or 5)
    print(f"{num}! = {factorial(num)}")


def lists_and_comprehensions():
    items: List[int] = [1, 2, 3, 4, 5]
    squares = [x * x for x in items]
    evens = [x for x in items if x % 2 == 0]
    print("items:", items)
    print("squares:", squares)
    print("evens:", evens)


def dicts_and_collections():
    text = input("Type a short sentence: ") or "this is a test"
    freq: Dict[str, int] = {}
    for word in text.split():
        freq[word] = freq.get(word, 0) + 1
    print("word frequencies:", freq)


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age}."


def classes_example():
    p = Person("Alice", 30)
    print(p.greet())
    # create from input
    name = input("Name for new person? ") or "Bob"
    age = int(input("Age? ") or 20)
    print(Person(name, age).greet())


def file_io_example():
    fname = "sample.txt"
    try:
        with open(fname, "w", encoding="utf-8") as f:
            f.write("line1\nline2\n")
        with open(fname, "r", encoding="utf-8") as f:
            print("File contents:")
            print(f.read())
    except OSError as e:
        print("File error:", e)


def exceptions_example():
    try:
        x = int(input("Enter an integer: "))
        print("You entered", x)
    except ValueError:
        print("That's not an integer!")


def small_tools():
    s = input("String to check palindrome? ") or "radar"
    print("Palindrome?" , s == s[::-1])
    n = int(input("Prime check number? ") or 13)
    if n < 2:
        print(f"{n} is not prime")
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is composite (divisible by {i})")
            return
    print(f"{n} is prime")


def menu():
    options = [
        ("Hello world", hello_world),
        ("Variables & types", variables_and_types),
        ("Arithmetic", arithmetic_examples),
        ("Control flow", control_flow_examples),
        ("Functions & recursion", functions_and_recursion),
        ("Lists & comprehensions", lists_and_comprehensions),
        ("Dicts & collections", dicts_and_collections),
        ("Classes", classes_example),
        ("File I/O", file_io_example),
        ("Exceptions", exceptions_example),
        ("Small tools (palindrome, prime)", small_tools),
        ("Quit", None),
    ]
    while True:
        print("\nChoose an example:")
        for i, (name, _) in enumerate(options, 1):
            print(f"{i}. {name}")
        choice = int(input("Option: ") or 12)
        if choice < 1 or choice > len(options):
            print("Invalid choice")
            continue
        if options[choice - 1][1] is None:
            print("Goodbye")
            break
        options[choice - 1][1]()


if __name__ == "__main__":
    menu()