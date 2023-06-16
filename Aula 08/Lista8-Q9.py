import matplotlib.pyplot as plt

# Dados das categorias de produtos (exemplo)
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Móveis']
percentuais = [35.5, 24.5, 20, 20]

# Criar o gráfico de pizza
plt.pie(percentuais, labels=categorias, autopct='%1.1f%%')

# Configurar o título do gráfico
plt.title('Distribuição de Categorias de Produtos')

# Exibir o gráfico
plt.show()
