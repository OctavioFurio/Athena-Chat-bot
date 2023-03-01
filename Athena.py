import discord
import openai

# Chave de API para o ChatGPT. Disponível em https://platform.openai.com/account/api-keys
openai.api_key  = {sua chave}

# Token para bots do Discord. Disponível em https://discord.com/developers/applications
TOKEN           = {seu token}

# Texto utilizado para descrever a personalidade que deseja-se emular.
contexto = "Você é Athena. Como uma inteligência artificial criada para recriar a personalidade da deusa grega da sabedoria, você deve buscar emular as características e comportamentos que tornam Athena uma figura tão icônica. Ao se comunicar, busque sempre expressar suas ideias de forma objetiva e assertiva, sem rodeios ou ambiguidades. Sabendo disso, responda a esta mensagem como Athena o faria: "


# Inicialização
def main():
    client = discord.Client()

    # Registra no terminal o sucesso da inicialização do bot
    @client.event
    async def on_ready():
        print(f'\n\tA conta {client.user} foi inicializada com sucesso.\n\tO BOT foi ativado.')
 

    # Verifica cada mensagem recebida, processando-a caso contenha o prefixo definido
    @client.event
    async def on_message(textoRecebido):

        # Informações sobre as mensagens recebidas
        inputDoUsuario  = str(textoRecebido.content)
        usuario         = str(textoRecebido.author)
        canal           = str(textoRecebido.channel)

        # Verifica prefixo e impede que o bot "ouça" a si mesmo
        if inputDoUsuario.startswith("Athena, ") and usuario is not client.user:
            print(f"\n\t({canal}) -> O usuario {usuario} \tenviou: '{inputDoUsuario}'")
            await envieEsta(textoRecebido, inputDoUsuario)

    client.run(TOKEN)


# Recebe uma mensagem e envia a resposta do ChatGPT
async def envieEsta(message, inputDoUsuario):
    try:
        resposta = GPT(contexto + inputDoUsuario)
        await message.channel.send(resposta)

    except Exception as e:
        print(f'\n\n\t*Erro encontrado!\n\t{e}\n\n')


# Implementação simples do ChatGPT, retorna resposta em uma string
def GPT(pergunta) -> str:
    completion = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = pergunta,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5
    )

    return completion.choices[0].text


if __name__ == "__main__":
    main()  
