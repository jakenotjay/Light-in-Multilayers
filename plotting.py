import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

filename = './data.csv'

lamda = []
trans = []
transPhase = []
ref = []
refPhase = []

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            lamda.append(float(row[0]))
            trans.append(float(row[1]))
            transPhase.append(float(row[2]))
            ref.append(float(row[3]))
            refPhase.append(float(row[4]))
            line_count += 1

df = pd.DataFrame(list(zip(lamda, trans, transPhase, ref, refPhase)), columns=['Lamda', 'Trans', 'Trans Phase', 'Ref', 'Ref Phase'])
print(df)

plotLamda = []
plotTrans = []
plotRef = []

for i in range(0, len(df), 50):
    plotLamda.append(df['Lamda'][i])
    plotTrans.append(df['Trans'][i])
    plotRef.append(df['Ref'][i])

# fig = go.Figure(data=go.Scatter(x=plotLamda, y=plotRef))
# fig.show()
# this is completely fucked
figTransVsRef = make_subplots()

figTransVsRef.add_trace(
    go.Scatter(x=plotLamda, y=plotTrans, name='Mean channel width of  fibres as a function of depth (z)')
)

figTransVsRef.add_trace(
    go.Scatter(x=plotLamda, y=plotRef, name='Fraction of image taken up by fibres as a function of depth (z)')
)

figTransVsRef.update_layout(
    title_text="Comparison of fibre fraction to channel width"
)

figTransVsRef.update_xaxes(title_text="Mask Depth, Z-height, (um)")

figTransVsRef.update_yaxes(title_text="Mean Channel Width (um)")
figTransVsRef.update_yaxes(title_text="Fibre fraction")

figTransVsRef.show()