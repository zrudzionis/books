## Acquiring Behavior Through Inheritance

### Understanding Classical Inheritance 
Inheritance is mechanism of automatic message delegation.
### Recognizing Where to Use Inheritance
#### Starting with a Concrete Class 
#### Embedding Multiple Types
Design smell: "I know who you are and because of that I know what 
you do".
#### Finding the Embedded Types
Inheritance solved problem where highly related 
types share common behavior but differ along some 
dimensions.
#### Choosing Inheritance
#### Drawing Inheritance Relationships
### Misapplying Inheritance
### Finding the Abstraction
For inheritance to work there must be 
generalization-specialization relationship.
Subclass should be everything that parent 
class is plus more.
#### Creating an Abstract Superclass
"Creating hierarchy has costs; the best way 
to minimize these costs is to maximize your 
changes of getting the abstraction right"
* Postpone decision of creating abstract class 
until there are enough concrete classes 
(information of how abstract class should look like)
#### Promoting Abstract Behavior
* When making design decisions ask yourself: 
"What are the costs of implementation and change of being wrong?"
* Promote abstractions rather than demote concretions
#### Separating Abstract from Concrete
#### Using the Template Method Pattern
#### Implementing Every Template Method
* Make requirements to subclasses explicit
### Managing Coupling Between Superclasses and Subclasses
#### Understanding Coupling
Using `super` in subclass creates dependency to superclass.
#### Decoupling Subclasses Using Hook Messages
* Decouple from superclass whenever possible
### Summary

