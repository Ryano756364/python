# Functions and Lambdas

## Functional Programming
- organized around functions
  - meaning problems are broken down into steps
  - you write a function for each step
  - once a function is complete, all of its local names go out of scope
    - which means they lack *state*
  - functions shouldn't mutate anything
    - should create new lists for example
  - as long as the input and output are consistent, it doesn't matter how you accomplish this task
  - top rules
    - a) every function should do one thing
    - b) function's implementation should never affect behavior of the rest of the program
    - c) avoid side effects. The one exception to this should occur when a function belongs to an object.
      - in that case, the function should only be able to mutate that object's members
    - d) in general, functions shouldn't have (or be affected by) state. 
      - Providing the same input should always yield the same output

## Python Function Essentials
    import random

    def roll_dice(sides):
        return random.randint(1, sides)

    #this is a pure function because it has no side affects
    #it accepts a value as an input and returns a value as an output

    #could also do a tuple
    def roll_dice(sides, dice):
        return tuple(random.randint(1, sides) for _ in range(dice))

    #dice is the number of dice being rolled
    #the return is a generator-expression

- parameter
  - slot in the function definition that accepts some data
- argument
  - the data that is passed to the parameter in the function call

## Recursion
    #when a function calls itself
    #when you need to repeat the logic and a loop doesn't feel right or seems too cluttered

    import random

    def roll_dice(sides, dice):
        if dice < 1:
            return()
        roll = random.randint(1, sides)
        return (roll, ) + roll_dice(sides, dice - 1)

    #the previous generator expression is usually considered more Pythonic
    #the recursion depth limit is 1000 but can be overridden 

    #example
    #find 5!

    #algorithm
    #function getFactorial(n)
        #if n < 2, return 1
        #else return n * getFacorial(n - 1)

    def get_recursive_factorial(n):
        if n < 0:
            return -1
        elif n < 2: 
            return 1
        else:
            return n * get_recursive_factorial(n-1)

    def get_iterative_factorial(n):
        if n < 0:
            return -1
        else:
            fact = 1
            for i in range( 1, n + 1):
                fact *= i
            return fact

    get_recursive_factorial(6)    #720
    get_iterative_factorial(6)    #720


- typically no calculations are done until the base case is reached
- requires more memory, so not good for large problems
- extremely practical for tree traversals and binary search

## Default Argument Values
    import random
  
    def roll_dice(sides, dice=1):
        return tuple(random.randint(1, sides) for _ in range(dice))

- dice=1 is the default setup
- will enact when second argument isn't specified
  - this is called an *optional parameter*
- if no default setup
  - called *required parameter*
- must list required before optional
- **never use mutable values for default argument types**
  - instead use **none**
  - then create new mutable value *if* that default is being used

## Keyword Arguments
    # help resolve readability of multiple parameters by attaching labels to arguments in function calls

    #instead of this
    dice_cup = roll_dice(6, 5)

    #do this
    dice_cup = roll_dice(sides = 6, dice = 5)

    #when using keyword arguments, order doesn't necessarily matter

    #this is possible too
    dice_cups =roll_dice(6, dice = 5)
- positional arguments
  - arguments that are mapped to their parameters by the order you pass them in

## Overloaded Functions
- Python doesn't need them
  - but if truly needed (which you probably won't) - then use *single-dispatch functions*

## Variadic Arguments
    import random

    def roll_dice(*dice):
      return tuple(random.randint(1, d) for d in dice)

    # *dice now turned into a variadic parameter
    # all arguments passed to roll_dice will now be packed into a tuple, bound to the name dice
    # then using generator expression to use tuple
    # must come after any positional parameters in the function definition

    # example
    dice_cup = roll_dice(6, 6, 6, 6, 6, 6)
    
    bunch_o_dice = roll_dice(20, 6, 8, 4)

    def roll_dice(*dice):
        if dice:
            roll = random.randint(1, dice[0])
            return (roll, ) + roll_dice(*dice [1:])
        return()


- aka arbitary arguments list
  - automatically pack multiple arguments into a single variadic parameter

## Keyword Variadic Arguments
    # precede parameter with two asteriks (**)

    def call_something_else(func, *args, **kwargs):
        return func(*args, **kwargs)

    # func -> positional argument
    # args -> positional variadic (not required)
    # kwards -> keyword variadic parameters (not required)

    # example
    def say_hi(name):
        print(f"Hello, {name}")

    call_something_else(say_hi, name="Bob")

    # prints -> Hello, Bob!

## Keyword-Only Parameters
    import random

    def roll_dice(*, sides = 6, dice = 1):
        return tuple(random.randomint(1, sides) for _ in range(dice))

    #contains two keyword-only parameters

    # * -> unnamed variadic parameter, this ensures that every parameter that follows it in the list can only be accessed by name

## Positional-Only Parameters
    # useful when parameter name is either unhelpful or likely to be changed down the road

    import random

    def roll_dice(dice = 1, /, sides = 6):
        return tuple(random.randomint(1, sides) for _ in range(dice))

    # dice = 1 -> dice has default value of 1
    # but it is now positional-only
    # sides, however, can be used as a positional or a keyword parameter

    # examples
    roll_dice(4, 20)                    #ok, dice = 4, sides = 20
    roll_dice(4)                        #ok, dice = 4, sides = 6
    roll_dice(sides = 20)               #ok, dice = 1, sides = 20
    roll_dice(4, sides = 20)            #ok, dice = 4, sides = 20

    roll_dice(dice = 4)                 #TypeError
    roll_dice(dice = 4, sides = 20)     #TypeError

    # first 4 are ok because positional-only argument is either first or omitted altogether
    # last two attempt to access dice by keyword

## Recap
    def func(pos_only = None, /, pos_kw = None, *, kw_only = None

    # pos_only is posiiton-only as it comes before the /
      # must appear first in list
      # if argument is passed to function, it must be first argument
      # otherwise TypeError occurs
    # pos_kw is either positional or keyword
      # also is after the /, if there is one
    # kw_only
    
    # in this example if function recieves more than two positional arguments
      # TypeError will occur

## Nested Functions
    import random

    def roll_dice(sides=6, dice=1):
        def roll():
            return random.randint(1, sides)

        if dice < 1:
            return()
        return (roll(), ) + roll_dice(sides, dice-1)

    # def roll is a nested function
    # can be called anywhere in the function roll_dice()
    # can access the names of its enclosing scope
    # if wanting to rebind or mutate, need to use nonlocal keyword

## Closures
    # can create a kind of function that builds and returns a kind of function called a closure
    # "function factory"
    
    import random

    def make_dice_cup(sides=6, dice=1):
        def roll():
            return tuple(random.randint(1, sides) for _ in range(dice))

        return roll

    roll_for_damage = make_dice_cup(sides=8, dice=5)
    damage = roll_for_damage()
    print(damage)

    # no paranthesis on roll
    # caution with closures when it has the ability to mutate the values it encloses

## Recursion with Closures
    import random

    def make_dice_cup(side=6, dice=1):
        def roll(dice=dice):
            if dice < 1:
                return ()
            die = random.randint(1, sides)
            return (die, ) + roll(dice - 1)
    
        return roll

    # used nonlocal name dice as default value of the new, local parameter, dice
    # this only works with immutable types

## Stateful Closures
    # a closure that retinas a little bit of state between calls that it can use
    # try to avoid this unless it's a last resort

    import random

    def start_turn(limit, dice=5, sides=6):
        def roll():
            nonlocal limit
            if limit < 1:
                return None
            limit -= 1
            return tuple(random.randint(1, sides) for _ in range(dice))
  
        return roll

    turn1 = start_turn(limit=3)
    while toss := turn1():
      print(toss)

    #prints the following
    (4, 1, 2, 1, 1)
    (4, 2, 3, 1, 5)
    (1, 6, 3, 4, 2)

    # remember to use cauting when you see nonlocal in a closure

## Lambdas
    #anonymous (nameless) function made up of a single expression

    lambda x, y: x + y

    # left side of colon is parameter list, which can be omitted
    # right is the return expression which is evaluated when lambda is called 
    # to use
      # bind it to a name, whether by assignment or by passing it as an argument to another function

    # example

    add = lambda x, y: x + y
    answer = add(20, 22)
    print(answer) # outputs "42"

    #this particular lambda accepts two arguments and returns their sum

### Why lambdas are useful

