import fs from 'fs';
import path from 'path';
import { chromium, devices } from 'playwright';

const args = process.argv.slice(2);
const cmd = args[0];
function arg(name, fallback = null) {
  const i = args.indexOf(`--${name}`);
  return i !== -1 ? args[i + 1] : fallback;
}
const url = arg('url');
const selector = arg('selector');
const device = arg('device', 'desktop');
const fullPage = arg('fullPage', 'false') === 'true';
const outRoot = path.resolve('ops/browser-visual/artifacts');
fs.mkdirSync(outRoot, { recursive: true });
const stamp = new Date().toISOString().replace(/[:.]/g, '-');
const runDir = path.join(outRoot, stamp);
fs.mkdirSync(runDir, { recursive: true });

const mobileProfile = devices['iPhone 13'];
const launch = async () => {
  const browser = await chromium.launch({ headless: true });
  const context = device === 'mobile'
    ? await browser.newContext({ ...mobileProfile })
    : await browser.newContext({ viewport: { width: 1440, height: 1200 } });
  const page = await context.newPage();
  const consoleLogs = [];
  page.on('console', msg => consoleLogs.push(`[${msg.type()}] ${msg.text()}`));
  page.on('pageerror', err => consoleLogs.push(`[pageerror] ${err.message}`));
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 120000 });
  await page.waitForLoadState('load', { timeout: 30000 }).catch(() => null);
  await page.addStyleTag({ content: `*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important;} iframe{animation:none!important;}` }).catch(() => null);
  await page.waitForTimeout(2500);
  return { browser, context, page, consoleLogs };
};

(async () => {
  if (!url) throw new Error('--url is required');
  const { browser, page, consoleLogs } = await launch();
  if (cmd === 'screenshot') {
    const out = path.join(runDir, `${device}.png`);
    await page.screenshot({ path: out, fullPage, timeout: 120000, animations: 'disabled' });
    console.log(JSON.stringify({ ok: true, type: 'screenshot', device, fullPage, path: out, consoleLogs }, null, 2));
  } else if (cmd === 'inspect') {
    const data = selector
      ? await page.locator(selector).first().evaluate(el => ({ text: el.innerText, html: el.outerHTML }))
      : { title: await page.title(), h1: await page.locator('h1').first().innerText().catch(() => null) };
    const out = path.join(runDir, 'inspect.json');
    fs.writeFileSync(out, JSON.stringify({ data, consoleLogs }, null, 2));
    console.log(JSON.stringify({ ok: true, type: 'inspect', path: out, data, consoleLogs }, null, 2));
  } else if (cmd === 'overflow') {
    const data = await page.evaluate(() => {
      const docWidth = document.documentElement.scrollWidth;
      const winWidth = window.innerWidth;
      const offenders = Array.from(document.querySelectorAll('body *')).map(el => {
        const r = el.getBoundingClientRect();
        return {
          tag: el.tagName,
          className: el.className,
          id: el.id,
          right: r.right,
          left: r.left,
          width: r.width,
          text: (el.innerText || '').trim().slice(0, 120)
        };
      }).filter(x => x.width > winWidth + 1 || x.right > winWidth + 1 || x.left < -1).slice(0, 50);
      return { winWidth, docWidth, overflowing: docWidth > winWidth, offenders };
    });
    const out = path.join(runDir, 'overflow.json');
    fs.writeFileSync(out, JSON.stringify({ data, consoleLogs }, null, 2));
    console.log(JSON.stringify({ ok: true, type: 'overflow', path: out, data, consoleLogs }, null, 2));
  } else if (cmd === 'pdf') {
    const out = path.join(runDir, 'page.pdf');
    await page.pdf({ path: out, format: 'A4', printBackground: true });
    console.log(JSON.stringify({ ok: true, type: 'pdf', path: out, consoleLogs }, null, 2));
  } else {
    throw new Error('Unknown command');
  }
  await browser.close();
})().catch(err => {
  console.error(err.stack || String(err));
  process.exit(1);
});