### Refactoring

#### Reconcile differences
- If you need to unify similarly looking code:
    - Gradually bring them closer
    - Unify them only when they are identical
    - For classes remove child classes only when they are empty   
#### Isolate change
- If you need to change multi-part method or object:
    -  Isolate the part that has to change
#### Migrate data
- If you need to move from one representation to another:
    - Temporary duplicate data
#### Extract method
- If you need to make long and complicated class/method easier to read:
    - Turn small part of it into seprate class/method and use new class/method
#### Inline method
- If you need to simplify control flow that has become too scattered:
    - Replace method invocations with method itself
#### Extract interface
- If you need to use two different types that have similar operations:
    - Create and interface containing the shared operations
#### Move method
- If you need to move method to where it belongs:
    - Move method where it belongs then invoke it
#### Method object
- If you want to represent complicated operation that requires
several parameters and local variables:
    - Create object wrapping method and parameters and invoke 
    it with dedicated method
#### Add parameter
- If you need to add parameter to a method:
    - Add parameter and and fix compiler errors
#### Method parameter to constructor parameter
- If you need move parameter from method to constructor:
    - Add parameter to constructor, replace method parameter 
    with constructor parameter
