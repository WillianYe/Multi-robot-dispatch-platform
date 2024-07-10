cmake_minimum_required(VERSION 3.5)
project(pybind11_json_vendor)

find_package(ament_cmake REQUIRED)
find_package(nlohmann_json REQUIRED)

option(FORCE_BUILD_VENDOR_PKG
  "Build pybind11_json from source, even if system-install package is available"
  OFF
)

if(NOT FORCE_BUILD_VENDOR_PKG)
  find_package(pybind11_json QUIET)
endif()


if(NOT pybind11_json_FOUND)
  find_package(pybind11_vendor REQUIRED)
  find_package(pybind11 REQUIRED)

  set(setup_install_dir "${CMAKE_CURRENT_BINARY_DIR}/pybind11_json")

  include(ExternalProject)
  set(pybind11_json_version 0fbbe3bbb27bd07a5ec7d71cbb1f17eaf4d37702)
  ExternalProject_Add(pybind11_json-${pybind11_json_version}
    GIT_REPOSITORY https://github.com/pybind/pybind11_json.git
    GIT_TAG ${pybind11_json_version}
    GIT_CONFIG advice.detachedHead=false
    # Suppress git update due to https://gitlab.kitware.com/cmake/cmake/-/issues/16419
    UPDATE_COMMAND ""
    CMAKE_ARGS
      -DCMAKE_INSTALL_PREFIX=${setup_install_dir}
      -DBUILD_SHARED_LIBS=true
      -Dpybind11_DIR=${pybind11_DIR}
    INSTALL_DIR ${setup_install_dir}
  )  

  install(
    DIRECTORY ${setup_install_dir}/
    DESTINATION ${CMAKE_INSTALL_PREFIX}
    USE_SOURCE_PERMISSIONS
  )
endif()

ament_export_dependencies(pybind11_json)

ament_package()

