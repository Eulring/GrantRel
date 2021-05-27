import json
import os

class ClsDataset():
    def __init__(self, data_root, split):
        if split == 'train':
            self.tar_file = 'train_sent.json'
        if split == 'dev':
            self.tar_file = 'dev_sent.json'

        with open(os.path.join(data_root, self.tar_file)) as json_file:
            all_data = json.load(json_file)
        
        sents, pmcids, labels = [], [], []

        N = len(all_data)
        for pmcid, units in all_data.items():
            for unit in units:
                if unit.get('flag') == 'j' or unit.get('flag') == 'q':
                    continue
                pmcids.append(pmcid)
                sents.append(unit['sent'])
                if unit['class'] == [0] or unit['class'] == [1]:
                    labels.append(unit['class'][0])
                else: labels.append(unit['class'])
        
        assert len(sents) == len(pmcids) == len(labels)
        self.sents = sents
        self.pmcids = pmcids
        self.labels = labels
        print(len(sents))



data_root = './Grant-SP'
train_dataset = ClsDataset(data_root, 'train')
eval_dataset = ClsDataset(data_root, 'dev')