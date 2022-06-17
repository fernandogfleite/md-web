from django.http import HttpResponse
from django.shortcuts import render
from rsa.apps.core.utils import generate_public_key, decrypt_message, encrypt_message, inverse, linear_combination, phi

def index_view(request):
    return render(request, 'index.html')


def encrypt_view(request):
    erros = {}
    if request.method == 'POST':
        chave = request.POST.get('chave').split()
        try:
            n = int(chave[0])
            e = int(chave[1])
        except ValueError:
            erros['mensagem'] = "Chave pública inválida"

            return render(request, 'encriptar.html', erros)

        mensagem = request.POST.get('mensagem')

        try:
            mensagem_criptografada = encrypt_message(mensagem, e, n)

            filename = "encrypted_message.txt"
            response = HttpResponse(mensagem_criptografada, content_type='text/plain')
            response['Content-Disposition'] = f'attachment; filename={filename}'

            return response
        
        except ValueError as erro:
            erros['mensagem'] = str(erro)

    return render(request, 'encriptar.html', erros)


def decrypt_view(request):
    erros = {}
    if request.method == 'POST':
        p = int(request.POST.get('primo_p'))
        q = int(request.POST.get('primo_q'))
        e = int(request.POST.get('expoente_e'))
        mensagem = request.POST.get('mensagem')

        try:
            s = linear_combination(e, phi(p, q))[1]
            d = inverse(s, 0, phi(p, q))

            mensagem_descriptografada = decrypt_message(mensagem, d, p*q)

            filename = "decrypted_message.txt"
            response = HttpResponse(mensagem_descriptografada, content_type='text/plain')
            response['Content-Disposition'] = f'attachment; filename={filename}'

            return response
        
        except Exception as erro:
            erros['mensagem'] = str(erro)

    return render(request, 'desencriptar.html', erros)


def generate_public_key_view(request):
    erros = {}
    if request.method == 'POST':
        p = int(request.POST.get('primo_p'))
        q = int(request.POST.get('primo_q'))
        e = int(request.POST.get('expoente_e'))

        try:
            public_key = generate_public_key(p, q, e)

            filename = "public_key.txt"
            response = HttpResponse(public_key, content_type='text/plain')
            response['Content-Disposition'] = f'attachment; filename={filename}'

            return response
        
        except ValueError as erro:
            erros['mensagem'] = str(erro)

    return render(request, 'chave.html', erros)
