import pandas as pd

@data_loader
def extract() -> dict[pd.DataFrame]:
    """
    Function to read .csv from data/input

    Return:
        dict[pd.DataFrame]: Dictionary with all content.
    """
    return {
        "clientes": pd.read_csv("data/input/clientes.csv"),
        "itens_vendas": pd.read_csv("data/input/itens_vendas.csv"),
        "produtos": pd.read_csv("data/input/produtos.csv"),
        "vendas": pd.read_csv("data/input/vendas.csv"),
    }