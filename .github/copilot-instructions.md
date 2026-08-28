
# Copilot Instructions

## Project Context

This is a small Sudoku game in `starter` built with Flask, vanilla JavaScript, and CSS.

- `app.py`: Flask application and HTTP routes.
- `sudoku_logic.py`: Sudoku board generation and validation logic.
- `templates/index.html`: Page structure and accessible controls.
- `static/main.js`: Board rendering and browser interaction.
- `static/styles.css`: Responsive visual styling.
- `requirements.txt`: Python dependencies.

## Development Guidelines

- Write clear, original, maintainable code. Do not copy external implementations; understand the required behavior and implement it in a style consistent with this project.
- Support Python 3.14 and current stable Flask practices.
- Keep responsibilities separated:
  - Sudoku generation, solving, validation, difficulty rules, and uniqueness checks belong in reusable Sudoku logic components.
  - Flask routes should handle HTTP concerns, input parsing, response formatting, and errors.
  - Frontend behavior belongs in focused vanilla JavaScript components or functions.
  - Styling belongs in maintainable CSS with reusable custom properties and selectors.
- Preserve existing working behavior during refactoring. Make focused changes and avoid unrelated rewrites.
- Use type hints, descriptive names, short docstrings for public or non-obvious functions, and consistent error handling.
- Add comments only when the logic is not obvious; do not narrate straightforward code.
- Generate only valid, uniquely solvable 9x9 Sudoku puzzles. Do not treat a target clue count alone as proof of difficulty or uniqueness.
- Implement distinct Easy, Medium, and Hard difficulty levels with documented, testable generation rules.
- Prefer the Python standard library, vanilla JavaScript, and CSS. Add a dependency only when it is genuinely necessary and document the reason.
- Use `pytest` for backend tests. Cover puzzle validity, unique solutions, difficulty behavior, malformed input, missing game state, boundary values, and other important edge cases.
- Keep the UI responsive for desktop and mobile, and support keyboard navigation, semantic structure, visible focus states, accessible labels and status messages, sufficient color contrast, light mode, and dark mode.
- Never add secrets, credentials, or sensitive data to source code. Avoid unnecessary dependencies, placeholder implementations, speculative features, and unrelated changes.
- Validate API input before indexing or comparing boards. Return predictable JSON responses and appropriate HTTP status codes for invalid requests and server errors.
- Explain significant suggestions before proposing or applying them, including the problem addressed, the relevant tradeoffs, and how the change preserves existing behavior. Keep explanations specific enough for review and informed acceptance.
- When adding or changing behavior, update focused tests and relevant documentation rather than relying only on manual browser testing.