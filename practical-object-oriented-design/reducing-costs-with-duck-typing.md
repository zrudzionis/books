## Reducing Costs with Duck Typing

### Understanding Duck Typing
"It's not what an object is that matters, it's what it does".
Having a class name is having additional knowledge you don't 
actually need. Class name is used not by you but by compiler 
and IDE. Having class name creates additional coupling to 
specific object type. Knowing about a class might also give you 
additional knowledge that you don't need. If class implement two 
public interfaces and you use only one then method is coupled 
to one more public method.
* Recognize across-class types
* Construct public interfaces intentionally and diligently
#### Overlooking the Duck
#### Compounding the Problem
Sending class based messages introduces 
dependencies on:
* Class names
* Names of messages
* Arguments that those messages require
#### Finding the Duck
* To find duck ask client what needs to 
be done ignoring how it should be done
#### Consequences of Duck Typing
Having duck types:
* Design becomes more flexible
* Becomes harder to understand code
### Writing Code That Relies on Ducks
#### Recognizing Hidden Ducks
Indication that ducks could be used:
* Case statements that switch on class
* king_of? and is_a?
* responds_to?
#### Placing Trust in Your Ducks
* When you see client that might benefit from 
use of duck types create duck types in terms 
of client needs
#### Documenting Duck Types
* Write tests to document duck types
#### Sharing Code Between Ducks
* To share code between ducks use Ruby modules if possible
#### Choosing Your Ducks Wisely
* Purpose of design is to reduce costs
* Use ducks to reduce costs
* If you depend on stable classes then it 
might make sense to not introduce duck typing
### Conquering a Fear of Duck Typing
#### Subverting Duck Types with Static Typing
#### Static versus Dynamic Typing
Static typing proponents claim:
* The compiler reveals type errors at compile time
* Visible type information serves as documentation
* Compiled code is optimized to run quickly
#### Embracing Dynamic Typing
* The compiler reveals type errors at compile time
    * The compiler will save you from accidental type errors
        * Not true for any language that allows type casting 
        or null
    * Without compiler these errors will occur
        * They just don't happen in practice. 
        Errors that happen most times are related 
        to using null that are not preventable in 
        statically types languages
* Visible type information serves as documentation
    * You can't understand code without type information
        * That just don't happen in practice. Usually 
        you care what objects are doing instead of 
        who they are
* Compiled code is optimized to run quickly
    * In some cases this is true    
### Summary
