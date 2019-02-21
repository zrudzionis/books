## Managing Dependencies

### Understanding Dependencies
#### Recognizing Dependencies
Dependency exists if object knows:
* Name of another class
* Name of message that does not 
belong to itself
* The arguments that a message requires
* The order of those arguments
#### Coupling Between Objects (CBO)
#### Other Dependencies

### Writing Loosely Coupled Code
#### Inject Dependencies
Suppose that you are creating instance of 
object and then sending message to it. 
You don't really care who does the job you 
just need the job done. Therefore author says:
"It is not the class of object that's important, 
it's the message you plan to send to it."
* Use Dependency Injection
#### Isolate Dependencies
* Isolate dependencies
* Isolate instance creation
* Isolate vulnerable external messages
#### Remove Argument-Order Dependencies
* Use keyword arguments instead of positional ones
* Explicitly define defaults
* Use wrapping method to isolate external dependencies

### Managing Dependency Direction
#### Reversing Dependencies
* Reverse direction of dependencies whenever needed
#### Choosing Dependency Direction
* Depend on more stable classes

Stability can be identified:
* Some classes are more likely to have changes 
in requirements
* Concrete classes are more likely to change 
than abstract classes
* Changing a class that has many dependants 
will have a widespread consequences

Usually code stability ladder looks like:
1. Built-in libraries
2. Frameworks
3. Your code

Statically typed languages explicitly define interfaces. 
Dynamically typed languages define interfaces implicitly 
and call this "duck typing".

* Avoid dependant-laden classes
* Depend on classes that change less often than you do

### Summary
