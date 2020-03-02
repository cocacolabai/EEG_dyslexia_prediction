#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:04:10 2020

@author: breixo
"""

from dataset_generator import DataGenerator
import numpy as np

class ModifiedDataGenerator(DataGenerator):
    
    def __init__(
            self, 
            list_IDs,
            main_labels,
            label_dict,
            binarizer_dict,
            ignore_labels,
            path_data,
            filenames,
            data_path, 
            to_fit=True, #TODO: implement properly for False
            n_average = 30,
            batch_size=32,
            iter_per_epoch = 2,
            up_sampling = True,
            n_timepoints = 501,
            n_channels=30,
            include_baseline = False,
            subtract_baseline = False,
            baseline_label = None,
            shuffle=True,
            warnings=False):
        super().__init__(
                list_IDs,
                main_labels,
                label_dict,
                binarizer_dict,
                ignore_labels,
                path_data,
                filenames,
                data_path, 
                to_fit,
                n_average,
                batch_size,
                iter_per_epoch,
                up_sampling,
                n_timepoints,
                n_channels,
                include_baseline,
                subtract_baseline,
                baseline_label,
                shuffle,
                warnings)
        
        self.initialize_functions()


    def initialize_functions(self):
        functions = np.array([[[0]] * self.n_channels] * self.n_timepoints)
        print(functions.shape)
        
        
        self.functions = functions

    def __getitem__(self, index):
        if self.to_fit:
            original_X, y = super().__getitem__(index)
        else:
            original_X = super().__getitem__(index)
        X = self.modify_batch(original_X)
        if self.to_fit:
            return X, y
        else:
            return X


    def modify_batch(self, original_X):
        X = original_X # TODO Modify
        for i in range(X.shape[0]):
            item = self.modify_item(X[i])
            X[i] = item
        return X


    def modify_item(self, o_item):
        item = np.add(o_item, self.functions)
        return item



if __name__ == "__main__":
    test_generator = ModifiedDataGenerator(
            list_IDs = IDs_train,
            main_labels = main_labels,
            label_dict = label_dict,
            binarizer_dict = binarizer_dict,
            ignore_labels = ignore_labels,
            path_data = PATH_DATA_processed,
            filenames = [x[:-4] for x in files_csv],
            data_path = PATH_DATA_processed, 
            to_fit=True, 
            n_average = 40,
            batch_size = 10,
            iter_per_epoch = 30,
            up_sampling = True,
            n_timepoints = 501,
            n_channels=30,
            shuffle=True)
    
    X, y = test_generator[0]
#    Xb = test_generator.__getitem__(0)