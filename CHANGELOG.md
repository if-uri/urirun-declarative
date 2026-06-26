# Changelog

All notable changes to `urirun-declarative` are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] - 2026-06-26

### Added
- Initial release. Define connector routes declaratively (a spec dict → urirun URI bindings, no
  Python handler code) — extracted from `urirun.connectors.declarative` as a standalone,
  dependency-free package.
- Back-compat: the old import path `urirun.connectors.declarative` keeps working via a `sys.modules`
  re-export shim. Connectors that build bindings from a spec (e.g. urirun-connector-ksef) depend on
  this package directly.
