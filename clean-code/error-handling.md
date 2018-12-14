# Error handling

- Extract try-catch to different functions (error handling is one thing)
- Use exceptions rather than return codes
- Start with try-catch-finally block If code can throw exceptions
- Write tests that force exceptions
- Use unchecked exceptions. Checked exceptions break open/closed principle.
- Provide context with exceptions
- Define exceptions in terms of a caller's needs (how they are caught) i.e.: throw one exception instead of many different ones
- Wrap third-party exceptions
- Define normal flow
- Use [Special Case Pattern](https://martinfowler.com/eaaCatalog/specialCase.html) (Fowler) to handle special cases
- Don't return null
- Don't pass null
