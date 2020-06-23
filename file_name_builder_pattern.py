from abc import ABCMeta, abstractmethod


class FileNameBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.python_file_name = ""
        self.image_file_name = ""

    def get_python_file_name(self):
        return self.python_file_name

    def get_image_file_name(self):
        return self.image_file_name

    @abstractmethod
    def create_python_file_name(self, arg_name):
        pass

    @abstractmethod
    def create_image_file_name(self, arg_name):
        pass


class PyrClassDiaFileNameBuilder(FileNameBuilder):
    def create_python_file_name(self, arg_name):
        self.python_file_name = arg_name[(arg_name.find(" ") + 1):]

    def create_image_file_name(self, arg_name):
        self.image_file_name = 'classes_' + \
            arg_name[0:(arg_name.find(" "))] + '.png'


class ValClassContentsFileNameBuilder(FileNameBuilder):
    def create_python_file_name(self, arg_name):
        self.python_file_name = arg_name

    def create_image_file_name(self, arg_name):
        self.image_file_name = 'validate_' + arg_name.split(".")[0] + '.png'


class FileNameDirector(object):
    def __init__(self, builder):
        self.builder = builder

    def set_builder(self, builder):
        self.builder = builder

    def construct_file_name(self, arg_name):
        self.builder.create_python_file_name(arg_name)
        self.builder.create_image_file_name(arg_name)


# Below for manual test only
# if __name__ == "__main__":
    # arg_name_pyr_class_dia = 'trial test.py'
    # arg_name_val_class_contents = 'test.py'

    # pyr_name_builder = PyrClassDiaFileNameBuilder()
    # file_name_dir = FileNameDirector(pyr_name_builder)
    # file_name_dir.construct_file_name(arg_name_pyr_class_dia)
    # print(pyr_name_builder.get_python_file_name())
    # print(pyr_name_builder.get_image_file_name())

    # val_name_builder = ValClassContentsFileNameBuilder()
    # file_name_dir.set_builder(val_name_builder)
    # file_name_dir.construct_file_name(arg_name_val_class_contents)
    # print(val_name_builder.get_python_file_name())
    # print(val_name_builder.get_image_file_name())
