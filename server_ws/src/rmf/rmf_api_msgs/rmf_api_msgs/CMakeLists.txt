cmake_minimum_required(VERSION 3.5.0)

project(rmf_api_msgs VERSION 0.1)

set(CMAKE_EXPORT_COMPILE_COMMANDS on)

# Default to C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

if(NOT CMAKE_BUILD_TYPE)
  # Use the Release build type by default if the user has not specified one
  set(CMAKE_BUILD_TYPE Release)
endif()

include(GNUInstallDirs)

find_package(ament_cmake REQUIRED)
find_package(nlohmann_json REQUIRED)

include(cmake/rmf_api_generate_schema_headers.cmake)
set(RMF_API_GENERATE_SCHEMA_TEMPLATE ${CMAKE_CURRENT_LIST_DIR}/cmake/schemas_template.hpp.in)
rmf_api_generate_schema_headers(
  PACKAGE rmf_api_msgs
  SCHEMAS_DIR ${CMAKE_CURRENT_LIST_DIR}/schemas
)

add_library(rmf_api_msgs INTERFACE)

target_include_directories(
  rmf_api_msgs
  INTERFACE
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

include(CMakePackageConfigHelpers)

set(INSTALL_CONFIG_DIR "${CMAKE_INSTALL_LIBDIR}/rmf_api_msgs/cmake")

set(PACKAGE_CONFIG_FILE "${CMAKE_CURRENT_BINARY_DIR}/rmf_api_msgs-config.cmake")
configure_package_config_file(
  "${CMAKE_CURRENT_LIST_DIR}/cmake/rmf_api_msgs-config.cmake.in"
  ${PACKAGE_CONFIG_FILE}
  INSTALL_DESTINATION ${INSTALL_CONFIG_DIR}
)

set(PACKAGE_CONFIG_VERSION_FILE "${CMAKE_CURRENT_BINARY_DIR}/rmf_api_msgs-config-version.cmake")
write_basic_package_version_file(
  ${PACKAGE_CONFIG_VERSION_FILE}
  COMPATIBILITY ExactVersion
)

install(
  TARGETS rmf_api_msgs
  EXPORT rmf_api_msgs-targets
)

install(
  FILES
    ${PACKAGE_CONFIG_FILE}
    ${PACKAGE_CONFIG_VERSION_FILE}
    ${CMAKE_CURRENT_LIST_DIR}/cmake/rmf_api_generate_schema_headers.cmake
    ${CMAKE_CURRENT_LIST_DIR}/cmake/schemas_template.hpp.in
  DESTINATION ${INSTALL_CONFIG_DIR}
)

install(
  EXPORT rmf_api_msgs-targets
  FILE rmf_api_msgs-targets.cmake
  NAMESPACE rmf_api_msgs::
  DESTINATION ${INSTALL_CONFIG_DIR}
)

install(
  DIRECTORY schemas
  DESTINATION ${CMAKE_INSTALL_DATADIR}
)

# Generate python schemas mode whenever colcon is triggered
message(" Generating schema as py mods")
ADD_CUSTOM_TARGET(
  py_schemas_gen ALL
  COMMAND eval "python3 generate_py_schemas.py \
    --schemas_dir ${CMAKE_CURRENT_LIST_DIR}/schemas \
    --output_file ${CMAKE_CURRENT_LIST_DIR}/rmf_api_msgs/schemas.py"
  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/scripts)

# Generate pydantic models according to schemas
# If datamodel-codegen not avail, then skip this proccess along with warning
find_program(PY_MODELGEN_AVAIL datamodel-codegen)
if(PY_MODELGEN_AVAIL)
  message(" Generating py models with 'datamodel-codegen'")
  ADD_CUSTOM_TARGET(
    py_models_gen ALL
    COMMAND eval "datamodel-codegen \
      --disable-timestamp \
      --input-file-type jsonschema  \
      --input ${CMAKE_CURRENT_LIST_DIR}/schemas \
      --output ${CMAKE_CURRENT_LIST_DIR}/rmf_api_msgs/models"
    WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/scripts)
else()
  message(
    WARNING "Not able to generate py models since 'datamodel-codegen' is not available")
endif()

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# # Install Python executables and share template
install(PROGRAMS
  scripts/check_sample.py
  scripts/schemas_template.jinja2
  scripts/generate_py_schemas.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
