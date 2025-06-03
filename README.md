# MeuApp Django

Este projeto é um exemplo simples de aplicação Django com uma página inicial exibindo "Hello, World!" e um cabeçalho estilizado.

---

## ✅ Requisitos

Antes de começar, você precisa ter instalado no seu computador:

- Python (3.10+)
- VS Code
- Extensão do Python no VS Code
- Git (opcional, mas recomendado)

---

## ⚙️ Como rodar o projeto no VS Code

### 1. Clone o projeto ou baixe o código

Você pode clonar via Git ou apenas copiar os arquivos para uma pasta no seu computador.

### 2. Abra o VS Code na pasta do projeto

No terminal ou no Explorer, abra o VS Code na pasta onde está o projeto:

```bash
code .
```

### 3. Crie e ative um ambiente virtual

No terminal integrado do VS Code (pressione `Ctrl + aspas` para abrir):

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```

- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

Se tudo estiver certo, aparecerá algo como: `(venv)` no início da linha do terminal.

### 4. Instale as dependências

```bash
pip install django
```

### 5. Rode as migrações iniciais do Django

```bash
python manage.py migrate
```

### 6. Rode o servidor local

```bash
python manage.py runserver
```

Abra o navegador e vá para:

```
http://127.0.0.1:8000/
```

---

## 📂 Estrutura do Projeto

```
meuprojeto/
├── manage.py
├── meuprojeto/         # configurações do projeto
│   └── settings.py
├── meuapp/             # app principal com views e templates
│   ├── templates/
│   │   └── meuapp/
│   │       └── hello.html
│   └── static/
│       └── meuapp/
│           └── style.css
```

---

## 📌 O que este projeto faz?

- Mostra uma página inicial com:
  - Um título (`<h1>`) com o nome do app
  - Um botão estilizado com JavaScript simples
- Usa templates, arquivos estáticos e views do Django

---

## 🧪 Testar o botão

Clique no botão da página para ver uma mensagem de alerta JavaScript!

---

## 🚀 Próximos passos (opcional)

- Criar novas páginas com outras views
- Adicionar rotas no `urls.py`
- Conectar com um banco de dados real (como PostgreSQL)

---

## 🙋‍♀️ Suporte

Se tiver dúvidas ou erros ao rodar, me pergunte ou pesquise no [site oficial do Django](https://docs.djangoproject.com/pt-br/5.0/).
