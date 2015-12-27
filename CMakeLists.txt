CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

rez_find_packages(PREFIX pkgs AUTO)

set(oiio_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url_oiio https://github.com/OpenImageIO/oiio.git)
set(tag_oiio Release-${oiio_version})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

# Create a wrapper script for cmake commands
set(PKG_CONFIG_PATH $ENV{PKG_CONFIG_PATH})
configure_file(configure_wrapper.in configure_wrapper @ONLY)
set(conf_wrapper ${PROJECT_BINARY_DIR}/configure_wrapper)

###########################################
#
# For now we are apllying a patch to be able to build agains a custom python.
# The patch makes it possible to specify the PYTHON_HOME.
#
###########################################
ExternalProject_add(
    oiio
    GIT_REPOSITORY ${url_oiio}
    GIT_TAG ${tag_oiio}
    PATCH_COMMAND patch -p1 -t -N < ${CMAKE_CURRENT_SOURCE_DIR}/custom_python.patch
    PREFIX oiio
    CMAKE_COMMAND ${conf_wrapper} cmake
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DVERBOSE=ON -DILMBASE_HOME=$ENV{REZ_ILMBASE_ROOT} -DOPENEXR_HOME=$ENV{REZ_OPENEXR_ROOT} -DPYTHON_HOME=$ENV{REZ_PYTHON_ROOT} -DOCIO_PATH=$ENV{REZ_OCIO_ROOT}
    BUILD_IN_SOURCE 0
)

rez_install_files(
    cmake/oiio.cmake
    DESTINATION .
)
