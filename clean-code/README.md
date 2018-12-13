# Clean Code: A Handbook of Agile Software Craftsmanship

<details>
  <summary>Functions</summary>
  <p>
    
- Function should communicate its intent
- Function should be small (hardly ever 20 lines long)
- Identation level should not be greater than 1 or 2
- Function should do one thing. It should do it well. It should do it only
- There should't be sections inside function
- Function should contain one level of abstraction
- Switch statements can be tolerated if they appear only once, are used to create polymorphic objects, and are hidden behind inheritance relationship
- Use descriptive function names
- Single parameter functions should return updated value
- There should't be flag parameters
- One, two or three parameters at most
- If more than three parameters needed create objects representing parameters
- Parameter list is the same as single parameter of type list
- Function name can include parameters to provide context ex. assertExpectedEqualsActual instead of assertEqual
- Have no side effects
- Output parameter dependency can be inversed ex. public void appendFooter(StringBuffer report) -> report.appendFooter()
- Function should't contain query and command
- Prefer exceptions to returning error codes
- Try/Catch blocks should be extracted to different functions
- Error Handling is one thing
- Don't repeat yourself
    
  </p>
</details>



<details>
  <summary>Comments</summary>
  <p>

- Good comments:
    - Legal
    - Informative
    - Explanation of intent
    - Clarification
    - Warning of consequences
    - TODO
    - Aplification of importance
    - Javadocs in public APIs
- Bad comments:
    - Mumbling
    - Redundant
    - Misleading
    - Mandated
    - Journal comments
    - Noise comments
    - Position marker comments
    - Closing brace comments
    - Attributions and bylines
    - Commented-out code
    - HTML comments
    - Containing nonlocal information
    - Containing too much information
    - Inobvious connection to code
    - In function headers (short functions don't need them)
    - Javadoc in nonpublic code
- Comments rot faster than code
- Comments should be used to communicate intent
- Don't use comment when you can use function or a variable

  </p>
</details>



<details>
  <summary></summary>
  <p>
  </p>
</details>



