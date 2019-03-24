## Combining Objects with Composition

### Composing a Bicycle of Parts
#### Updating the Bicycle Class
#### Creating a Parts Hierarchy
### Composing the Parts Object
#### Creating a Part
#### Making the Parts Object More Like an Array
### Manufacturing Parts
#### Creating the PartsFactory
* Use Factories to isolate dependency on class name
#### Leveraging the PartsFactory
### The Composed Bicycle
Composition in stricter definition means that contained 
object has no life of itself. Aggregation means that 
contained object have life of their own. Example 
relationships university - departments 
composition but university - professors 
aggregation. 
### Deciding Between Inheritance and Composition
"Composition allows objects to have structural 
independence, but at the cost of explicit 
message delegation".
* Prefer composition over inheritance
#### Accepting the Consequences of Inheritance
Low cost of change for good hierarchy.
High cost of change for flawed hierarchy.
#### Accepting the Consequences of Composition
High tolerance for change.
No automatic message delegation. Harder to understand the whole.
#### Choosing Relationships
* Use inheritance for is-a relationship
* Use duck types for behaves-like-a relationship
* Use composition for has-a relationship
### Summary
