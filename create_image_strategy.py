from abc import ABCMeta, abstractmethod
import subprocess
import webbrowser
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os.path
from os import path
from file_name_builder_pattern import PyrClassDiaFileNameBuilder
from file_name_builder_pattern import ValClassContentsFileNameBuilder
from file_name_builder_pattern import FileNameDirector
from file_to_data import FileToData
import numpy as np


class ImageContext(object):
    def __init__(self, image_strategy):
        self.image_strategy = image_strategy

    def produce_image(self, file_name):
        self.image_strategy.create_image_algor(file_name)
        self.image_strategy.display_image_algor(file_name)


class ImageStrategy(metaclass=ABCMeta):
    def __init__(self):
        self.file_to_data = FileToData()
        self.pyr_name_builder = PyrClassDiaFileNameBuilder()
        self.file_name_dir = FileNameDirector(self.pyr_name_builder)
        self.val_name_builder = ValClassContentsFileNameBuilder()

    @abstractmethod
    def create_image_algor(self, file_name):
        pass

    @abstractmethod
    def display_image_algor(self, file_name):
        pass


class ClassImageStrategy(ImageStrategy):

    def create_image_algor(self, file_names):
        self.file_name_dir.set_builder(self.pyr_name_builder)
        self.file_name_dir.construct_file_name(file_names)
        python_file_name = self.pyr_name_builder.get_python_file_name()
        if path.exists(python_file_name):
            pyreverse_command = 'pyreverse -ASmn -o png -p ' + file_names
            subprocess.call(pyreverse_command)
        else:
            print("Your given python file does not exist in the current "
                  "directory or your input arguments were wrong. The "
                  "input arguments should be [png_file_name_suffix "
                  "py_file_name.py]. Please try again!")

    def display_image_algor(self, file_names):
        self.file_name_dir.set_builder(self.pyr_name_builder)
        self.file_name_dir.construct_file_name(file_names)
        png_file_name = self.pyr_name_builder.get_image_file_name()
        if path.exists(png_file_name):
            img = mpimg.imread(png_file_name)
            fig = plt.imshow(img)
            fig.axes.get_xaxis().set_visible(False)
            fig.axes.get_yaxis().set_visible(False)
            plt.show()
        else:
            print("The image of class diagram cannot be generate.")
            print("Please check with your system administrators.")


class ValidateImageStrategy(ImageStrategy):

    def create_image_algor(self, file_name):
        self.file_name_dir.set_builder(self.val_name_builder)
        self.file_name_dir.construct_file_name(file_name)
        python_file_name = self.val_name_builder.get_python_file_name()
        png_file_name = self.val_name_builder.get_image_file_name()
        if path.exists(python_file_name):
            num_of_classes = 0
            num_of_functions = 0
            file_to_data = FileToData()
            file_to_data.read_file(python_file_name)
            num_of_classes = len(file_to_data.tree.body)

            print("---There are " + str(num_of_classes) +
                  " classes.-------------------")
            print("-----The classes are: -------------------")
            for my_class in file_to_data.tree.body:
                print("-------" + my_class.name + " class")
            for my_class in file_to_data.tree.body:
                print("---------The " + my_class.name + " class has " +
                      str(len(my_class.body)) + " functions")
                num_of_functions += len(my_class.body)
                print("-----------The functions in " +
                      my_class.name + " class are ")
                for my_function in my_class.body:
                    print("---------------" + my_function.name + " function")
            print("total number of classes is " + str(num_of_classes))
            print("total number of functions is " + str(num_of_functions))
            types_x = ["class", "function"]
            x_pos = np.arange(len(types_x))
            num_y = [num_of_classes, num_of_functions]
            plt.bar(x_pos, num_y, align='center', alpha=0.5)
            plt.xticks(x_pos, types_x)
            plt.ylabel('Total Numbers')
            plt.title('Total Numbers of classes and functions')
            plt.savefig(png_file_name)
        else:
            print("Your given python file does not exist in "
                  "the current directory ")
            print("or your input arguments were wrong. The input arguments ")
            print("should be [py_file_name.py]. ")
            print("Please try again!")

    def display_image_algor(self, file_name):
        self.file_name_dir.set_builder(self.val_name_builder)
        self.file_name_dir.construct_file_name(file_name)
        png_file_name = self.val_name_builder.get_image_file_name()
        if path.exists(png_file_name):
            img = mpimg.imread(png_file_name)
            plt.show()
        else:
            print("The image of validate class diagram cannot be generate.")
            print("Please check with your system administrators.")


# Below for manual test only
if __name__ == '__main__':
    file_names_created = "test test.py"
    class_image = ImageContext(ClassImageStrategy())
    class_image.produce_image(file_names_created)

    file_name_created = "test.py"
    class_image = ImageContext(ValidateImageStrategy())
    class_image.produce_image(file_name_created)
