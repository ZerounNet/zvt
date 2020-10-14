# script to auto generate some files
import os


def export_interfaces(module='./domain/meta'):
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'samples', 'data.zip'))
    import pkgutil
    for importer, modname, ispkg in pkgutil.iter_modules([module]):
        print("Found submodule %s (is a package: %s)" % (modname, ispkg))
        for element_name in dir(importer):
            print(element_name)



if __name__ == '__main__':
    # zip_dir(ZVT_TEST_DATA_PATH, zip_file_name=DATA_SAMPLE_ZIP_PATH)
    export_interfaces()
