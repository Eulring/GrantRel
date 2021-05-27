import os 
import json

class PipeDataset():
    def __init__(self, data_root, split):
        if split == 'test': 
            self.tar_file = 'test_pipe.json'
        with open(os.path.join(data_root, self.tar_file)) as json_file:
            all_data = json.load(json_file)
        
        sents, pmcids, psgcy, psgid, label = [], [], [], [], []
        N = len(all_data)
        count = 0

        # ipdb.set_trace()
        for pmcid, units in all_data.items():
            for unit in units:
                if unit.get('flag') == 'j' or unit.get('flag') == 'J' or unit.get('flag') == 'q': 
                    continue
                if unit.get('psgcy') == None: unit['psgcy'] = []
                if unit.get('psgid') == None: unit['psgid'] = []
                if len(unit['psgcy']) != len(unit['psgid']):
                    continue
                pmcids.append(pmcid)
                sents.append(unit['sent'])
                psgcy.append(unit['psgcy'])
                psgid.append(unit['psgid'])
                label.append(unit['class'])

        assert len(sents) == len(pmcids) == len(psgcy) == len(psgid)
        self.sents = sents 
        self.pmcids = pmcids 
        self.psgcy = psgcy 
        self.psgid = psgid
        self.label = label
        print(len(sents))


data_root = './Grant-SP'
test_dataset = PipeDataset(data_root, 'test')