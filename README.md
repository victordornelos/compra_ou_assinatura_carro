# Análise dos custos de comprar ou assinar um carro

Autores: Adriano Souza Lima, Luiz Fernando M. Meirinho e Victor Flávio P. Dornelos \
E-mail: adrianoflu16@gmail.com | luizfcefetrj@gmail.com | victor.dornelos@hotmail.com

![Foto da fábrica do polo](fabrica-da-volkswagen-brasil---taubate---producao-do-polo.jpg)



## 1. Objetivo:

O objetivo dessa análise é avaliar a escolha entre realizar uma **assinatura** de carro ou **comprar** um automóvel. O serviço de assinatura de automóvel, foi iniciado a partir de 2015 e popularizado em 2021, consistindo em alugar um carro por um longo período com pagamento de mensalidade, enquanto outros custos serão pagos pela locadora.

Portanto, se tornou um debate econômico a questão de comprar ou assinar um carro. Dessa forma, iremos analisar os principais **custos** e **fatores** que possam impactar essa escolha, visando obter um resultado com a satisfação entre os diferentes cenário, por meio da calculadora criada em Python.

## 2. Metodologia:

A decisão entre comprar ou assinar será diretamente influenciada por variáveis econômicas e pessoais, tanto por desejos quanto capacidade financeira. Assim, durante análise, foi utilizado um automóvel da marca Volkswagen, modelo “**Polo Highline TSI 2024 0km**”, pelo fato de ter sido o 2º carro mais emplacado em 2023, no valor aproximado de 118 mil reais obtidos diretamente do site da montadora, enquanto para estimar o valor da assinatura foi utilizado o site da Locadora Movida, que é uma das maiores empresas desse setor e que disponibiliza mais facilmente os dados.

Nesse sentido, para fazer a comparação é necessário determinar alguns pressupostos, assim, o valor da **inflação** foi representado pelo índice IPCA em 4,5% ao ano, CDI como a taxa de investimento do **custo de oportunidade** no valor de 11,06% anual que é média desde 2000 obtido no BCB SGS, então tornando possível obter uma taxa de retorno real. Outrossim, foi considerar a **depreciação nominal** em 8% que é um valor que varia muito conforme o modelo de carro, tempo de uso, quilometragem e conservação, sendo difícil sua estimação precisa.

Ademais, para calcular os **impostos estaduais** foi usado o estado do Rio de Janeiro como referência. Outro fator, foi considerar que a **quilometragem anual** será de 15 mil km e os preços de **revisão** foram obtidos do site da Volkswagen. Além disso, o preço do **seguro do carro** foi determinado em 5,6% correspondendo ao IPSA (Índice de Preço de Seguro de Automóveis) do valor de mercado do carro.

Na realidade brasileira, é bastante comum comprar carro por meio de **financiamento**, então para isso foi adotado uma **taxa de financiamento** 1,87% ao mês que é a média de março de 2024 com base de dados do BCB, usando o método **PRICE** onde as parcelas são valores fixo e juros reduz com o tempo. Nessa conjuntura, visando obter a melhor análise possível simulamos cenários que variam entre comprar à vista ou financiar com **entrada** de 10%,20%,40%,60% ou 80%, além disso também variamos o **tempo da assinatura** e **financiamento** com as possibilidades de 1, 2, 3 ou 4 anos considerando que o financiamento seja o mesmo prazo que a assinatura.

## 3. Cenário Base:

Consideramos para a escolha da compra do automóvel, os seguintes custos obrigatórios:

- **Juros do financiamento**: importante custo a ser considerado, visto que esses juros são bastante elevados e representam uma grande despesa quanto menor for o valor da entrada.
- **Seguro**: apesar do seguro não ser obrigatório, o carro por assinatura tem esse custo incluso na mensalidade, assim para a correta comparação ele precisa ser considerado.
- **Depreciação real**: representa outro custo extremamente importante, pois o valor da depreciação nominal já é elevado em carros novos, e ao somar a inflação, temos o custo mais elevado em comparação aos outros.
- **Impostos**: corresponde as despesas com o IPVA, licenciamento anual e emplacamento do veículo e IOF no caso de financiamento.
- **Custo de oportunidade**: corresponde as despesas com o custo incorrido ao não investir o valor do carro em uma aplicação financeira.
- **Manutenção**: corresponde ao custo de manutenção do veículo realizado em concessionaria a cada quilometragem definida pela marca do veículo, somado ao custo de troca de pneu a cada 45 mil quilômetros.

Já em relação ao carro de assinatura, temos o seguinte custo:

- **Valor da assinatura**: valor único mensal, reajusto pela inflação a cada ano, enquanto todos os outros custos do carro já estão incluídos na assinatura.

Dado esses custos, trabalhamos em nosso cenário base, com pagamento a vista, sem financiamento e no período escolhido de 4 anos. Dessa forma, ao fim desse tempo, o **saldo** resultante da subtração do preço do carro com os seus seguintes custos, será de -R$ 9.729,60, enquanto esse mesmo saldo em relação a assinatura, será de -R$ 12.923,75, por consequência, ao subtrairmos o saldo da assinatura pelo saldo do carro próprio, teremos como resultado obtido -R$ 3.093,36, ou seja, é **vantajoso** nessa conjuntura comprar o carro ao invés de alugar. Outro teste realizado, foi variar o período de anos para 1, 2 ou 3, mesmo assim o resultado não mudou, continuou valendo mais a pena comprar o carro.

Nesse sentido a pequena vantagem do carro próprio perante a assinatura pode ser explicada por um custo de oportunidade mais conservador, pois o juro real retirando os impostos ficou no valor de 5,33%, ou seja, caso a pessoa consiga um investimento que pague pelo menos 6,5% de juro real, fará com que o carro por assinatura seja a melhor opção em comparação a compra.

Outro fator importante a destacar é a questão do **tempo** e da **burocracia**, de modo que no carro próprio, todos os processos de manutenção, cotação de seguro, pagamento de impostos é feito pelo individuo, enquanto no carro por assinatura, tudo é feito pela locadora, significando assim uma economia de tempo.

## 4. Os diferentes cenários:

Inicialmente, é importante evidenciar o papel do **custo de oportunidade** nos diferentes cenários propostos nesse trabalho (compra de veículo: à vista, financiado (20%, 40%, 60%, 80% ou 90%) ou, assinatura). Quanto maior o capital imobilizado inicialmente, maior o custo de oportunidade,como por exemplo, um carro comprado à vista. Conforme se opte por possibilidades de aquisição do veículo como o financiamento, o custo de oportunidade é minimizado. Isso ocorre, porque ao escolher compromissar um valor de entrada menor, o custo de deixar de ganhar com outras escolhas, é mais baixo. É o que se verifica na análise, o custo de oportunidade diminui dependendo da escolha de financiamento.

Entretanto, os **juros** se comportam de forma oposta, quanto maior o financiamento, maior os juros, isso ocorre por dois principais fatores: o **risco** e a **proporcionalidade**. O primeiro acontece porque quanto menor o valor da entrada, maior a dívida com o financiamento do carro, e menor o “compromisso inicial” de obtenção do bem, gerando um risco maior de inadimplência e, consequentemente, juros mais altos. O segundo acontece porque se a entrada é menor, as parcelas são maiores, e como os juros incidem sobre o valor das parcelas, os juros aumentam com o aumento do financiamento. Para o cenário de se comprar o veículo à vista, os juros são nulos, não há risco e nem parcelas.

Devido ao movimento das duas variáveis descritas acima, a diminuição do custo de oportunidade e o aumento dos juros, no caso de aquisição do veículo à vista (não há juros), há uma propensão a se preferir a aquisição à assinatura. Mas, por causa da incorrência de altos juros, as opções de financiamento (qualquer um deles) são preteridas em relação à assinatura.

## 5. Considerando outras opções:

Alguns carros são mais vantajosos que outros, no sentido de que o valor da assinatura comparado com o preço do carro pode variar entre as escolhas. Por exemplo, o Versa tem o preço de R$ 151.490,00, e sua assinatura custa R$ 2.719,50. Dessa forma, o valor da assinatura equivale a 1,79% do preço do carro. Possui um maior **custo-benefício**, por exemplo, que o carro objeto desse estudo, no qual a assinatura do Polo equivale a 2,24% do preço do carro. E há ainda, exemplos extremos, como a assinatura do TAN EV Premium, que tem o preço de R$ 529.890,00, e sua assinatura custa R$ 24.029,40, assinatura essa que equivale a 4,5% do valor do carro, representando valores bem maiores que as outras duas assinaturas.

## 6. Conclusão:

Por fim, após diferentes cenários, pode-se inferir que a escolha entre **carro próprio** e carro por **assinatura** dependerá principalmente do carro a ser escolhido e do custo de oportunidade a ser considerado, visto que os outros custos são relativamente estáveis entre diferentes carros. Cabe ainda ressaltar, que a diferença monetária entre alugar e assinar não é muito elevada, em cenários sem financiamento, dessa forma, a consequência será que o indivíduo deve realizar as contas para verificar seu cenário específico, observando qual será a opção mais vantajosa, apenas relembrando que na maioria dos casos de financiamento, a assinatura será consideravelmente mais barata.


