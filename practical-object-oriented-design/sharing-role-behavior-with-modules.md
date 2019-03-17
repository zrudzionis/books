## Sharing Role Behavior with Modules

### Understanding Roles
#### Finding Roles
Ruby modules are similar to mixin classes. It 
differs in a way that modules do not use inheritance.
Ruby modules are like objects used in composition 
but they avoid explicit dependency.
#### Organizing Responsibilities
#### Removing Unnecessary Dependencies
* Let objects speak for themselves 
(StringUtils.empty(string) vs string.empty())
#### Writing the Concrete Code
* Write concrete methods first, later move 
them to interface
#### Extracting the Abstraction
Modules represent behaves-like-a and 
inheritance represents is-a
 relationship.
#### Looking Up Methods
#### Inheriting Role Behavior
### Writing Inheritable Code
#### Recognize the Antipatterns
* Class driven behavior is an indication of bad design
#### Insist on the Abstraction
Abstract class methods should apply to every subclass. 
If subclass raises NotImplementedError in inherited 
method that means that it "does not do that" which 
implies that it "is not that thing".
* Subclasses must honor parent contract
#### Honor the Contract
* Follow Liskov Substitution Principle
#### Use the Template Method Pattern
* Use template method pattern to describe algorithm
#### Preemptively Decouple Classes
* Avoid writing code that requires 
its inheritors to send super
* Use hook messages to decouple from parent class
#### Create Shallow Hierarchies
* Prefer shallow hierarchies
### Summary
