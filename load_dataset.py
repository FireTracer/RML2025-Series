import numpy as np
import pickle, random
import torch

from torch.utils.data import DataLoader, TensorDataset
import os

def dat_loader(path,train_bs=128,test_bs=128,ratio=0.8):
    with open(path, 'rb') as file:
        Xd = pickle.load(file,encoding='bytes')
    snrs,mods = map(lambda j: sorted(list(set(map(lambda x: x[j], Xd.keys())))), [1,0])
    X = []
    lbl = []
    for mod in mods:
        for snr in snrs:
            X.append(Xd[(mod,snr)])
            for i in range(Xd[(mod,snr)].shape[0]):  lbl.append((mod,snr))
    X = np.vstack(X)

    n_examples = X.shape[0]
    n_train = np.uint32(n_examples * ratio)
    np.random.seed(2016)
    train_idx = np.random.choice(range(0,n_examples), size=n_train, replace=False)
    test_idx = list(set(range(0,n_examples))-set(train_idx))

    print('if {} == 83808, wo can make sure random seed is right\n'.format(train_idx[0]))
    X_train = X[train_idx]
    Y_train = list(map(lambda x: mods.index(lbl[x][0]), train_idx))
    SNR_train = list(map(lambda x: snrs.index(lbl[x][1]), train_idx))

    X_test = X[test_idx]
    Y_test = list(map(lambda x: mods.index(lbl[x][0]), test_idx))
    SNR_test = list(map(lambda x: snrs.index(lbl[x][1]), test_idx))

    train_set_all = TensorDataset(torch.tensor(X_train), torch.tensor(Y_train),torch.tensor(SNR_train))
    test_set_all = TensorDataset(torch.tensor(X_test), torch.tensor(Y_test), torch.tensor(SNR_test))
    train_loader_all = DataLoader(dataset=train_set_all, batch_size=train_bs,shuffle=True,num_workers=0,drop_last=True)
    test_loader_all = DataLoader(dataset=test_set_all, batch_size=test_bs,num_workers=0)

    return train_loader_all,test_loader_all





if __name__ == "__main__":
    data = dat_loader('./data/AWGN.dat')
    print()


