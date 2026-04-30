const slider = document.getElementById("tamanho");
const valor = document.getElementById("valor");
slider.oninput = () => {
   valor.innerText = slider.value;
};
async function gerarSenha() {
   const resposta = await fetch("/gerar", {
       method: "POST",
       headers: { "Content-Type": "application/json" },
       body: JSON.stringify({
           minusculas: document.getElementById("minusculas").checked,
           maiusculas: document.getElementById("maiusculas").checked,
           numeros: document.getElementById("numeros").checked,
           especiais: document.getElementById("especiais").checked,
           tamanho: slider.value
       })
   });
   const dados = await resposta.json();
   document.getElementById("senha").value = dados.senha;
}
function copiarSenha() {
   const campo = document.getElementById("senha");
   if (!campo.value) {
       alert("Gere uma senha primeiro!");
       return;
   }
   navigator.clipboard.writeText(campo.value);
   const botao = document.querySelector(".copiar");
   botao.innerText = "✅ Copiado!";
   setTimeout(() => {
       botao.innerText = "📋 Copiar Senha";
   }, 2000);
}