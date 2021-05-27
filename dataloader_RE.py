# the dataset loader for the manually tagging dataset

import numpy as np 
import json
import os
from tqdm import tqdm
import ipdb

class JointDataset():
    def __init__(self, data_root, split):

        if split == 'test': 
            self.tar_file = 'test.json'
        if split == 'train': 
            self.tar_file = 'train.json'
        if split == 'eval': 
            self.tar_file = 'dev.json'
        if split == 'test_arxiv':
            self.tar_file = 'test_arxiv.json'
        with open(os.path.join(data_root, self.tar_file)) as json_file:
            all_data = json.load(json_file)
        
        sents, pmcids, psgcy, psgid = [], [], [], []
        N = len(all_data)
        count = 0

        for pmcid, units in all_data.items():
            
            for unit in units:
                # if unit.get('flag') == 'j' or unit.get('flag') == 'J' or unit.get('flag') == 'q': 
                #     continue
                if len(unit['psgcy']) != len(unit['psgid']):
                    continue
                if len(unit['psgcy']) == 0:
                    continue
                count += 1
                pmcids.append(pmcid)
                sents.append(unit['sent'])
                psgcy.append(unit['psgcy'])
                psgid.append(unit['psgid'])

        assert len(sents) == len(pmcids) == len(psgcy) == len(psgid)
        self.sents = sents 
        self.pmcids = pmcids 
        self.psgcy = psgcy 
        self.psgid = psgid
        print("Samples : {}".format(count))


data_root = './Grant-RE'
train_dataset = JointDataset(data_root, 'train')
eval_dataset = JointDataset(data_root, 'eval')
test_dataset = JointDataset(data_root, 'test')
test_arxiv_dataset = JointDataset(data_root, 'test_arxiv')