CMAKE_MINIMUM_REQUIRED(VERSION 3.16)

include(RezBuild)

# Don't have to rely on any compiler
project($ENV{REZ_BUILD_PROJECT_NAME} NONE)

# Info
message(STATUS "Installing ${REZ_BUILD_PROJECT_NAME}")

# Gen .pyc and copy files(.py and .pyc)
file(GLOB_RECURSE sources python/*.py)
rez_install_python(
    $ENV{REZ_BUILD_PROJECT_NAME}
    FILES ${sources}
    DESTINATION $ENV{REZ_BUILD_INSTALL_PATH}
)