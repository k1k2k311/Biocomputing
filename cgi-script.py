from functions import getData, getCodonTable
import cgi
import pandas as pd

''' PERHAPS ADD DEBUGGING '''

'''
print ("Content-Type: text/html\n")

form = cgi.FieldStorage()

input = form['input'].value
type = form['type'].value
'''

# data = getData('geneid',geneid)
# [DNA,CDS_loc,codon_table,enzyme_table] = data


testCDS = 'TTTTTTTTTAGAGAGAATCCTACTCTCTAAGCTTCGCGCGAAGCTCGCGCGC' \
          'GATAGCGCATAGCGCTAGCTATCAGCGGGGCGCCCGCGCCTCCTATATATATTCATTCTAGGAGGCTTCTTAAAGCT'

codon_table = pd.DataFrame(getCodonTable(testCDS)).T
codon_table.columns = ['Triplet', 'Amino Acid', 'Gene %', 'Chr %', 'Relative Frequency', 'P-value']
codon_table['First']= codon_table['Triplet'].astype(str).str[0]
codon_table['Second']= codon_table['Triplet'].astype(str).str[1]
codon_table['Third']= codon_table['Triplet'].astype(str).str[2]
index = pd.MultiIndex.from_product([['T','C','A','G'],['T','C','A','G'],['T','C','A','G']])
index1 = pd.MultiIndex.from_product([['T','C','A','G'],['T','C','A','G']])
index2 = pd.MultiIndex.from_product([['T','C','A','G'],['Triplet', 'Amino Acid', 'Gene %', 'Chr %', 'Relative Frequency', 'P-value']])
index3 = pd.MultiIndex.from_product([['T','C','A','G'],['T','C','A','G'],['T','C','A','G'],['Triplet', 'Amino Acid', 'Gene %', 'Chr %', 'Relative Frequency', 'P-value']])
df = codon_table.set_index(index)
print(df.unstack())