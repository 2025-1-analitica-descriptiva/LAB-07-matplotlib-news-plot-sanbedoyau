import pandas as pd
import matplotlib.pyplot as plt
import os
from glob import glob

def pregunta_01():
    def create_ouptput_directory(output_directory: str):
        if os.path.exists(output_directory):
            for file in glob(f'{output_directory}/*'):
                os.remove(file)
            os.rmdir(output_directory)
        os.makedirs(output_directory)

    in_path = 'files/input'
    out_path = 'files/plots'

    df = pd.read_csv(f'{in_path}/news.csv', index_col=0)

    plt.figure()
    colors = dict(zip(df.columns, ['dimgray', 'grey', 'tab:blue', 'lightgrey']))
    zorder = dict(zip(df.columns, [1, 1, 2, 1]))
    linewidths = dict(zip(df.columns, [2, 2, 3, 2]))

    for col in df.columns:
        plt.plot(df[col], color=colors[col], label=col, zorder=zorder[col], linewidth=linewidths[col])

    plt.title('How people get their news', fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    first_year = df.index[0]
    last_year = df.index[-1]

    for col in df.columns:
        plt.scatter(x=first_year, y=df[col][first_year], color=colors[col], zorder=zorder[col])
        plt.text(x=first_year - 0.2, y=df[col][first_year], s=col + ' ' + str(df[col][first_year]) + '%', ha='right', va='center', color=colors[col])
        plt.scatter(x=last_year, y=df[col][last_year], color=colors[col], zorder=zorder[col])
        plt.text(x=last_year + 0.2, y=df[col][last_year], s=str(df[col][last_year]) + '%', ha='left', va='center', color=colors[col])

    plt.tight_layout()
    create_ouptput_directory(out_path)
    plt.savefig(f'{out_path}/news.png')