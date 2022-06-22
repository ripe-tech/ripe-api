# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

*

### Changed

*

### Fixed

*

## [0.7.0] - 2022-06-22

### Added

* Added `delete_tag` and `deactivate_tag` methods - [ripe-robin-revamp/#363](https://github.com/ripe-tech/ripe-robin-revamp/issues/363)

### Changed

* Move `_query_to_spec`, `_unpack_query`, `_parse_extra_s`, `_tuples_to_parts`, `_parts_to_parts_m` to util API

## [0.6.0] - 2022-06-08

### Added

* Added new `sku`, `invoice_rules` and `transport_rules` endpoints
* Added methods for waybill deletion (void) - [ripe-pulse/#301](https://github.com/ripe-tech/ripe-pulse/issues/301)
* Methods to unset order tracking info - [ripe-pulse/#301](https://github.com/ripe-tech/ripe-pulse/issues/301)
* Entire bulk order module for feature parity with JS SDK
* Pylint config and pylint command to the CI environment
* Added new methods `video` and `video_thumbnail` that return a video and video thumbnail related to a given mode, video name and customization - [ripe-white/#996](https://github.com/ripe-tech/ripe-white/issues/996)
* General order chat methods - [ripe-core/#4702](https://github.com/ripe-tech/ripe-core/issues/4702)
* Order tag methods - [ripe-robin-revamp/#363](https://github.com/ripe-tech/ripe-robin-revamp/issues/363)
* Port `_query_to_spec`, `_unpack_query`, `_parse_extra_s`, `_tuples_to_parts`, `_parts_to_parts_m` from RIPE SDK JS

## [0.5.1] - 2022-02-03

### Added

* Support for the `update_report_url_order` method

## [0.5.0] - 2022-02-03

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
