# Site Kelli Klein Transfer

Site estático de 4 páginas, pronto para GitHub + Vercel (sem build).

- `index.html` – Transfer Natal Pipa (home)
- `transfer-natal-pipa.html` – trechos, veículos e reserva
- `passeios-em-pipa.html` – passeios privativos saindo de Pipa
- `sobre-e-contato.html` – sobre a empresa e formulário que monta a mensagem do WhatsApp
- `styles.css`, `site.js` – estilos e scripts compartilhados
- `sitemap.xml`, `robots.txt`, `vercel.json` (cleanUrls: as URLs ficam sem .html)

Para editar textos: altere os arquivos em `src/` e rode `python3 build.py` (gera as páginas na raiz).
O build espera `src/` ao lado de `build.py` e grava em `./site`; ao rodar a partir desta pasta, ajuste `OUT` para `ROOT`.

Pendências antes de publicar:
- Subir `logo-kelli-klein.png` e `og-kelli-klein-transfer.jpg` (1200x630) na raiz.
- Substituir o logotipo em texto pelo SVG oficial da marca, se disponível.
- Inserir fotos reais (Instagram) nas capas dos passeios.
