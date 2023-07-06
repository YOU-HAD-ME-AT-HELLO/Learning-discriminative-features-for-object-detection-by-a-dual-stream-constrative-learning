import pickle


def load_file(filename):
    with open(filename, 'rb') as fo:
        data = pickle.load(fo, encoding='latin1')
    return data

dictCow = {'num_cases_per_batch':20,#每个batch包含的样本数量
           'label_names':['0', '1'],#类别索引，将类别索引表（object_list.txt）中的label_names:填进去
           'num_vis':3072}#这里不要动

f = open('bin3/batches.meta','wb')
pickle.dump(dictCow,f)

f.close()
data = load_file('bin3/batches.meta')
print(data.keys())
print(data.values())
