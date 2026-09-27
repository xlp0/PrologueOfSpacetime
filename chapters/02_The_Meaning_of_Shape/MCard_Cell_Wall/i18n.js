/**
 * Reusable Internationalization (i18n) Engine
 * Chapter: 02 - The Meaning of Shape
 * 
 * Decouples linguistic statements into external `locales.json`,
 * separating spatial mathematical invariants from presentation prose.
 * 
 * Works isomorphically in:
 * - Node.js (ES Module: synchronous auto-load via fs)
 * - Browser (fetch API or window.CellWallI18n)
 */

let localesData = {};
let currentLocale = 'id';
const listeners = new Set();

// Synchronous auto-load for Node.js environment
if (typeof process !== 'undefined' && process.versions && process.versions.node) {
  try {
    const fs = await import('fs');
    const jsonUrl = new URL('./locales.json', import.meta.url);
    const raw = fs.readFileSync(jsonUrl, 'utf-8');
    localesData = JSON.parse(raw);
  } catch (err) {
    console.warn('[i18n] Node auto-load of locales.json failed:', err.message);
  }
}

/**
 * Load or update locale definitions from an external URL or object
 * @param {string | object} source - Path to JSON file or raw locale object
 * @returns {Promise<object>} The loaded locale dictionary
 */
export async function loadLocales(source) {
  if (typeof source === 'object' && source !== null) {
    localesData = source;
  } else if (typeof source === 'string') {
    if (typeof fetch !== 'undefined') {
      const res = await fetch(source);
      if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
      localesData = await res.json();
    } else if (typeof process !== 'undefined') {
      const fs = await import('fs');
      const raw = fs.readFileSync(source, 'utf-8');
      localesData = JSON.parse(raw);
    }
  }

  // Notify listeners that locales updated
  for (const listener of listeners) {
    try {
      listener(currentLocale);
    } catch (e) {
      console.error('[i18n] Listener error:', e);
    }
  }

  return localesData;
}

/**
 * Set the active locale
 * @param {string} lang - Language code ('id', 'sa', 'en', 'zh-TW', etc.)
 * @returns {string} The active language code
 */
export function setLocale(lang) {
  let target = (lang === 'zh' || lang === 'zh-tw' || lang === 'zh-hant') ? 'zh-TW' : lang;
  if (target === 'sa-bali' || target === 'sanskrit' || target === 'bali') target = 'sa';
  if (localesData[target] || target === 'id' || target === 'en' || target === 'zh-TW' || target === 'sa') {
    currentLocale = target;
    if (typeof document !== 'undefined') {
      applyToDOM();
    }
    for (const listener of listeners) {
      try {
        listener(currentLocale);
      } catch (e) {
        console.error('[i18n] Error in locale change listener:', e);
      }
    }
  }
  return currentLocale;
}

/**
 * Get current active locale
 */
export function getLocale() {
  return currentLocale;
}

/**
 * Get list of available locales with metadata
 */
export function getAvailableLocales() {
  return Object.keys(localesData).map(k => localesData[k]?.meta || { code: k, name: k });
}

/**
 * Subscribe to locale change events
 * @param {Function} fn - Callback receiving new locale string
 * @returns {Function} Unsubscribe function
 */
export function onLocaleChange(fn) {
  listeners.add(fn);
  return () => listeners.delete(fn);
}

/**
 * Translate a key using dot notation and parameter interpolation
 * Example: t('header.mainTitle') or t('canvas.verticesCount', { count: 6 })
 * 
 * @param {string} key - Dot notation path
 * @param {object} params - Key-value map for parameter replacements
 * @param {string} lang - Optional explicit language code (defaults to currentLocale)
 * @returns {string} Translated string or fallback
 */
export function t(key, params = {}, lang = currentLocale) {
  let targetLang = (lang === 'zh' || lang === 'zh-tw' || lang === 'zh-hant') ? 'zh-TW' : lang;
  if (targetLang === 'sa-bali' || targetLang === 'sanskrit' || targetLang === 'bali') targetLang = 'sa';
  
  const dict = localesData[targetLang] || localesData.en || localesData.id || {};
  const parts = key.split('.');
  let val = dict;

  for (const part of parts) {
    if (val && typeof val === 'object' && part in val) {
      val = val[part];
    } else {
      // Fallback to English
      val = getFallback(key);
      break;
    }
  }

  if (typeof val !== 'string') {
    return key;
  }

  // Parameter interpolation: {param}
  return val.replace(/\{(\w+)\}/g, (_, k) => (k in params ? params[k] : `{${k}}`));
}

function getFallback(key) {
  const parts = key.split('.');
  let val = localesData.en || localesData.id || {};
  for (const part of parts) {
    if (val && typeof val === 'object' && part in val) {
      val = val[part];
    } else {
      return key;
    }
  }
  return typeof val === 'string' ? val : key;
}

/**
 * Apply translations to DOM elements with `data-i18n` attributes
 * @param {HTMLElement|Document} container
 */
export function applyToDOM(container) {
  const root = container || (typeof document !== 'undefined' ? document : null);
  if (!root) return;

  if (typeof document !== 'undefined' && document.documentElement) {
    document.documentElement.lang = currentLocale;
  }

  // Update all elements with data-i18n attribute
  root.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (key) {
      el.innerHTML = t(key);
    }
  });

  // Update active state on language switcher buttons
  root.querySelectorAll('.lang-btn[data-lang]').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-lang') === currentLocale);
  });
}

/**
 * Automatically bind click events on language buttons (.lang-btn[data-lang])
 * @param {HTMLElement|Document} container
 */
export function bindLanguageSwitcher(container) {
  const root = container || (typeof document !== 'undefined' ? document : null);
  if (!root) return;

  root.querySelectorAll('.lang-btn[data-lang]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const lang = btn.getAttribute('data-lang');
      if (lang) {
        setLocale(lang);
      }
    });
  });
}

/**
 * Initialize i18n: Load external JSON and configure default locale
 * @param {string|object} source - Path to locales.json or pre-loaded object
 * @param {string} defaultLang - Initial locale code ('id', 'sa', 'en', 'zh-TW')
 * @returns {Promise<object>} The initialized i18n instance
 */
export async function init(source = './locales.json', defaultLang = 'id') {
  if (Object.keys(localesData).length === 0 || typeof source === 'string') {
    await loadLocales(source);
  }
  setLocale(defaultLang);
  if (typeof document !== 'undefined') {
    applyToDOM();
    bindLanguageSwitcher();
  }
  return i18n;
}

export const i18n = {
  get locales() { return localesData; },
  loadLocales,
  init,
  t,
  setLocale,
  getLocale,
  getAvailableLocales,
  onLocaleChange,
  applyToDOM,
  bindLanguageSwitcher
};

// Global attachment for standard browser scripts
if (typeof window !== 'undefined') {
  window.CellWallI18n = i18n;
}

export default i18n;
