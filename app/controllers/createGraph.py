import pandas as pd
import matplotlib.pyplot as plt
import os

def estadoGraph():
    metricas_df = pd.read_csv(os.path.join('app/models', 'for_Metricas.csv'), encoding = 'UTF-8')
    metricas_df1 = metricas_df[['task', 'state']]
    metricasfinal = metricas_df1.groupby(metricas_df1['state']).count().reset_index()

    #criação do gráfico
    plt.figure(figsize = (20, 8))
    metricasfinal = metricasfinal.sort_values(by='task', ascending=False)
    plt.bar(metricasfinal['state'], metricasfinal['task'], color='#038c3e', width = 0.9, edgecolor = '#000000', linewidth = 1)
    plt.axis('auto')
    plt.ylabel('Número de Vagas', fontsize = 14)
    plt.xlabel('Estados', fontsize = 14)
    plt.savefig(os.path.join('app/static/img', 'estadoGraph.png'), format='png', dpi=300, bbox_inches='tight')


def areaGraph():
    metricas_df = pd.read_csv(os.path.join('app/models', 'for_Metricas.csv'), encoding = 'UTF-8')
    metricas_df1 = metricas_df[['task', 'area']]
    metricasfinal = metricas_df1.groupby(metricas_df1['area']).count().reset_index()

    #criação do gráfico
    plt.figure(figsize = (20, 8))
    metricasfinal = metricasfinal.sort_values(by='task', ascending=False)
    plt.bar(metricasfinal['area'], metricasfinal['task'], color='#038c3e', width = 0.4, edgecolor = '#000000', linewidth = 1)
    plt.axis('auto')
    plt.ylabel('Número de Vagas', fontsize = 14)
    plt.xlabel('Áreas', fontsize = 14)
    plt.savefig(os.path.join('app/static/img', 'areaGraph.png'), format='png', dpi=300, bbox_inches='tight')

def cursoGraph():
    df = pd.read_csv(os.path.join('app/models', 'for_Metricas.csv'), encoding = 'UTF-8')
    df = pd.DataFrame(data=[[7, 'Tecnologia'], [2, 'Administração'], [2, 'Marketing'], [2, 'Gastronomia'], [2, 'Elétrica']], columns=['qtd_cursos', 'area'])

    #criação do gráfico
    plt.figure(figsize = (20, 8))
    plt.axis('auto')
    plt.ylabel('Número de Cursos', fontsize = 14)
    plt.xlabel('Áreas', fontsize = 14)
    plt.bar(df['area'], df['qtd_cursos'], color='#038c3e', width = 0.3, edgecolor = '#000000', linewidth = 1)
    plt.savefig(os.path.join('app/static/img', 'cursoGraph.png'), format='png', dpi=300, bbox_inches='tight')

