### Testing Patterns
#### Child Test
- If test case is too big:
  - Write a smaller test case that represents the broken part of the bigger test
  - Get the smaller test case running
  - Reintroduce the larger test case
#### Mock Object
- If test relies on an expensive or complicated resource:
  - Create a fake version of resource that answers constants
#### Self Shunt
- If you need to test that one object communicates correctly with other object:
  - Have the object under test communicate with the test case instead of with the object it expects
#### Log String
- If you need to check that the sequence in which methods are called is correct:
  - Have a log string and append to the string when method is called
#### Crash Test Dummy
- If you need to test error handling:
  - Have dummy object that throws exception
#### Broken test
- If you need to leave programming session when you are programming alone:
  - Leave the last test broken
#### Clean Check-in
- If you need to leave programming session when you are programming in team:
  - Leave all of the tests passing
