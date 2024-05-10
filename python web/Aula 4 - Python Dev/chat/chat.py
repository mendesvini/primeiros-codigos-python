import flet as ft

def main(pagina):
    titulo = ft.Text('Hastzap')

    titulo_janela = ft.Text('Bem vindo ao hasgzap')
    campo_nome = ft.TextField(label='Escreva seu nome no chat')

    chat = ft.Column()
    
    def mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(mensagem_tunel)
    def enviar_mensagem (evento):
        textomensagem = campo_mensagem.value
        nomeusuario = campo_nome.value
        mensagem = f'{nomeusuario}:{textomensagem}'
        pagina.pubsub.send_all(mensagem)
        
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label='Escreva uma mensagem no chat')
    btn_enviar = ft.ElevatedButton('enviar',on_click=enviar_mensagem)

    linha_mensagem = ft.Row([campo_mensagem,btn_enviar])
    def entrar_chat(event):
        pagina.remove(titulo)
        pagina.remove(btn)
        janela.open = False

        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f'{campo_nome.value} entrou no chat'
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    btn_poup = ft.ElevatedButton('Entrar no chat',on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela,content=campo_nome,actions=[btn_poup])
    def iniciar(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
    btn = ft.ElevatedButton('Iniciar chat',on_click=iniciar)
    pagina.add(titulo)
    pagina.add(btn)
    


ft.app(main,view=ft.WEB_BROWSER)