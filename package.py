name = "oiio"

version = "1.7.14"

description = \
    """
    Open Image IO
    """

variants = [
    ["platform-linux"]
]

#build_requires = [
#    "cmake"
#]

requires = [
    "ocio-1.0.9",
    "ilmbase-2",
    "openexr-2",
    "jpeg-1",
    "tiff-4",
    "boost-1",
    "python-2.7",
    "zlib-1",
    "png-1"
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python/site-packages")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
