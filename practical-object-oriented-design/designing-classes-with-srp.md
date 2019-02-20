## Designing Classes with a Single Responsibility

### Deciding What Belongs in a Class
#### Grouping Methods into Classes
#### Organizing Code to Allow for Easy Changes
Easy to change code defined as:
* Changes have no unexpected side effects
* Small changes in requirements require correspondingly small 
changes in code
* Existing code is easy to reuse
* The easiest way to make a change is to add code that in itself 
is easy to change
 
Code you write should have following qualities:
* **Transparent** - the consequences of change should be obvious 
in the code that is changing and in distant code that relies 
upon it
* **Reasonable** - the cost of any change should be proportional 
to the benefits change achieves
* **Usable** - Existing code should be usable in new and 
unexpected contexts
* **Exemplary** - the code itself should encourage those who
change it to perpetuate these qualities
### Creating Classes that have a Single Responsibility
#### An Example Application: Bicycle and Gears
#### Why Single Responsibility Matters
Classes that have more than one responsibility:
* Are hard to change
* Are difficult to reuse
* Have more dependencies
#### Determining If a Class Has a Single Responsibility
* Question of form: "[class] what is your [method name]?" should 
make sense.
* You should be able to describe class in one sentence. If sentence has:
    * And - most likely class has more than one responsibility
    * Or - most likely class has more than one responsibility 
    and they are not closely related
#### Determining When to Make Design Decisions
* Resist urge to make premature design decisions
* Ask yourself: what is the future cost of doing nothing today
    * When the future cost of doing nothing is the same as current cost 
    postpone the decision
    * Make the decision only when you have to
### Writing Code That Embraces Change
#### Depend on Behavior, Not Data
* Always wrap instance variables in accessor methods
* Avoid complex data structures. If complex data structure is received 
convert it to wrapping data structure that is easy to work with
#### Enforce Single Responsibility Everywhere
* Enforce SRP for methods
* Methods following SRP will have qualities:
    * Expose previously hidden qualities
    * Avoid the need for comments
    * Encourage reuse
    * Are easy to move to another class
### Finally, the Real Wheel
### Summary
