# Objects and data structures

- Procedural (code using data structures) makes it easy to add new functions without changing the existing data structures
- OO code makes it easy to add new classes without changing existing functions
- Procedural code makes it hard to add new data structures because all the functions must change
- OO code makes it hard to add new functions because all the classes must change
- The Law of Demeter says that method f of class C should only call methods of:
  - C
  - An object created by f
  - An object passed as an argument to f
  - An object held in an instance variable of C
 - The Law of Demeter can be satified by hidding structure i.e.: a.b().c() -> a.d() where d = this.b().c()
 
