#!/usr/bin/env python
# coding: utf-8

# Usage: python <samplefile.csv> <assayfile.csv>
# Will export three csv files
# One with Sample and Assay combined on Sample Name column
# One with Sample and Assay combined but only including columns in which
# there is more than one Value
# One with the columns and values that were the same in all samples.

import sys
import pandas as pd

samplefile = sys.argv[1]
assayfile = sys.argv[2]

sample = pd.read_csv(samplefile)
assay = pd.read_csv(assayfile)

combined = sample.merge(assay, on='Sample Name')

combined.to_csv('SampleAssay.csv')

# check for columns where all values are the same
# export to separate csv
# export simplified csv with only varying columns

shared_parameters = []
shared_values = []

for column in combined.columns:
    n = len(pd.unique(combined[column]))
    if(n == 1):
        value = combined[column][0]
        #print(column, value, sep='\t')
        combined = combined.drop(labels=column, axis=1)
        shared_parameters.append(column)
        shared_values.append(value)
    else: 
        pass
combined.to_csv('SampleAssaySimple.csv')

shared = pd.DataFrame(list(zip(shared_parameters, shared_values)), columns=['Parameters', 'Values'])
shared.to_csv('SampleAssayShare.csv')
