#>>>>>>>>>>>>>>>>>>>>>>>>>>Codigo desenvolvido Suzana Gomes<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#pip install "dask[complete]"

import dask[complete]
import dask.dataframe as dd
import pyarrow.parquet as pq

# funçao recebe o caminho de um arquivo como parâmetro, verifica o tipo e transforma em parquet
@dask.delayed
def convert_parquet(caminho_arquivo):
    if caminho_arquivo.endswith('.csv'):
        base = dd.read_csv(caminho_arquivo)
        base.to_parquet(caminho_arquivo + '.parquet')
    elif caminho_arquivo.endswith('.sav'):
        base = dd.read_spss(caminho_arquivo)
        base.to_parquet(caminho_arquivo + '.parquet')
    else:
        print(f"Arquivo não suportado: {caminho_arquivo}")



if __name__ == '__main__':
    caminhos_arquivos = ['caminho_arquivo.csv', 'caminho_arquivo2.sav', 'caminho_arquivo3.sav', 'caminho_arquivo4.csv', 'caminho_arquivo5.csv']

    dask.compute(*[dask.delayed(convert_parquet)(caminho_arquivo) for caminho_arquivo in caminhos_arquivos])
    
    
 #if __name__ == '__main__'é uma estrutura dentro do seu código para executar ou não uma parte específica do código em outro arquivo.
#O conteúdo dentro da estrutura if__name__==”main” só vai ser executado quando você rodar o código do arquivo, 
#caso contrário o que tem dentro dessa estrutura não será executado. (https://www.hashtagtreinamentos.com/if__name____main__-no-python)   

#Em if __name__ == '__main__' usamos a função dask.delayed para atrasar a chamada da função "convert_parquet" para cada arquivo. 
# Em seguida, usamos dask.compute com * para executar essas tarefas em paralelo.
# O resultado final será a conversão de todos os arquivos em paralelo pelo Dask.

##
#>>>>>>>>>>>>>>>>>>>>> Paralelismo:dask.delay
#>>>>>>>>>>>>>>>>>>>>>>>>>>>Estudos:
#https://docs.dask.org/en/stable/delayed-best-practices.html#:~:text=Compute%20on%20lots%20of%20computation%20at%20once,-To%20improve%20parallelism&text=delayed%20calls%20to%20define%20your,moving%20forward%20with%20your%20code.
#https://tutorial.dask.org/03_dask.delayed.html
#https://docs.dask.org/en/stable/delayed.html
#https://community.revelo.com.br/dask-uma-ferramenta-pythonic-para-processamento-de-dados/