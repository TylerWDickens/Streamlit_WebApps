import pandas as pd
import streamlit as st
import altair as alt

st.write("""
# DNA Nucleotide Count Web App

This app counts the necloetide compistion of the query DNA
""")

st.header('Enter DNA Sequence')

sequenceInput = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("DNA Sequence Input", sequenceInput, height=25)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('User Input (DNA Query):')
sequence

st.header('Output (DNA Nucleotide Count):')

st.subheader('1) Data as Dictionary')


def dnaNucleotideCount(seq):
    dnaDictionary = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])

    return dnaDictionary


dna = dnaNucleotideCount(sequence)

dna_label = list(dna)
dna_values = list(dna.values())

dna

st.subheader('2) Data as Text')

st.write('There are ' + str(dna['A']) + ' adenine (A)')
st.write('There are ' + str(dna['T']) + ' thymine (T)')
st.write('There are ' + str(dna['G']) + ' guanine (G)')
st.write('There are ' + str(dna['C']) + ' cytosine (C)')

st.subheader('3) Data as Dataframe')

df = pd.DataFrame.from_dict(dna, orient='index')
df = df.rename({0: 'Count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'Nucleotide'})
st.write(df)

st.subheader('4) Data as Bar Chart')

barChart = alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y='Count'
)

barChart = barChart.properties(
    width=alt.Step(80)
)

st.write(barChart)
