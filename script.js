const api = "http://127.0.0.1:5000/tarefas";

async function carregar() {
    const res = await fetch(api);
    const dados = await res.json();

    const lista = document.getElementById("lista");
    lista.innerHTML = "";

    dados.forEach(t => {
        const li = document.createElement("li");

        li.innerHTML = `
            <strong>${t.titulo}</strong> - ${t.prioridade} - ${t.status}
            <button onclick="concluir(${t.id})">✔</button>
            <button onclick="remover(${t.id})">X</button>
        `;

        lista.appendChild(li);
    });
}

async function adicionar() {
    const titulo = document.getElementById("titulo").value;
    const descricao = document.getElementById("descricao").value;
    const prioridade = document.getElementById("prioridade").value;

    await fetch(api, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({titulo, descricao, prioridade})
    });

    carregar();
}

async function concluir(id) {
    await fetch(api + "/" + id, {method: "PUT"});
    carregar();
}

async function remover(id) {
    await fetch(api + "/" + id, {method: "DELETE"});
    carregar();
}

carregar();
