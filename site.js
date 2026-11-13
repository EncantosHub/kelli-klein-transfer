(function () {
  var ZAP = "5541995519817";
  // Chave pública (publishable) do Supabase: só permite inserir pedidos, sem leitura.
  var SB_URL = "https://sganexgnpqaqdvbxdvsw.supabase.co";
  var SB_KEY = "sb_publishable_ASNfi6fSEn0StrBUrCcL7g_q-70b0dj";

  // Raios de luz da identidade: linhas que partem de um ponto acima do centro
  document.querySelectorAll(".raios").forEach(function (el) {
    var n = parseInt(el.getAttribute("data-n") || "26", 10);
    var ns = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(ns, "svg");
    svg.setAttribute("viewBox", "0 0 1000 300");
    svg.setAttribute("preserveAspectRatio", "none");
    svg.setAttribute("aria-hidden", "true");
    var ox = 500, oy = -260;
    for (var i = 0; i < n; i++) {
      var a = (12 + (156 * i) / (n - 1)) * Math.PI / 180;
      var r1 = 330 + ((i * 37) % 90);
      var r2 = 900;
      var l = document.createElementNS(ns, "line");
      l.setAttribute("x1", (ox + Math.cos(a) * r1).toFixed(1));
      l.setAttribute("y1", (oy + Math.sin(a) * r1).toFixed(1));
      l.setAttribute("x2", (ox + Math.cos(a) * r2).toFixed(1));
      l.setAttribute("y2", (oy + Math.sin(a) * r2).toFixed(1));
      svg.appendChild(l);
    }
    el.appendChild(svg);
  });

  // Menu mobile
  var t = document.querySelector(".menu-toggle"), m = document.getElementById("menu");
  if (t && m) {
    t.addEventListener("click", function () {
      var aberto = m.classList.toggle("aberto");
      t.setAttribute("aria-expanded", aberto ? "true" : "false");
      t.textContent = aberto ? "Fechar" : "Menu";
    });
  }

  // Card de passeio inteiro leva aos detalhes; o botão de agendar segue para o WhatsApp
  document.querySelectorAll(".passeio[data-href]").forEach(function (card) {
    card.addEventListener("click", function (ev) {
      if (ev.target.closest("a")) return;
      location.href = card.getAttribute("data-href");
    });
  });

  // Ano do rodapé
  document.querySelectorAll("[data-ano]").forEach(function (e) { e.textContent = new Date().getFullYear(); });

  // Formulário de orçamento: monta a mensagem e o link do WhatsApp
  var f = document.getElementById("form-orcamento");
  if (f) {
    f.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var v = function (id) { var x = document.getElementById(id); return x ? x.value.trim() : ""; };
      var linhas = [
        (/passeio/i.test(v("f-servico")) ? "Olá, vim do site Kelli Klein Transfer e gostaria de agendar um passeio." : "Olá, vim do site Kelli Klein Transfer e gostaria de agendar minha viagem."),
        "Nome: " + v("f-nome"),
        "Serviço: " + v("f-servico"),
        "Saída: " + v("f-origem"),
        "Destino: " + v("f-destino"),
        "Data: " + v("f-data") + (v("f-voo") ? " | Voo: " + v("f-voo") : ""),
        "Passageiros: " + v("f-pax")
      ];
      if (v("f-obs")) linhas.push("Observações: " + v("f-obs"));
      var msg = linhas.join("\n");

      // Guarda o pedido no Supabase (tabela orcamentos). Se falhar, o WhatsApp segue funcionando.
      try {
        var pax = parseInt(v("f-pax"), 10);
        fetch(SB_URL + "/rest/v1/orcamentos", {
          method: "POST",
          headers: { "apikey": SB_KEY, "Content-Type": "application/json", "Prefer": "return=minimal" },
          body: JSON.stringify({
            nome: v("f-nome"), servico: v("f-servico"), origem: v("f-origem"), destino: v("f-destino"),
            data_horario: v("f-data"), voo: v("f-voo"), passageiros: isNaN(pax) ? null : pax,
            observacoes: v("f-obs"), pagina: location.pathname
          })
        }).catch(function () {});
      } catch (e) {}
      var out = document.getElementById("resultado");
      out.hidden = false;
      document.getElementById("resultado-texto").textContent = msg;
      document.getElementById("resultado-link").href = "https://wa.me/" + ZAP + "?text=" + encodeURIComponent(msg);
    });
  }
})();
