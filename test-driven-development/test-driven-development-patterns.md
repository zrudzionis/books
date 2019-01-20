### Test-Driven Development Patterns

#### Isolated Test
Test should be:
- Repeatable
- Fast
- Independent

#### Test List
- Before you begin write a list of all test you know you will have to write:
  1. Add to list examples of operations that you know you need to implement
  2. Add null version operation that don't already exist
  3. Add refactoring tasks
- Writing all the tests first is a bad idea

#### Test First

#### Assert First
  - Start writing test from assert

#### Test Data
  - Never use the same constant to mean more than one thing
  - Realistic data is useful for:
    - Testing real-time systems using traces of external events
    - Comparing output of the current systems with the new system
 
 #### Evident Data
 - Make expected and actuals results relationship apparent
