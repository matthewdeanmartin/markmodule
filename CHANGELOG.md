# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Begin implementation of executing .md files via Python's encoding feature (not yet functional)

## [0.3.0] - 2023-06-18

### Added

- Markdown module importer (md_importer) allowing Python to import .md files as modules
- String-based module loader (string_loader) for dynamic module creation
- Stub file generator (generate_pyi) for producing .pyi type hint files from modules

## [0.2.0] - 2023-06-18

### Changed

- Documentation updates

## [0.1.0] - 2023-06-18

### Added

- Basic idea with basics in place

[Unreleased]: https://github.com/matthewdeanmartin/markmodule/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/matthewdeanmartin/markmodule/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/matthewdeanmartin/markmodule/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/matthewdeanmartin/markmodule/releases/tag/v0.1.0
