cmake_minimum_required(VERSION 3.5)
project(rmf_battery VERSION 0.1.3)

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

# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=address")
# set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fsanitize=address")

include(GNUInstallDirs)

# find dependencies
find_package(rmf_utils REQUIRED)
find_package(rmf_traffic REQUIRED)
find_package(eigen3_cmake_module QUIET)
find_package(Eigen3 REQUIRED)
find_package(ament_cmake_catch2 QUIET)
find_package(ament_cmake_uncrustify QUIET)

# ===== Battery modelling library
file(GLOB_RECURSE core_lib_srcs "src/rmf_battery/*.cpp")
add_library(rmf_battery SHARED
  ${core_lib_srcs}
)

target_link_libraries(rmf_battery
  PUBLIC
    rmf_utils::rmf_utils
    rmf_traffic::rmf_traffic
)

target_include_directories(rmf_battery
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
    ${Eigen3_INCLUDE_DIRS}
)

if(BUILD_TESTING AND ament_cmake_catch2_FOUND AND ament_cmake_uncrustify_FOUND)

  file(GLOB_RECURSE unit_test_srcs "test/*.cpp")

  ament_add_catch2(
    test_rmf_battery test/main.cpp ${unit_test_srcs}
    TIMEOUT 300)
  target_link_libraries(test_rmf_battery
      rmf_battery
  )

  target_include_directories(test_rmf_battery
    PRIVATE
      $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/>
  )

  find_file(uncrustify_config_file
    NAMES "rmf_code_style.cfg"
    PATHS "${rmf_utils_DIR}/../../../share/rmf_utils/")

  ament_uncrustify(
    ARGN include src test
    CONFIG_FILE ${uncrustify_config_file}
    MAX_LINE_LENGTH 80
  )
endif()

# Create cmake config files
include(CMakePackageConfigHelpers)

set(INSTALL_CONFIG_DIR "${CMAKE_INSTALL_LIBDIR}/rmf_battery/cmake")
set(PACKAGE_CONFIG_VERSION_FILE "${CMAKE_CURRENT_BINARY_DIR}/rmf_battery-config-version.cmake")
set(PACKAGE_CONFIG_FILE "${CMAKE_CURRENT_BINARY_DIR}/rmf_battery-config.cmake")

configure_package_config_file(
  "${CMAKE_CURRENT_LIST_DIR}/cmake/rmf_battery-config.cmake.in"
  ${PACKAGE_CONFIG_FILE}
  INSTALL_DESTINATION ${INSTALL_CONFIG_DIR}
)

write_basic_package_version_file(
  ${PACKAGE_CONFIG_VERSION_FILE}
  COMPATIBILITY ExactVersion
)

install(
  TARGETS rmf_battery
  EXPORT  rmf_battery-targets
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(
  DIRECTORY include/
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install(
  TARGETS rmf_battery
  EXPORT  rmf_battery
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(
  FILES
    ${PACKAGE_CONFIG_VERSION_FILE}
    ${PACKAGE_CONFIG_FILE}
  DESTINATION ${INSTALL_CONFIG_DIR}
)

install(
  EXPORT rmf_battery-targets
  FILE rmf_battery-targets.cmake
  NAMESPACE rmf_battery::
  DESTINATION ${INSTALL_CONFIG_DIR}
)

export(
  EXPORT rmf_battery-targets
  FILE ${CMAKE_CURRENT_BINARY_DIR}/rmf_battery-targets.cmake
  NAMESPACE rmf_battery::
)

# Export ament index path
file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/share/ament_index/resource_index/packages/${PROJECT_NAME} "")
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/share/ament_index/resource_index/packages/${PROJECT_NAME} DESTINATION share/ament_index/resource_index/packages)

file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/share/${PROJECT_NAME}/hook/ament_prefix_path.dsv "prepend-non-duplicate;AMENT_PREFIX_PATH;")
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/share/${PROJECT_NAME}/hook/ament_prefix_path.dsv DESTINATION share/${PROJECT_NAME}/hook)
