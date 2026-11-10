#!/usr/bin/env python3
"""Monta as 4 páginas do site da Kelli Klein Transfer a partir de partes compartilhadas."""
import json, pathlib, urllib.parse

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
OUT = ROOT
DOM = "https://www.kellikleintransfer.com.br"
ZAP = "5541995519817"
ZAP_MSG = "Olá, conheci o serviço de TRANSFER da agência Kelli Klein e quero agendar minha viagem"
ZAP_URL = f"https://wa.me/{ZAP}?text=" + urllib.parse.quote(ZAP_MSG)
TEL_TXT = "+55 41 99551-9817"
INSTA = "https://www.instagram.com/kellikleintransfer/"

ICO_ZAP = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3Z"/></svg>'

PAGES = [
    ("index.html", "Início", "/"),
    ("transfer-natal-pipa.html", "Transfer e trechos", "/transfer-natal-pipa"),
    ("passeios-em-pipa.html", "Passeios", "/passeios-em-pipa"),
    ("sobre-e-contato.html", "Sobre e contato", "/sobre-e-contato"),
]

NEGOCIO = {
    "@type": ["LocalBusiness", "TaxiService"],
    "@id": DOM + "/#empresa",
    "name": "Kelli Klein Transfer",
    "alternateName": "Kelli Klein Transfer Natal Pipa e Região",
    "slogan": "Transporte para quem quer ser bem recebido",
    "url": DOM + "/",
    "telephone": "+5541995519817",
    "image": DOM + "/og-kelli-klein-transfer.jpg",
    "logo": DOM + "/logo-kelli-klein.png",
    "priceRange": "$$",
    "address": {"@type": "PostalAddress", "streetAddress": "R. Dr. Ronaldo Maranhão, 1071 - Casa 31 - Nova Esperança",
                "addressLocality": "Parnamirim", "addressRegion": "RN", "postalCode": "59144-040", "addressCountry": "BR"},
    "areaServed": [
        {"@type": "City", "name": "Natal"}, {"@type": "City", "name": "Tibau do Sul"},
        {"@type": "Place", "name": "Praia da Pipa"}, {"@type": "City", "name": "Parnamirim"},
        {"@type": "City", "name": "São Gonçalo do Amarante"}, {"@type": "City", "name": "João Pessoa"},
        {"@type": "City", "name": "Recife"}, {"@type": "State", "name": "Rio Grande do Norte"}],
    "availableLanguage": ["pt-BR", "es"],
    "sameAs": [INSTA],
}


def head(title, desc, path, extra_ld=None):
    ld = {"@context": "https://schema.org", "@graph": [NEGOCIO] + (extra_ld or [])}
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOM}{path}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#1C1A1B">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Kelli Klein Transfer">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOM}{path}">
<meta property="og:image" content="{DOM}/og-kelli-klein-transfer.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600&family=Poppins:wght@400;500;600&display=swap">
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
"""


def header(active):
    links = "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == active else ""}>{n}</a>' for f, n, _ in PAGES)
    return f"""<header class="topo">
  <div class="wrap">
    <a class="marca" href="index.html" aria-label="Kelli Klein Transfer, página inicial">
      <span class="nome">Kelli<br>Klein</span><span class="sub">select<br>transfer<br>group</span>
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
    <nav class="menu" id="menu" aria-label="Principal">
      {links}
      <a class="btn btn-rosa" href="{ZAP_URL}" target="_blank" rel="noopener">Reservar</a>
    </nav>
  </div>
</header>
"""


def footer():
    return f"""<footer class="rodape">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="marca" href="index.html"><span class="nome">Kelli<br>Klein</span><span class="sub">select<br>transfer<br>group</span></a>
        <p style="margin-top:14px;max-width:34ch">Transfer privativo do Aeroporto de Natal para a Praia da Pipa e trechos em todo o Rio Grande do Norte, Paraíba e Pernambuco.</p>
      </div>
      <div>
        <h3>Trechos</h3>
        <ul>
          <li><a href="transfer-natal-pipa.html#aeroporto">Aeroporto de Natal → Pipa</a></li>
          <li><a href="transfer-natal-pipa.html#trechos">Natal → Pipa</a></li>
          <li><a href="transfer-natal-pipa.html#trechos">João Pessoa → Pipa</a></li>
          <li><a href="transfer-natal-pipa.html#trechos">Recife → Pipa</a></li>
        </ul>
      </div>
      <div>
        <h3>Site</h3>
        <ul>{"".join(f'<li><a href="{f}">{n}</a></li>' for f, n, _ in PAGES)}</ul>
      </div>
      <div>
        <h3>Contato</h3>
        <ul>
          <li>WhatsApp: <a href="{ZAP_URL}" target="_blank" rel="noopener">{TEL_TXT}</a></li>
          <li>Instagram: <a href="{INSTA}" target="_blank" rel="noopener">@kellikleintransfer</a></li>
          <li>Atendimento todos os dias, com agendamento</li>
          <li>Parnamirim · Natal · Pipa — RN</li>
        </ul>
      </div>
    </div>
    <div class="base">
      <span>© <span data-ano>2026</span> Kelli Klein Transfer. Transfer Natal Pipa e região.</span>
      <span>Identidade visual: DOS II Creative Media & Design</span>
    </div>
  </div>
</footer>
<a class="zap" href="{ZAP_URL}" target="_blank" rel="noopener" aria-label="Falar com a Kelli Klein Transfer no WhatsApp">{ICO_ZAP}</a>
<script src="site.js"></script>
</body>
</html>
"""


def build():
    for f, _, path in PAGES:
        meta = json.loads((SRC / (f + ".json")).read_text())
        body = (SRC / f).read_text()
        body = body.replace("{{ZAP_URL}}", ZAP_URL).replace("{{ICO_ZAP}}", ICO_ZAP).replace("{{TEL}}", TEL_TXT).replace("{{INSTA}}", INSTA)
        extra = meta.get("ld", [])
        if f != "index.html":
            extra = extra + [{"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": DOM + "/"},
                {"@type": "ListItem", "position": 2, "name": meta["crumb"], "item": DOM + path}]}]
        html = head(meta["title"], meta["description"], path, extra) + header(f) + "<main>\n" + body + "\n</main>\n" + footer()
        (OUT / f).write_text(html)
        print("ok", f, len(html))


if __name__ == "__main__":
    build()
