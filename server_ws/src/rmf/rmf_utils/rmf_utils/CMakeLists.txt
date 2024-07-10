cmake_minimum_required(VERSION 3.5.0)

project(rmf_utils VERSION 1.4.0)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

include(GNUInstallDirs)

file(GLOB_RECURSE lib_srcs "src/rmf_utils/*.cpp")
add_library(rmf_utils SHARED ${lib_srcs})

target_include_directories(rmf_utils
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

target_compile_features(rmf_utils INTERFACE cxx_std_17)

# Create cmake config files
include(CMakePackageConfigHelpers)

set(INSTALL_CONFIG_DIR "${CMAKE_INSTALL_LIBDIR}/rmf_utils/cmake")
set(PACKAGE_CONFIG_VERSION_FILE "${CMAKE_CURRENT_BINARY_DIR}/rmf_utils-config-version.cmake")
set(PACKAGE_CONFIG_FILE "${CMAKE_CURRENT_BINARY_DIR}/rmf_utils-config.cmake")

configure_package_config_file(
  "${CMAKE_CURRENT_LIST_DIR}/cmake/rmf_utils-config.cmake.in"
  ${PACKAGE_CONFIG_FILE}
  INSTALL_DESTINATION ${INSTALL_CONFIG_DIR}
)

write_basic_package_version_file(
  ${PACKAGE_CONFIG_VERSION_FILE}
  COMPATIBILITY ExactVersion
)

install(
  TARGETS rmf_utils
  EXPORT rmf_utils-targets
  DESTINATION lib
)

install(
  DIRECTORY include/rmf_utils
  DESTINATION include
)

install(
  FILES
    ${PACKAGE_CONFIG_VERSION_FILE}
    ${PACKAGE_CONFIG_FILE}
  DESTINATION ${INSTALL_CONFIG_DIR}
)

install(
  EXPORT rmf_utils-targets
  FILE rmf_utils-targets.cmake
  NAMESPACE rmf_utils::
  DESTINATION ${INSTALL_CONFIG_DIR}
)

export(
  EXPORT rmf_utils-targets
  FILE ${CMAKE_CURRENT_BINARY_DIR}/rmf_utils-targets.cmake
  NAMESPACE rmf_utils::
)

find_package(ament_cmake_catch2 QUIET)
find_package(ament_cmake_uncrustify QUIET)
if(BUILD_TESTING AND ament_cmake_catch2_FOUND AND ament_cmake_uncrustify_FOUND)
  file(GLOB_RECURSE unit_test_srcs "test/*.cpp")

  ament_add_catch2(
    test_rmf_utils test/main.cpp ${unit_test_srcs}
    TIMEOUT 300)
  target_link_libraries(test_rmf_utils
    rmf_utils
  )
  target_include_directories(test_rmf_utils
    PRIVATE
      $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/>
  )

  find_file(uncrustify_config_file
    NAMES "rmf_code_style.cfg"
    PATHS "test/format/")

  ament_uncrustify(
    ARGN include src test
    CONFIG_FILE ${uncrustify_config_file}
    MAX_LINE_LENGTH 80
    EXCLUDE include/rmf_utils/catch.hpp
  )
endif()

install(
  FILES
    test/format/rmf_code_style.cfg
  DESTINATION share/${PROJECT_NAME}
)

# Export ament index path
file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/share/ament_index/resource_index/packages/${PROJECT_NAME} "")
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/share/ament_index/resource_index/packages/${PROJECT_NAME} DESTINATION share/ament_index/resource_index/packages)

file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/share/${PROJECT_NAME}/hook/ament_prefix_path.dsv "prepend-non-duplicate;AMENT_PREFIX_PATH;")
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/share/${PROJECT_NAME}/hook/ament_prefix_path.dsv DESTINATION share/${PROJECT_NAME}/hook)
