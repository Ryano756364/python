# Variables and Types
* great video to watch https://youtu.be/_AEJHKGk9ns

* Python uses terms *name* and *value* instead of *variable*

### Name
* what would be called variable
* same way that your name refers you but does not contain you

### Value
* particular instance of data in memory 
* *variable* refers to a combination of the two; a name that refers to a value

## Assignment 
    answer = 42
* the name answer is bound to the value 42
* this operation of binding is referred to as an *assignment*
    > insight = answer
* *answer* and *insight* both point to the same value in memory
* regarding "is"
  * checks not if two values are the same, but whether they both point to the same spot in memory
  * "is" compares identity

### Example
    spam = 123456789
    maps = spam
    eggs = 123456789

    spam == maps #True
    spam == eggs #True

    spam is maps #True
    spam is eggs #False

* spam and maps share an *identity*
* in the beginning only use *is* to check if something is *None*

## Data Types
* Python is a dynamically typed language
* You can *name* anything, but you are bound to what you can do with a particular *value*

### type() function
    print(type(answer))    #prints <class 'int'>

    if type(answer) is int:
        #do something

    if isinstance(answer, int):
        #do something
        #this may be better as is accounts for sub-classes and inhertitance
* using built-in type()
* everything in Python is an object
* there is usually a need for either, developers love a more dynamic approach

## Scope and Garbage Collection
* names have scope, values do not
* **loops do not have their own scope!**
* accessing outside a function will not work
* returned values are not deleted when a function is complete

## Global scope
    high_score = 10

    def score():
        global high_score
        new_score = 465
        if new_score > high_score:
            print("New high score")
            high_score = new_score

    score()
    print(high_score)    #prints 465
* when a name is defined within a module but outside any function, class, or comprehension
* use a class when too many global scopes become present

### Bad code
    current_score = 0

    def score():
        new_score = 465
        current_score = new_score

    score()
    print(current_score)    #prints 0

    #no errors will rise from this

### Good code
    current_score = 0

    def score():
        global current_score
        new_score = 465
        current_score = new_score

    score()
    print(current_score)    #prints 465

    #no errors will rise from this

### The nonlocal keyword
    spam = True

    def order():
        eggs = 12

        def cook():
            nonlocal eggs

            if spam:
                print("Spam!")

            if eggs:
                egg -= 1
                print("...and eggs.")

        cook()

    order()

* The nonlocal will search back one nested loop and then another until it determines it doesn't exist in a nonglobal enclosed scope

### Scope Resolution Order
* LEGB
  * Local
  * Enclosing-function locals (that is, anything found via nonlocal)
  * Global
  * Built-in

### Classes and scope
    class Nutrimatic:
        output = "Something almost, but not quite, entirely unlike tea."

        def request(self, beverage)
            return self.output

    machine = Nutrimatic()
    mug = machine.request("Tea")
    
    print(mug) #prints "Something almost..."
    print(machine.output)
    print(Nutrimatic.output)

    #these all print the same

* classes have own way of dealing with scope
* every name in class is an *attribute*

## The Immutable Truth
* values in Python are either *immutable* or *mutable*
  * the difference lies in whether they can be *modified in place*
    * meaning can they be changed right where they are in memory

### Immutable
    eggs = 12
    carton = eggs
    eggs is carton    #True
    eggs += 1
    eggs is carton    #False
    eggs    #13
    carton    #12

* cannot be modified in place
* when eggs is modified, it's bound to a new value
  * so no longer shares identity with carton
* examples are int, float, str, and tuple

### Mutable
    temps = [87, 76, 79]
    highs = temps
    temps is highs    #True
    temps += [81]
    temps is highs    #True
    print(highs)    #[87, 76, 79, 81]
    print(temps)    #[87, 76, 79, 81]


## Passing by Assignment
    def greet(person):
        print(f"Hello, {person}.")

    my_name = "Jason"
    greet(my_name)

* Python does not either pass by *value* or *reference*
* it passes by assignment
* ...
* there is one copy of Jason in memory
  * and then it is bound to the name my_name
  * when myi_name is passed to the greet() function, its the same as
    * person = my_name

### Passing by assignment gets tricky when working with mutable values
    def find_lowest(tempuratures):
        temperatures.sort()
        print(tempuratures[0])

* this is bad as all other names bound to this value are also sorted

### This is good
    def find_lowest(tempuratures):
        sorted_temps = sorted(temperatures) #sorted returns a new list
        print(sorted_temps[0])

## Collections and References
    scores_team_1 = [100, 95, 120]
    scores_team_2 = [45, 30, 10]
    scores_team_3 = [200, 35, 190]

    scores = (scores_team_1, scores_team_2, scores_team_3)

    scores_team_1[0] = 300
    scores[0]    #[300, 95, 120]

    scores[0][0] = 400
    scores[0]    #[400, 95, 120]

* **individual items are references**
* just as name is bound to a value
  * so also are items in collections bound to values, in the same manner
* the binding is called reference
* ...
* tuples cannot be changed, but their values they hold can

## Shallow Copy (bad)
    class Taco:

        def _init_(self, toppings):
            self.ingredients = toppings

        def add_sauce(self, sauce);
            self.ingredients.append(sauce)

    default_toppings = ["Lettuce", "Tomato", "Beef"]
    mild_taco = Taco(default_toppings)
    hot_taco = Taco(default_toppings)
    hot_taco.add_sauce("Salsa")

    hot_taco.ingredients    #['Lettuce', 'Tomato', 'Beef', 'Salsa']
    mild_taco.ingredients    #['Lettuce', 'Tomato', 'Beef', 'Salsa']
    default_toppings    #['Lettuce', 'Tomato', 'Beef', 'Salsa']

* *shallow copy* is in contrast to *deep copy*

## Shallow Copy (good)
    import copy

    class Taco:

        def _init_(self, toppings):
            self.ingredients = copy.copy(Toppings)

        def add_sauce(self, sauce);
            self.ingredients.append(sauce)

    default_toppings = ["Lettuce", "Tomato", "Beef"]
    mild_taco = Taco(default_toppings)
    hot_taco = Taco(default_toppings)
    hot_taco.add_sauce("Salsa")

    hot_taco.ingredients    #['Lettuce', 'Tomato', 'Beef', 'Salsa']
    mild_taco.ingredients    #['Lettuce', 'Tomato', 'Beef']
    default_toppings    #['Lettuce', 'Tomato', 'Beef']

## Deep Copy (bad)
    default_toppings = ["Lettuce", "Tomato", "Beef"]
    mild_taco = Taco(default_toppings)
    hot_taco = copy.copy(mild_taco)
    hot_taco.add_sauce("Salsa")

    hot_taco.ingredients    #['Lettuce', 'Tomato', 'Beef', 'Salsa']
    mild_taco.ingredients    #['Lettuce', 'Tomato', 'Beef', 'Salsa']
    default_toppings    #['Lettuce', 'Tomato', 'Beef']

## Deep Copy (good)
    default_toppings = ["Lettuce", "Tomato", "Beef"]
    mild_taco = Taco(default_toppings)
    hot_taco = copy.deepcopy(mild_taco)
    hot_taco.add_sauce("Salsa")

    hot_taco.ingredients    #['Lettuce', 'Tomato', 'Beef', 'Salsa']
    mild_taco.ingredients    #['Lettuce', 'Tomato', 'Beef']
    default_toppings    #['Lettuce', 'Tomato', 'Beef']

## Coercion and Conversion
* Coercion
  * allowing Python to figure out the conversions by itself
  * examples
    * print(42.5)    #coerces to a string
    * x = 5 + 1.5    #coerces to a float (6.5)
* Conversion
  * process of explicit casting a value of one type to another type
    > life = "42"
  * conversion
    > answer = float(life)
  * What is going on here is the float class has an initializer (__ init __())
  * that accepts a string as an argument
  * The float() object is initialized
    * then passed *life* to it
      * then bind the resulting object to the name *answer*

## Page 117
* Many great definitions here to review!