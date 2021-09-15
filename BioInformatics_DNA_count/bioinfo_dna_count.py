# importin'Glibraries

import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# Page title
image = Image.open('deku.jpg')

st.image(image, use_column_width = True)

st.write("""
         # DNA Nucleotide Count Web App
         
         This app counts the nucleotide composition of query DNA!
         
         ***
         """)

# *** represents a horizontal line

# Inputting text box
st.header('Enter DNA sequence')

sequence_input = ">DNA Query2\naatatgagccatgcataccaaggacgtcatagggtcgcagacagactagtgcatctctgggtctacatgacatattcgaaaattaaacctagcctggctt\ngctgaggtggtgttgggcctgagcccgctagtgaagggagaatgcagccagttattagacgactacgacgattcgtattggtgtgcacgccgctaacttc\ncacaacctgcgcatgtatcgttcccttccgtaacttacttcgggagctgaatgtaacgcttcgcatggcggaggaaccgaatcataattttgtgtctcac"


sequence = st.text_area("Sequence input", sequence_input, height = 250)
sequence = sequence.splitlines()
sequence
sequence = sequence[1:] # skips the sequence name (first line)
sequence 
sequence = "".join(sequence) #concatenates list to string
sequence

st.write("""
         ***
         """)

# prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

#print dictionary
st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence.upper())

X

# Print Text
st.subheader('2. Print Text')
st.write(f"There are {X['A']} adenaine (A)")
st.write(f"There are {X['T']} thymine (T)")
st.write(f"There are {X['G']} adenaine (guanine)")
st.write(f"There are {X['C']} thymine (cytosine)")

# Displaying as DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis = 'columns')
df.reset_index(inplace = True)
df = df.rename({'index': 'nucleotide'}, axis = 'columns')
# df = df.rename(columns = {'index': 'nucleotide'})
st.write(df)


# Display as bar chart using altair
st.subheader('4. Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
)

p = p.properties(
    width = alt.Step(80) #controls the width of the bar
)

st.write(p)


