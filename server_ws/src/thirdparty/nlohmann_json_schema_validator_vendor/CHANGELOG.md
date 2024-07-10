## Changelog for package nlohmann_json_schema_validator_vendor

0.2.4 (2022-11-28)
------------------
* Added patch command and file to try to fix the version problem.
* Contributors: Esteban Martinena

0.2.3 (2022-11-15)
------------------
* Fixed external project commit reference to build with json-dev 3.6

0.2.2 (2022-11-14)
------------------
* Vendoring a version that not depends on json-dev > 3.6
  [https://github.com/open-rmf/rmf/issues/265#validator](https://github.com/open-rmf/rmf/issues/265#validator)
* Contributors: Esteban Martinena

0.2.1 (2022-10-09)
------------------
* Remove export of vendored project. [#10](https://github.com/open-rmf/nlohmann_json_schema_validator_vendor/issues/10)
* Add buildtool dependency on git. [#10](https://github.com/open-rmf/nlohmann_json_schema_validator_vendor/issues/10)
* Do not export dependencies on the vendored project. [#10](https://github.com/open-rmf/nlohmann_json_schema_validator_vendor/issues/10)
* Contributors: Steven! Ragnarök

0.2.0 (2022-10-07)
------------------
* Removed unused `ExternalProject_Add` arguments. [#9](https://github.com/open-rmf/nlohmann_json_schema_validator_vendor/pull/9)
* Pin to specific commit of vendored project. [#9](https://github.com/open-rmf/nlohmann_json_schema_validator_vendor/pull/9)
* Remove unneeded `BUILD_ALWAYS` argument to `ExternalProject_Add`. [#9](https://github.com/open-rmf/nlohmann_json_schema_validator_vendor/pull/9)
* Fix formatting and update build options for changes in vendored project. [#9](https://github.com/open-rmf/nlohmann_json_schema_validator_vendor/pull/9)
* Remove CMake patch which is no longer required for relocatability. [#9](https://github.com/open-rmf/nlohmann_json_schema_validator_vendor/pull/9)

0.1.3 (2022-10-05)
------------------
Fixed system install

0.1.2 (2022-10-05)
------------------
* Added ament_cmake_libraries dependence

0.1.1 (2022-10-04)
------------------
* Change install behavior (`#7 <https://github.com/open-rmf/nlohmann_json_schema_validator_vendor/issues/7>`_)
* Adding vendored package license to package.xml (`#6 <https://github.com/open-rmf/nlohmann_json_schema_validator_vendor/issues/6>`_)
* Contributors: Grey, Marco A. Gutiérrez

0.1.0 (2022-02-14)
------------------
* Initial version
