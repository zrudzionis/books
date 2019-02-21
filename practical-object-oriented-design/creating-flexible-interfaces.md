## Creating Flexible Interfaces

### Understanding Interfaces

### Defining Interfaces
#### Public Interfaces
#### Private Interfaces
#### Responsibilities, Dependencies, and Interfaces
* Depend on class methods that are less likely 
to change
* Depend on public methods rather than on private
### Finding the Public Interface
#### An Example Application: Bicycle Touring Company
#### Constructing an Intention
* Form an intention about the objects and 
the messages needed to satisfy use case
#### Using Sequence Diagrams
* Use sequence diagrams to discover design
* Focus more on messages rather than on objects
#### Asking for "What" Instead of Telling "How"
* Delegate responsibilities that do not belong in the class
#### Seeking context independence
The things class knows about other objects makes up its context. 
The less context it has the better it is.
* Have as little context as possible
#### Trusting Other Objects
#### Using Messages to Discover Objects
#### Creating a Message Based Application

### Writing Code That Puts Its Best (Inter)Face Forward
* Create interfaces intentionally
#### Create Explicit Interfaces
* Methods in the public interface should:
    * Be explicitly identified as such
    * Be more about what than how
    * Have names that, insofar as you can anticipate, will not change
    * Take a kwargs as an options parameter
#### Honor the Public Interfaces of Others
* Avoid depending on private methods
#### Exercise Caution When Depending on Private Interfaces
* If you have to depend on private interface isolate it
#### Minimize Context

### The Law of Demeter
#### Defining Demeter
* Do not use "train-wrecks" like customer.bicycle.wheel.rotate
#### Consequences of Violations
Law of Demeter violation cost (lowest to highest):
* Using stable attributes
* Getting attribute of non-stable object
* Sending a message to non-stable object
#### Avoid Violation
* Avoid hiding violation
#### Listening to Demeter

### Summary
