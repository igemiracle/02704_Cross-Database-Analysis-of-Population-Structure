#PREDEFINED FUNCTIONS FOR YOUR USE
#functions partially borrowed from Harvard EPI511

# please set the path to your data directory here
path = '/Users/jingl1/Desktop/CMU/02704/hw1/hw_data/02704_data'

# please use the following function (or something like it) to read files
def pname(name):
    '''Prepend the path to the filename'''
    return path + '/' + name

def popen(name):
    '''Open file in the path'''
    return open(pname(name))

import numpy as np
import pandas as pd
import scipy.stats as ss
import itertools as it

# read in SNPs
def read_snp(file):
    '''Read a snp file into a pandas dataframe'''
    return(pd.read_table(
        file,
        sep='\s+', # columns are separated by whitespace
        # names of the columns
        names=[None, 'chromosome', 'morgans', 'position', 'ref', 'alt'],
        index_col=0
    ))

def read_snp_pop(pop):
    return(read_snp(pname(pop + '.snp')))

SNPs = read_snp_pop('HapMap3')

def get_chr_range(chromosome):
    '''Returns the range of positions where SNPs for a chromosome are kept'''
    filt = SNPs.query('chromosome=={}'.format(chromosome))
    start = SNPs.index.get_loc(filt.iloc[0].name)
    stop  = SNPs.index.get_loc(filt.iloc[-1].name) + 1
    return(start, stop)


# read in individual data
def read_ind(file):
    '''Read an ind file into a pandas dataframe'''
    return pd.read_table(
        file,
        sep='\s+',
        names=[None, 'sex', 'pop'],
        index_col=0
    )

def read_ind_pop(pop):
    return(read_ind(pname(pop + '.ind')))


# read in genotype data
import itertools as it

def read_geno(file):
    '''Reads a geno file into a numpy matrix'''
    return(np.genfromtxt(
        file,               # the file
        dtype='uint8',      # read the data in as 1-byte integers
        delimiter=1,        # 1-byte width data
        missing_values=9,   # 9 indicates missing data
        usemask=True        # return a masked array
    ))

def read_geno_pop(pop):
    return read_geno(pname(pop + '.geno'))

def read_geno_pop_chr(pop, chromosome):
    '''Reads a slice of a geno file into a numpy matrix'''
    f = popen(pop + '.geno')      # open the file
    (start, stop) = get_chr_range(chromosome)
    s = it.islice(f, start, stop) # slice the file
    return read_geno(s)
