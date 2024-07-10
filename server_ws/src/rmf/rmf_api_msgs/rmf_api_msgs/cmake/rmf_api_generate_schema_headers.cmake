#################################################
# rmf_api_generate_schema_headers(
#   PACKAGE <package_name>
#   SCHEMAS_DIR <schema_directory>
# )
#
# This function takes a schema file and generates a C++ header
# file that hardcodes the schema into it as a const string.
function(rmf_api_generate_schema_headers)

  cmake_parse_arguments(
    _ARG
    ""
    "PACKAGE;SCHEMAS_DIR"
    ""
    ${ARGN}
  )

  string(TOUPPER ${_ARG_PACKAGE} upper_package_name)
  file(GLOB_RECURSE schema_files "${_ARG_SCHEMAS_DIR}/*.json")

  foreach(file_name ${schema_files})
    get_filename_component(schema_name ${file_name} NAME_WE)
    string(TOUPPER ${schema_name} upper_schema_name)
    file(READ ${file_name} schema_text)

    configure_file(
      ${RMF_API_GENERATE_SCHEMA_TEMPLATE}
      ${CMAKE_BINARY_DIR}/rmf_api_generate_schema_headers/include/${_ARG_PACKAGE}/schemas/${schema_name}.hpp
      @ONLY
    )
  endforeach()

  install(
    DIRECTORY ${CMAKE_BINARY_DIR}/rmf_api_generate_schema_headers/include/
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
  )

endfunction()
