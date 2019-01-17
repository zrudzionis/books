# Test-Driven Development: By Example by Kent Beck

[Preface](preface.md)

## The Money Example

## The xUnit Example
Example [code](xunit.py)

## Patterns for Test-Driven Development
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
 
 ### Red Bar Patterns
 #### Starter Test
 - Start by testing operation that doesn't do anything
 #### Explanation Test
 - Ask for and give explanations in terms of tests
 #### Learning Test
 - Write tests to learn how 3rd party library works
 - Learning tests protect you from 3rd party library changes
 #### Another Test
 - When new idea arises, add test to the list and go back to the topic
 #### Regression Test
 - When something breaks add test first before fixing it
 #### Break
 - When feeling stuck take a break
 #### Do Over
 - When you are feeling lost, throw away code and start over
 #### Cheap Desk, Nice Chair
 - Better have nice chair than expensive desk
 
 
 
 
 
