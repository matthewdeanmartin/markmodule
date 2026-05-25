ifeq ($(origin VIRTUAL_ENV),undefined)
    VENV := uv run
else
    VENV :=
endif

uv.lock: pyproject.toml
	@echo "Installing dependencies"
	@pipenv install --dev


# tests can't be expected to pass if dependencies aren't installed.
# tests are often slow and linting is fast, so run tests on linted code.
test: pylint bandit uv.lock
	@echo "Running unit tests"
	# $(VENV) pytest markmodule --doctest-modules
	# $(VENV) python -m unittest discover
	$(VENV) py.test test --cov=markmodule --cov-report=html --cov-fail-under 50


isort:  
	@echo "Formatting imports"
	$(VENV) isort markmodule markmodule

black:  isort 
	@echo "Formatting code"
	$(VENV) black . --exclude .virtualenv

pre-commit:  isort black
	@echo "Pre-commit checks"
	$(VENV) pre-commit run --all-files

bandit:  
	@echo "Security checks"
	$(VENV)  bandit .

.PHONY: pylint
pylint:  isort black 
	@echo "Linting with pylint"
	$(VENV) pylint markmodule --fail-under 9.9
	@touch pylint

mypy:  
	@echo "mypy"
	@echo "temporarily disabling mypy"
	# $(VENV)  mypy markmodule

.PHONY: mypy
mypy: mypy


check: test pylint bandit mypy

.PHONY: publish
publish: check
	rm -rf dist && $(VENV) hatch build


# ── Dogfooding targets (independent, not wired into check) ───────────────────

.PHONY: version-check
version-check:
	@uv run jiggle_version check

.PHONY: dev-status
dev-status:
	@uv run troml-dev-status validate .

.PHONY: prerelease-check
prerelease-check: version-check dev-status
	@echo "Pre-release checks passed."

.PHONY: dont-be-lazy
dont-be-lazy:
	@uv run dont_be_lazy --root . --no-color summary
	@uv run dont_be_lazy --root . --no-color scan markmodule --no-config-suppressions || true

.PHONY: pydoc-docs
pydoc-docs:
	@uv run pydoc_fork markmodule -o ./pydoc/
