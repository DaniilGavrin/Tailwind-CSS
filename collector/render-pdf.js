const puppeteer = require('puppeteer');
const fs = require('fs');
const { marked } = require('marked');

(async () => {
    console.log('📖 Читаю Markdown...');
    const md = fs.readFileSync('../output/tailwind-css-guide-compressed.md', 'utf-8');
    
    console.log('🎨 Читаю CSS...');
    const css = fs.readFileSync('print.css', 'utf-8');
    
    console.log('🔄 Конвертирую в HTML...');
    const html = marked.parse(md);
    const fullHtml = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>${css}</style>
</head>
<body>${html}</body>
</html>
    `;
    
    console.log('🚀 Запускаю Puppeteer...');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setContent(fullHtml, { waitUntil: 'networkidle0' });
    
    console.log('📄 Генерирую PDF...');
    await page.pdf({
        path: '../output/tailwind-guide2.pdf',
        format: 'A4',
        printBackground: true,
        margin: { top: '10mm', bottom: '10mm', left: '8mm', right: '8mm' }
    });
    
    await browser.close();
    console.log('✅ PDF готов: output/tailwind-guide.pdf');
})();