# Concurrency

- Writing clean concurrent programs is very hard
- Concurrency is decoupling of what gets done from when it gets done
- Myths:
  1. Concurrency always improves performance
  2. Design does not change when writing concurrent programs
  3. Understanding concurrency issues is not important when working with containers
- Concurrency incurs some overhead
- Correct concurrency is complex
- Concurrency bug aren't usually repeatable
- Concurrency often requires a fundamental change in design strategy
- Keep your concurrency-related code separate from other code
- Take data encapsulation to heart; severely limit the access of any data that may be shared
- Attempt to use copies of data
- Attempt to partition data into independent subsets than can be operated on by independent threads, 
possibly in different processors
- Know your library (thread-safe collections and so on)
- Know your execution models
- Learn basic algorithms and understand their solutions
- Avoid using more than one method on a shared object. Some solutions:
  1. Client-Based Locking
  2. Server-Based Locking
  3. Adpted Server
- Keep synchronized sections as small as possible
- Correct shut-down is hard
- Think about shut-down early and get it working early
- Write tests that have the potential to expose problems and then run them frequently with different load and configurations.
If tests ever fail, track down the failure. Don't ignore a failure just because the tests pass on a subsequent run
- Testing threaded code tips:
  - Treat spurious failures as condidate threading issues
  - Get your nonthreaded code working first
  - Make your threaded code pluggable
  - Make your threaded code tunable
  - Run with more threads than processors
  - Run on different platforms
  - Instrument your code to try and force failures

