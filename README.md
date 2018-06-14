#Existem 2 arquivos em formato texto que deverão ser processados:
   NFe.txt 
      Contém os documentos fiscais. 
   
   NFeTran.txt
      Contém as transações dos documentos fiscais.


##1) Criar um Web Services RESTful (formato JSON) que disponibilize os seguintes serviços:
###   Com base no arquivo NFe.txt:    
      a. Filtro dos documentos fiscais por período e tipo de documento (entrada/saída);
      b. Filtro de documentos fiscais por chave da NF-e;
      c. Filtro de documentos fiscais por documento do destinatário;
      d. Totalizadores (valor total, valor produto, valor ICMS e valor IPI) da movimentação por período e tipo de documento (entrada/saída);
      e. Filtro dos documentos por status (AUTORIZADO, REJEITADO, DENEGADO e/ou CANCELADO)
      f. O documento fiscal e suas transações (arquivo NFeTran.txt), onde será realizada sua busca pela Chave. 
   
###   Com base no arquivo NFeTran.txt
      a. Retorne de forma sintética:
         i. Quantas transações retornaram erro e detalhe por tipo de erro
         ii. Quantas transações foram autorizadas com sucesso
         iii. Estatística por SEFAZ-UF

##2) Criar o frontend para consumo dos serviços criados acima.

# Requisitos

1. Use a linguagem que você tem mais habilidade (temos preferência por Java, Node.js, Ruby, Golang ou Python, mas poderá ser utilizado qualquer linguagem desde que explicado a preferência).
2. As APIs deverão seguir o modelo RESTFul com formato JSON  
3. Faça testes unitários, suite de testes bem organizados (atenção especial nesse item).
4. Use git e tente fazer commits pequenos e bem descritos.
5. Faça pelo menos um README explicando como fazer o setup, uma explicação da solução proposta, o mínimo de documentação para outro desenvolvedor entender seu código
6. Siga o que considera boas práticas de programação.
7. Após concluir o teste suba em um REPOSITÓRIO PRIVADO e nos mande o link.