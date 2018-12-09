# Clean Code: A Handbook of Agile Software Craftsmanship

## Meaningful names

- Use intention revealing names
- Avoid disinformation
- Make meaningful distinctions
- Use pronaunceable names
- Use searchable names
- The length of name should correspond to the size of its scope
- Avoid encodings
- Avoid Hungarian notation
- Avoid member prefixes
- Encode implementation rather than interface
- Avoid mental mapping
- Class name should be noun
- Method name should be verb
- Don't be clever or cute
- Be consistent one word per one concept
- Don't use same name for things that have different semantic meaning
- Use solution domain names
- Use problem domain names
- Add meaningful context
- Don't add redundant context

## Functions

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





