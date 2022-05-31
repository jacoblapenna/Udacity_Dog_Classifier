#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Jacob Lapenna
# DATE CREATED:                                   
# REVISED DATE: May 31, 2022
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse
import os

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() - data structure that stores the command line arguments object  
    """
    
    # create ArgumentParser object
    parser = argparse.ArgumentParser(usage="Program to classify dog breeds from their image.",
                                     description="The available arguments are:\n")
    
    # add expected valid arguments
    parser.add_argument("-d", "--dir",
                        default="pet_images",
                        type=str,
                        choices=[d for d in os.listdir() if os.path.isdir(d) and '.' not in d and "__" not in d], # argument validation method 1
                        help="The directory containing the dog images.")
    parser.add_argument("-a", "--arch",
                        default="vgg",
                        type=str,
                        choices=["resnet", "alexnet", "vgg"],
                        help="The convolutional neural network (CNN) model architecture to use for classification.")
    parser.add_argument("-df", "--dogfile",
                        default="dognames.txt",
                        type=str,
                        choices=[f for f in os.listdir() if ".txt" in f], # argument validation method 1
                        help="The text file which covers the available dog breed names.")
    
    # get the arguments for validation checks
    args = parser.parse_args()
    
    # argument validation method 2
    """
    # check that the --dir argument is a valid directory
    if not os.path.isdir(os.getcwd() + "/" + f"{args.dir}"):
        raise Exception("Invalid image directory, check the image directory argument entered!")
    # consider checking that the directory contains valid dog images (or images at all) in the future here.
    
    # the model is validated by choices when added to the parser.
    
    # check that the --dogfile argument is a valid file
    if not os.path.isfile(os.getcwd() + "/" + f"{args.dogfile}"):
        raise Exception("Invalid dog names file, check the dog file argument entered!")
    # consider checking that contents of specified file are valid dog names in the future here.
    """
    
    # if the arguments are valid, return the args object  
    return args
