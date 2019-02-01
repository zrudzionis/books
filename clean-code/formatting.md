# Formatting

- Formatting should be done continuously
- Files should be below 500 lines
- Files should be read top to bottom from high level to low level details (including file name)
- Different concepts should be separated by empty lines i.e.: build-in imports, third-party package imports, our code imports
- Lines of code that are tightly related should appear vertically dense
- Closely related concepts should be kept vertically close
- Variables should be declared close to their usage
- Instance variable should be declared at the top of the class
- If one function call another they should be vertically close
- The greater the conceptual affinity the closer to each other code should be
- Function caller should be above callee
- Line length should be not greater than 80
- In horizontal formatting use white space to associate things that are strongly related and dissociate 
things that are more weakly related i.e.: 2*3 + 1 or foo(1, 2) over foo (1,2)
- Horizontal alignment not recommended
- One new identation level per one new block
- Make dummy scopes visible i.e.: indented while(f.read() != -1) { } over while(f.read() != -1);
- Make sure your team agrees on formatting convention
