#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Jacob Lapenna
# DATE CREATED:                                  
# REVISED DATE: June 3, 2022
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
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
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                         a percentage or a count) where the key is the statistic's 
                         name (starting with 'pct' for percentage or 'n' for count)
                         and the value is the statistic's value. See comments above
                         and the previous topic Calculating Results in the class for details
                         on how to calculate the counts and statistics.
    """ 
    
    stats = {}
    
    stats["n_images"] = 0 # number of images
    stats["n_dogs_img"] = 0 # number of dog images
    stats["n_notdogs_img"] = 0 # number of NON-dog images
    stats["n_match"] = 0 # number of matches between pet & classifier labels
    stats["n_correct_dogs"] = 0 # number of correctly classified dog images
    stats["n_correct_notdogs"] = 0 # number of correctly classified NON-dog images
    stats["n_correct_breed"] = 0 # number of correctly classified dog breeds
    # stats["n_false_positives"] = 0 # number of false positives (i.e. non-dogs classified as dogs or incorrectly classified non-dog images)
    stats["pct_match"] = 0 # percentage of correct matches
    stats["pct_correct_dogs"] = 0 # percentage of correctly classified dogs
    stats["pct_correct_breed"] = 0 # percentage of correctly classified dog breeds
    stats["pct_correct_notdogs"] = 0 # percentage of correctly classified NON-dogs
    # stats["pct_false_positives"] = 0 # percentage of false positives
    
    def percent(key1, key2):
        if stats[key2]:
            return round(stats[key1]/stats[key2] * 100, 1)
        else:
            return 0
    
    for key in results_dic:
        value = results_dic[key]
        stats["n_images"] += 1
        if value[3]:
            stats["n_dogs_img"] += 1
        else:
            stats["n_notdogs_img"] += 1
            """
            # the actual correct way to count correct matches of non-dog images
            if value[2]:
                stats["n_correct_notdogs"] += 1
            """
            # the desired, incorrect way to count correct non-dog images
            if value[4]:
                stats["n_correct_notdogs"] += 1
        if value[2]:
            stats["n_match"] += 1
        if value[3] and value[4]:
            stats["n_correct_dogs"] += 1
        if value[3] and value[2]:
            stats["n_correct_breed"] += 1
    
    stats["pct_match"] = percent("n_match", "n_images")
    stats["pct_correct_dogs"] = percent("n_correct_dogs", "n_dogs_img")
    stats["pct_correct_breed"] = percent("n_correct_breed", "n_dogs_img")
    stats["pct_correct_notdogs"] = 100.0 - percent("n_correct_notdogs", "n_notdogs_img")
    # stats["pct_false_positives"] = percent("n_false_positives", "n_notdogs_img")
    
    # return the stats dictionary created in this function 
    return stats
