# T1W8 - Saturday

## Virtual Environments (VENV)

They help create isolated environments for your projects, ensuring each project has its own dependencies.

## Testing

Allows us to confirm whether the application works as intended or not.
Helps catch bugs early and ensure that your code behaves smoothly.

### Types of Testing

Manual vs Automated
    - Manual
        - When a person manually performs tasks, based on events.
    - Automated
        - Programmed tests, also called scripts, to automatically perform tasks without human involvement.

- Unit Testing
    - Testing specific components / functions / methods.

- Integration Testing
    - Testing the entire application.
    - Testing the compatibility with other modules / packages.

- Chaos Testing
    - Making a program break on purpose by disabling a function or feature to see how errors are handled.

- Stress Testing
    - Testing in high volumes of data / inputs (depending on use-case)

- E2E Testing
    - Testing done towards the end of the project, when its almost complete. To ensure things work as expected.

> NOTE: Great idea to organise your directory structure for maintenance and easy access.

### pytest

- Powerful and user friendly testing framework
- Simple yet powerful
- pytest follows the principle of 'assert'-ing that things are true in order for a test to pass.
- For a test to pass, all assertions must be true.

#### Reading test output

- `.` means pass
- `F` means fail
- `E` means error
- `X` means skipped

#### Exceptions
- Used to check what happens when things go wrong.
- How your program is handled when things go wrong.

#### Parameterized tests

- Test cases that can be run with different inputs.
- Can be used to test different combinations of inputs.
- Make sure you initialise the packages to use them in different folders.

#### Fixtures

- Arrange and prepare data before running tests.
- Reusable code
- Fixture Scopes: Function, Class, Module, Package, Session (When to destroy the fixture)

## File Handling

- Read and write data from and to files
- Before performing any operatin its important to open the file, and close when you're done.
- Operations:
    - Open
    - Read
    - Write
    - Close
- 'with' statement: