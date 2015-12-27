name = "oiio"

version = "1.6.8"

description = \
    """
    Open Image IO
    """

variants = [
    ["platform-linux"]
]

requires = [
    "ocio",
    "ilmbase",
    "openexr",
    "qt",
    "boost",
    "ffmpeg",
    "python"
]

uuid = "repository.oiio"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python/site-packages")
