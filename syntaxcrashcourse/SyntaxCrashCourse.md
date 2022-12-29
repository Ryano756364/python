# Syntax Crash Course

## Math
* Integers (int) 
  * Store whole numbers. No max values
* Floating-point numbers (float)
  * Store numbers with a decimal
* Complex numbers
  * store imaginary numbers by appending j to the value
    > 24 + 42j
  * imaginary number
    * has the square root of negative one as one of its factors, even though value is impossible
 * Operators
   * Absolute value prints 42
     > abs(-42)
   * Floor division, discard remainder, and evaluates to 42
     > 680 // 16
   * Exponent, evaluets to 49
     > 7 ** 2
   * AND
     > 9 & 8
   * OR
     > 9 | 8
   * XOR
     > 9 ^ 8
* How to use math functions 
  * Import math module
    > import math
    > >print(math.pi) #Prints PI
* Check documentation for complete list of everything in the math module

## Conditionals
    command = "greet"
    if command == "greet"
        print("hello!")
    elif command == "exit":
        print("Goodbye")
    else:
        print("I don't understand")
* This contains three clauses
  * If first clause is true, it's suite runs

## Comparison Operators
* Normal, nothing new here

## Boolean
    spam = True
    eggs = False
    potatoes = None
* use 'is', 'not', or 'is not'
* best practice is to use
  > if spam
* or
  > if not spam

## Truthiness
    answer = 42
    bool(answer) #True

    answer = none
    bool(answer) #False

    answer = -1
    bool(answer) #True

## Logical Operators
    if spam and eggs

    if spam or eggs

    if (not eggs) and spam
    if not eggs and spam   #not takes precedence

## Walrus Operator
    if (eggs := 7 + 5) == 12:
        print("We have a dozen eggs")

    print(eggs) #Prints 12

* What is interesting here is the eggs variable is out of scope and still works

## Strings
### String literals
    danger = "Cuidada, llamas!"
    danger = 'Cuidada, llamas!'
    danger = '''Cuidada, llamas!'''
    danger = """Cuidada, llamas!"""

    parrot = """\
        This parrot is no more!
        He has ceased to be!"""

    spam = "Hello" "World" "!"

* single or double doesn't matter, but pick one and stick to it
* use \ when needing to include " or ' in the string literal
* or use oposite of intended quotation needed when declaring a string literal
  * this method is much more readable

### Raw Strings
    print(r"I love backslashes: \ Aren't they cool?")
* Everything on the line is printed
* **Always use raw strings for regular expression patterns**

### Formatted Strings (or f-string)
    in_stock = 0
    print(f"This cheese shop has {in_stock} types of cheese.")

* You precede the string literal with an f
* Not just variables have to go in there. You can put just about anything. 

### Template Strings
    from string import Template
    s = Template("$greeting, $user")
    print(s.substitute(greeting="Hi", user="Jason"))
    #prints Hi, Jason!

### String Conversion
    str()

### String Concatenation
    greeting = "Hello"
    name = "Jason"
    message = "".join((greeting, ", ", name, "!")
    print(message)
    #prints Hello, Jason!

* Use join instead of + for concatenation 
* In order of speed
  * f-strings -> join -> concatenation

### Functions
    def tell_joke(joke_type):
        if joke_type == "funny":
            print("funny")
        else:
            print("not funny")

    tell_joke("funny") #calling function

* declared function with the def keyword, followed up name of function, followed by parameter

### Classes and Objects
    class Joke:
        def _init_(self, joke_type):
            if joke_type == "funny":
                self.answer = "Funny"
            elif joke_type == "lethal":
                self.answer = "Ja!"
            else:
                self.answer = "Not funny"

        def tell(self):
            print(self.answer)

    lethal_joke = Joke("lethal")
    lethal_joke.tell()

* everything is an object
* _ init _ is the method
* You create a new instance of the Joke class by passing the string "lethal" to its *initializer*, the _ init _ () from ealier
  * The new object is stored in the variable lethal_joke
  * Then . operator calls function tell() within the object

### Error Handling
    num_from_user = input("Enter a number: ")

    try:
        num = int(num_from_user)
    except ValueError:
        print("you didn't enter a valid number.")
        num = 0

    print(f"You number squared is {num**2}")

### Tuples and Lists

* Two of pythons most common built-in data structures called *collections*
* Lists
  * most like arrays
    > cheeses = ["swiss", "cheddar"]
  * can print out too
    > cheeses[1] #prints "cheddar"
  * can reassign values
    > cheeses[1] = mozzarella
  * then prints to
    >cheeses[1] #prints "mozzarella"
* Tuple
  * Similiar to list but has a few kew differences
    * items cannot be added, reassigned, or removed after it's creation
    * otherwise TypeError is thrown
    * they are *immutable*
  * creation of a tuple with ()
    > cheeses = ("swiss", "cheddar")

### Loops
    n = 0

    while n < 10:
        n += 1
        print(n)

    for i in range(1, 11):
        print(i)
    #technically this is a for-each loop

* Main two types: while and for
* make sure header gets the :
* *continue*
  * abandons current iteration and jumps to the next one
* *break*
  * exits loop altogether

### Structural Pattern Matching
    lunch_order = input("What would you like for lunch? ")
    
    match lunch_order:
        case 'pizza':
            #something
        case 'sandwhich':
            #something
        case 'taco':
            #something
        case _:
            #something else (known as a wildcard)

* new to Python 3.10
* not as powerful as a switch statement

### Or Patterns
    lunch_order = input("What would you like for lunch? ")
    
    match lunch_order:
        case 'pizza' | 'tacos':
            #something unhealthy
        case 'salad' | 'fruit':
            #something healthy
        case _:
            #something else (known as a wildcard)

### Caputre Patterns
    lunch_order = input("What would you like for lunch? ")
    
    match lunch_order:
        case 'pizza' | 'tacos':
            #something unhealthy
        case 'salad' | 'fruit':
            #something healthy
        case order:
            print(f"Enjoy you {order}!")

    #'lunch_order' is captured as 'order'