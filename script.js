// A interface é servida pelo mesmo Flask que fornece a API.
// Assim, não dependemos de um endereço localhost fixo no navegador.
const api = "/tarefas";
const lista = document.getElementById("lista");
const mensagem = document.getElementById("mensagem");
const campoTitulo = document.getElementById("titulo");
const campoDescricao = document.getElementById("descricao");
const campoPrioridade = document.getElementById("prioridade");

function avisar(texto, erro = false) {
    mensagem.textContent = texto;
    mensagem.style.color = erro ? "#b42318" : "#166534";
}

async function requisitar(url, opcoes = {}) {
    let resposta;
    try {
        resposta = await fetch(url, opcoes);
    } catch (erro) {
        throw new Error("Não foi possível conectar ao servidor. Abra o sistema pelo Flask.");
    }

    const tipo = resposta.headers.get("content-type") || "";
    const dados = tipo.includes("application/json") ? await resposta.json() : null;
    if (!resposta.ok) {
        throw new Error(dados?.erro || `Erro na requisição (${resposta.status}).`);
    }
    return dados;
}

async function carregar() {
    try {
        const tarefas = await requisitar(api);
        lista.replaceChildren();

        if (!tarefas.length) {
            const vazio = document.createElement("li");
            vazio.textContent = "Nenhuma tarefa cadastrada.";
            lista.appendChild(vazio);
            return;
        }

        for (const tarefa of tarefas) {
            const item = document.createElement("li");
            const resumo = document.createElement("strong");
            resumo.textContent = tarefa.titulo;
            item.appendChild(resumo);
            item.appendChild(document.createTextNode(
                ` - ${tarefa.prioridade} - ${tarefa.status} `
            ));

            const concluirBotao = document.createElement("button");
            concluirBotao.type = "button";
            concluirBotao.textContent = "Concluir";
            concluirBotao.disabled = tarefa.status === "concluido";
            concluirBotao.addEventListener("click", () => concluir(tarefa.id));

            const removerBotao = document.createElement("button");
            removerBotao.type = "button";
            removerBotao.textContent = "Excluir";
            removerBotao.addEventListener("click", () => remover(tarefa.id));

            item.append(concluirBotao, removerBotao);
            lista.appendChild(item);
        }
    } catch (erro) {
        lista.replaceChildren();
        avisar(erro.message, true);
    }
}

async function adicionar() {
    const titulo = campoTitulo.value.trim();
    const descricao = campoDescricao.value.trim();
    const prioridade = campoPrioridade.value;

    if (!titulo) {
        avisar("Informe o título da tarefa.", true);
        campoTitulo.focus();
        return;
    }

    try {
        await requisitar(api, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ titulo, descricao, prioridade })
        });
        campoTitulo.value = "";
        campoDescricao.value = "";
        campoPrioridade.value = "media";
        avisar("Tarefa adicionada com sucesso.");
        await carregar();
    } catch (erro) {
        avisar(erro.message, true);
    }
}

async function concluir(id) {
    try {
        await requisitar(`${api}/${id}`, { method: "PUT" });
        avisar("Tarefa concluída.");
        await carregar();
    } catch (erro) {
        avisar(erro.message, true);
    }
}

async function remover(id) {
    try {
        await requisitar(`${api}/${id}`, { method: "DELETE" });
        avisar("Tarefa excluída.");
        await carregar();
    } catch (erro) {
        avisar(erro.message, true);
    }
}

carregar();
