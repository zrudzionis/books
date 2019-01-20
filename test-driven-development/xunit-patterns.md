### xUnit Patterns
#### Assertion
- If you need to check that tests worked correctly:
  - Write boolean expression that automate your judgment about whether the code worked
#### Fixture
- If you need to create common objects needed by several tests:
  - Convert local variables into instance variables
  - Override `setUp()` and initialize those variables
 - Usually one test class uses one fixture
#### External Fixture
- If you need to release external resources in the fixture:
  - Override `tearDown()` and release the resources
#### Test Method
- If you need to represent test:
  - Have a method that name begins with `test`
- Tests that require different fixture should go to different class
- Test method should be easy to read
#### Exception Test
- If you need to test expected exception:
  - Catch expected exception and ignore them, failing only if the exception isn't thrown
#### All Tests
- If you need to run all the tests:
  - Make suite of all the suites and run that suite
