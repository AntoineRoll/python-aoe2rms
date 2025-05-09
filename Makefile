check-format:
	ruff format tests/ aoe2rms/ --check

check-lint:
	ruff check tests/ aoe2rms/

checkers: check-format check-lint

formatters:
	ruff format tests/ aoe2rms/
	ruff check tests/ aoe2rms/ --fix
