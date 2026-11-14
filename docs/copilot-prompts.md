# Copilot prompt examples

Good prompts provide context, constraints, and a way to verify the result. Try these in an example file, then inspect the suggestion before accepting it.

## Understand existing code

```text
Explain this function line by line for someone new to Python. Mention its inputs,
return value, edge cases, and one question I should investigate.
```

## Plan a change

```text
I want to add input validation without adding dependencies. Give me a three-step
plan, identify the files to change, and list tests for empty and invalid input.
Do not write code yet.
```

## Generate a test

```text
Write focused unit tests for the public behavior of this function. Include the
normal case, an empty input, and one invalid input. Use the testing style already
present in this repository.
```

## Review safely

```text
Review my uncommitted changes for correctness, readability, and security. Do not
rewrite the code. Report findings by severity and include a minimal fix for each.
```

## Learn from an error

```text
This command failed with the error below. Explain the likely cause, suggest two
diagnostic steps, and only then propose the smallest fix:

[paste the command and error here]
```

Never paste passwords, API keys, tokens, or private source code into a prompt.
