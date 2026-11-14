# Project structure

```text
.
├── .devcontainer/       # GitHub Codespaces development container
├── .github/workflows/   # Automated checks
├── .vscode/             # Recommended editor extensions
├── docs/                # Learning and contribution documentation
├── java/src/             # Java console example
├── javascript/           # JavaScript console example
├── python/               # Python example and tests
├── LICENSE
└── README.md
```

Keep each example small and runnable without external services. Add language-specific tests beside the example they exercise, and put cross-project guidance in `docs/`.

## Adding an exercise

1. Create a clearly named folder under the relevant language directory.
2. Add a short `README.md` describing the goal and how to run it.
3. Include a runnable entry point and a focused test when practical.
4. Update the root README if the exercise changes the learning path.
5. Run the commands in the root README before opening a pull request.
