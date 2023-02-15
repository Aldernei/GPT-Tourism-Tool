# GPT-Tourism-Tool

PT-BR 

Este código é um programa de sugestão de viagem que usa a API do OpenAI para gerar sugestões de destinos de viagem com base em uma descrição fornecida pelo usuário. O programa usa o modelo GPT-3 da OpenAI para gerar uma resposta que combina a descrição fornecida pelo usuário e um local específico, gerando assim uma sugestão personalizada.

A função 'get_trip_suggestion' solicita ao usuário uma descrição de viagem e, em seguida, chama o método 'openai.Completion.create' duas vezes, passando a descrição como entrada para gerar a sugestão de destino e uma descrição da sugestão como entrada para gerar uma explicação do motivo pelo qual a sugestão foi feita.

O loop 'while True' permite que o usuário obtenha quantas sugestões de viagem quiser. O programa exibe a sugestão gerada pelo modelo GPT-3 e pergunta ao usuário se ele deseja outra sugestão. Quando o usuário não deseja mais sugestões, o programa é encerrado.

EN-US 

This code is a travel suggestion program that uses the OpenAI API to generate travel destination suggestions based on a description provided by the user. The program uses OpenAI's GPT-3 model to generate a response that combines the user-provided description and a specific location, thus generating a personalized suggestion.

The 'get_trip_suggestion' function prompts the user for a travel description and then calls the 'openai.Completion.create' method twice, passing the description as input to generate the destination suggestion and a description of the suggestion as input to generate an explanation of why the suggestion was made.

The 'while True' loop allows the user to get as many travel suggestions as they want. The program displays the suggestion generated by the GPT-3 model and asks the user if they want another suggestion. When the user no longer wants any more suggestions, the program exits.
