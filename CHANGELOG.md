# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

* Added methods for waybill deletion (void) - [ripe-pulse/#301](https://github.com/ripe-tech/ripe-pulse/issues/301)
* Methods to unset order tracking info - [ripe-pulse/#301](https://github.com/ripe-tech/ripe-pulse/issues/301)
* Entire bulk order module for feature parity with JS SDK
* Pylint config and pylint command to the CI environment

### Changed

*

### Fixed

*

## [0.5.1] - 2021-02-03

### Added

* Support for the `update_report_url_order` method

## [0.5.0] - 2021-02-03

### Added

* Add missing RIPE API endpoints to be consistent with RIPE SDK - [#31](https://github.com/ripe-tech/ripe-api/pull/31)
* Add `Invoice Rule` API methods - [peri-invoicing/#3](https://github.com/ripe-tech/peri-invoicing/issues/3)

### Fixed

* Call to report URL, which was not working as expected

## [0.4.0] - 2021-11-22

### Added

* Add methods `produce_order`, `ready_order` and `send_order` to allow order state change - [Related to ripe-bridge/#4584](https://github.com/ripe-tech/ripe-bridge/issues/148)
* Add `strict` para to methods `produce_order`, `ready_order` and `send_order` - [Related to ripe-bridge/#4584](https://github.com/ripe-tech/ripe-bridge/issues/148)
* Add `locale_to_native` and `locale_to_native_b` methods - [#4638](https://github.com/ripe-tech/ripe-core/issues/4638)

## [0.3.0] - 2021-08-26

### Added

* Support for saving login data

## [0.2.0] - 2021-06-16

### Added

* Add support for `logic_method_brand` method
* Add support for `logic_method_exists_brand` method
