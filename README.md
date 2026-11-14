# Copilot Skills Lab

[![CI](https://github.com/2500031290/skills-copilot-codespaces-vscode/actions/workflows/ci.yml/badge.svg)](https://github.com/2500031290/skills-copilot-codespaces-vscode/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A beginner-friendly playground for experimenting with **GitHub Copilot**, **GitHub Codespaces**, and **Visual Studio Code**. The examples are intentionally small so you can read, run, change, and improve them with Copilot.

## What is included?

- A Python greeting application with a unit test
- A Java console application
- A JavaScript console application
- Reusable [Copilot prompt examples](docs/copilot-prompts.md)
- A documented [project structure](docs/project-structure.md)
- A ready-to-use Codespaces and VS Code setup
- GitHub Actions checks for all three languages

## Quick start

### GitHub Codespaces (recommended)

1. Select **Code** → **Codespaces** → **Create codespace on main**.
2. Wait for the dev container to finish setting up.
3. Open a file under `python/`, `java/`, or `javascript/`.
4. Ask Copilot to explain the code, suggest an improvement, or write a test.

### Local development

Install Python 3.11+, Java 17+, Node.js 20+, and VS Code. Then run the examples:

```bash
python python/hello_copilot/main.py
python -m unittest discover -s python -p 'test_*.py'

javac -d /tmp/copilot-java java/src/Main.java
java -cp /tmp/copilot-java Main

node javascript/hello-copilot/index.js
```

## A simple Copilot learning loop

1. **Understand:** ask Copilot to explain an example without changing it.
2. **Plan:** describe a small feature and ask for an implementation plan.
3. **Implement:** accept only suggestions you understand.
4. **Verify:** ask Copilot for tests, then run the checks yourself.
5. **Reflect:** update the code or documentation with what you learned.

See the [prompt examples](docs/copilot-prompts.md) for ideas and the [structure guide](docs/project-structure.md) for where to put new work.

## Contributing

Small improvements are welcome: fix a typo, add an exercise, improve an example, or document a new Copilot workflow. Keep examples dependency-free where possible and make sure `python -m unittest discover -s python -p 'test_*.py'`, `node --check javascript/hello-copilot/index.js`, and the Java compile command continue to pass.

## License

This project is available under the [MIT License](LICENSE).
