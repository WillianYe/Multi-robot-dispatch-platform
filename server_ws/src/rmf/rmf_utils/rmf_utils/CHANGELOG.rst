^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package rmf_utils
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.4.0 (2022-02-14)
------------------
* Add a class to help with limiting rates of events (`#18 <https://github.com/open-rmf/rmf_utils/pull/18>)

1.3.0 (2020-01-19)
------------------
* Adding missing string include for test, only shows up when building with clang (`#9 <https://github.com/open-rmf/rmf_utils/issues/9>`_)
* Add quality declaration documents (`#1 <https://github.com/open-rmf/rmf_utils/issues/1>`_)
* Changed package requirement to QUIET to allow use in non-ROS 2 packages (`#6 <https://github.com/open-rmf/rmf_utils/issues/6>`_)
* install rmf_code_style.cfg in rmf_utils_DIR (`#4 <https://github.com/open-rmf/rmf_utils/issues/4>`_)
* change to catch2 test, uncrustify everything (`#3 <https://github.com/open-rmf/rmf_utils/issues/3>`_)
* Contributors: Aaron Chong, Geoffrey Biggs, ddengster

1.1.0 (2020-09-24)
------------------
* Replace rmf_utils::optional with std::optional (`#177 <https://github.com/osrf/rmf_core/issues/177>`_)
* Foxy Support (`#133 <https://github.com/osrf/rmf_core/issues/133>`_)
* Remove ros2 dependency (`#142 <https://github.com/osrf/rmf_core/issues/142>`_)
* Contributors: Aaron Chong, Grey, Yadu

1.0.0 (2020-06-23)
------------------
* Basic utilities for use in the `rmf_core` packages
    * `impl_ptr` - A smart pointer that helps implement a PIMPL-pattern
    * `clone_ptr` - A smart pointer with cloning semantics (copying the pointer instance will clone the underlying object)
    * `optional` - A stopgap measure to get the features of `std::optional` before C++17 is available
    * `Modular` - A class for comparing integral version numbers that may wrap around due to integer overflow
* Contributors: Grey, Luca Della Vedova, Marco A. Gutiérrez, Michael X. Grey, Morgan Quigley, Yadu, Yadunund
