### Design Patterns
#### Command
- If you need to invoke computation in a more complex way than simply calling a method:
  - Make an object for computation and invoke it
#### Value Object
- If you need objects that will be widely shared, but for whom identity is not important:
  - Set their state when they are created and never change it
  - Operations on such an object should return a new object
#### Null Object
- If you need to avoid client handling special cases:
  - Create and object representing special case
  - Give it the same protocol as the regular objects
#### Template method
- If you need to provide template that will be implemented in future (ex. `setup()`, `run()`, `tearDown()`):
  - Write a method that is implemented in entirely in terms of other methods
- If computation makes no sense on its own:
  - Declare abstract method
  - Throw `NotImplementedError`
#### Pluggable Object
- If you need to express variation and avoid duplication:
  - Create two or more object that implement the same interfaces and use them to perform computation 
#### Pluggable Selector
- If you need to invoke different behaviours for different instances (there are some obvious drawbacks):
  - Store the name of a method
  - Invoke method dynamically
#### Factory Method
- If you want flexibility in creating new objects:
  - Create the object in a method instead of constructor
#### Imposter
- If you need to introduce a new variation into a computation:
  - Introduce new object with same protocol but different implementation
- Interesting insight:
  - Null Object - absence of data can be treated the same as presence of data
  - Composite - collections of data can be treated as a single object
#### Composite
- If you need to implement an object whose behaviour is the composition of the behaviour of a list of other objets:
  - Make it an Imposter for the component objects
#### Collecting Parameter
- If you need to collect the result of an operation that is spread over several objects:
  - Add parameter to the operation in which the results will be collected
#### Singleton
- If you need global variables:
  - Don't do it, rather think about design instead
