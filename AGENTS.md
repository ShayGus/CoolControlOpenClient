# Repository Guidelines

## Project Structure & Module Organization
- `cool_open_client/` hosts the public interface: `cool_automation_client.py` wraps authentication and websocket flows, `hvac_units_factory.py` builds device abstractions, the generated async API lives in `client/`, and shared helpers sit in `utils/`.
- `open_api/CoolAPI-resolved.yaml` is the source schema for regenerating the SDK.
- `script/` contains maintenance utilities (`generate_client.sh`, `build.sh`) that refresh generated code and build distributions.
- `tests/` provides integration-style unittest suites that hit the live service and expect local credential fixtures.
- `swagger_client/` mirrors the raw swagger-codegen output; keep edits out of this tree and stage changes via the scripts above.

## Build, Test, and Development Commands
- `pip install -r requirements.txt` (plus `-r devrequirements.txt` for packaging helpers) prepares the environment.
- `bash script/generate_client.sh` regenerates `cool_open_client/client/` using Dockerized swagger-codegen; ensure Docker is running and network access is available.
- `python -m build` emits wheel and sdist artefacts in `dist/`; run after syncing generated code.
- `python -m unittest discover tests` executes the provided suites; use `pytest tests/test_hvac_units_factory.py -vv` for richer output when diagnosing failures.

## Coding Style & Naming Conventions
- Follow PEP 8: four-space indentation, snake_case for functions and variables, PascalCase for dataclasses and request bodies.
- Keep type hints on async APIs and prefer small, descriptive coroutine names (e.g., `get_dictionary`, `set_operation_mode`).
- Treat files inside `cool_open_client/client/` and `swagger_client/` as generated—extend behaviour in higher-level modules instead of patching generated code.

## Testing Guidelines
- Tests require `token.txt` (and `bad_token.txt`) at the repo root with valid CoolAutomation tokens; never commit these fixtures.
- Mark new integration tests clearly and guard them so they skip gracefully when tokens are missing.
- When possible, stub HTTP calls in unit tests to keep coverage meaningful without relying on real hardware.

## Commit & Pull Request Guidelines
- Keep commit messages concise and action-oriented (`Update dependencies fix bidict`, `Fix API v2 duplicated types`). Reference API versions or related issues when relevant.
- PRs should describe scope, testing performed, and any API schema changes; attach logs or screenshots when altering websocket behaviour.
- Exclude build artefacts (`dist/`, `*.egg-info`, `token.txt`) from commits and verify `python -m build` before requesting reviews.

## Security & Configuration Tips
- Store tokens and environment secrets outside the repository; use `.env`-style files listed in `.gitignore` when scripting locally.
- Review debug logs and websocket traces for device identifiers before sharing them in issues or PR discussions.

## Active Technologies
- Python ≥3.9 + aiohttp, marshmallow (+ dataclass integration), rel, websocket-client, bidict (001-migrate-aiohttp-client)
- N/A (stateless client interacting with Coolemaster API) (001-migrate-aiohttp-client)

## Recent Changes
- 001-migrate-aiohttp-client: Added Python ≥3.9 + aiohttp, marshmallow (+ dataclass integration), rel, websocket-client, bidict
