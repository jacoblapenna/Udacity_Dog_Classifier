#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    
    print(f"========= Summary of {model.upper()} Model Classification Results =========")
    
    """
    # print non-dog image information for debugging
    for key in results_dic:
        if not results_dic[key][3]:
            print(results_dic[key])
    """
    print()
    print("CLASSIFICATION TOTALS:")
    print(f"Number of total images: {results_stats['n_images']}")
    print(f"Number of dog images: {results_stats['n_dogs_img']}")
    print(f"Number of non-dog images: {results_stats['n_notdogs_img']}")
    print(f"Number of correctly classified dog images: {results_stats['n_correct_dogs']}")
    print(f"Number of correctly classified dog images with correctly classified breed: {results_stats['n_correct_breed']}")
    print(f"Number of images correctly determined as not being dogs: {results_stats['n_correct_notdogs']}")
    # print(f"Number of incorrectly classified non-dog images (i.e. flase positives): {results_stats['n_false_positives']}")
    print(f"Number of total correct classifications (dog or not): {results_stats['n_match']}")
    print()
    print("CLASSIFICATION PERCENTS:")
    print(f"Percentage of total correct matches: {results_stats['pct_match']}")
    print(f"Percentage of dog images correctly classified as dogs: {results_stats['pct_correct_dogs']}")
    print(f"Percentage of dog images where the breed of dog was correctly identified: {results_stats['pct_correct_breed']}")
    print(f"Percentage of images correctly determined as not being dogs: {results_stats['pct_correct_notdogs']}")
    # print(f"Percentage of non-dog pets which were classified as dogs (i.e. false positives): {results_stats['pct_false_positives']}")
    
    if print_incorrect_dogs or print_incorrect_breed:
        incorrect_dogs = []
        incorrect_breeds = []
        for key in results_dic:
            value = results_dic[key]
            if print_incorrect_dogs:
                if value[3] and not value[4]:
                    incorrect_dogs.append((key, value[1]))
            if print_incorrect_breed:
                if value[3] and value[4] and not value[2]:
                    incorrect_breeds.append((key, value[1]))
        if print_incorrect_dogs:
            print()
            print("INCORRECTLY CLASSIFIED DOG IMAGES:")
            if incorrect_dogs:
                for icd in incorrect_dogs:
                    print(f"File {icd[0]} was incorrectly classified as {icd[1]}.")
            else:
                print("None encountered.")
        if print_incorrect_breed:
            print()
            print("INCORRECTLY CLASSIFIED BREEDS:")
            if incorrect_breeds:
                for icb in incorrect_breeds:
                    print(f"File {icb[0]} was correctly classified as a dog though the breed was incorrectly classified as {icb[1]}.")
            else:
                print("None encountered.")
    
    print()
  
                 
