/**
 * Internationalization (i18n) Module for HyperCard Water Clock
 * Chapter: 01 - The Value of Counting
 * 
 * Supports:
 * - 'id': Bahasa Indonesia
 * - 'en': English
 * - 'zh': 中文 (Simplified Chinese)
 * 
 * Works isomorphically in both Node.js (ES Module) and Browser (window.WaterClockI18n)
 */

export const locales = {
  id: {
    meta: {
      code: 'id',
      name: 'Bahasa Indonesia',
      flag: '🇮🇩'
    },
    header: {
      mainTitle: 'Pancuran Jam Air: Stasiun 01',
      subtitle: '"Menghitung adalah tindakan mengamati yang membutuhkan energi."',
      breadcrumb: 'PROLOGUE OF SPACETIME: CH 01',
      stationBadge: 'STASIUN 01 (INVENTARIS)',
      depthBadge: 'RCA₀ LEVEL 1'
    },
    spigot: {
      banner: '[═══ PANCURAN BAMBU ALIRAN ANALOG ═══]',
      reservoirLabel: 'Akumulasi Air di Bilah Bambu:'
    },
    counter: {
      title: 'Jumlah Tetesan Terhitung (MCard)',
      cidPrefix: 'CID'
    },
    meters: {
      energyLabel: 'Energi Pengamat (E)',
      entropyLabel: 'Entropi / Suhu (H)'
    },
    status: {
      laminar: '💧 Aliran Laminar (Tenang & Optimal — ΔH < 0)',
      turbulent: '⚡ Aliran Turbulen (Terlalu Cepat! Gesekan Panas)',
      overheat: '⚠️ SYSTEM FAILURE: Sensor Kepanasan! Entropi Meledak'
    },
    buttons: {
      startFlow: 'Mulai Aliran',
      stopFlow: 'Hentikan Aliran',
      catchDrop: '💧 Tangkap Tetesan',
      reset: 'Dinginkan / Reset'
    },
    gasingHint: {
      default: '💡 <strong>Prinsip GASing (Asyik)</strong>: Buka kran air dengan tombol "Mulai Aliran", lalu perhatikan tetesan bambu. Klik "Tangkap Tetesan" tepat saat air penuh. Jaga irama tenang (~1 detik sekali) agar mesin tidak kepanasan!',
      laminar: '🌟 <strong>Hebat! (Gampang & Nikmat)</strong>: Irama Anda seimbang sempurna. Aliran laminar tercapai, entropi terkendali!',
      fast: '⚠️ <strong>Awas! (Gesekan Panas)</strong>: Anda memencet terlalu cepat! Prinsip Landauer: gesekan informasi membakar energi dan menciptakan panas.',
      slow: '🌊 <strong>Hati-hati!</strong>: Air meluap dari bilah bambu sebelum sempat dicatat. Fokus pada ritme tetesan.',
      dead: '🔥 <strong>Sensor Mogok!</strong>: Energi terkuras habis. Klik tombol "Dinginkan / Reset" untuk menyegarkan kembali sistem.'
    },
    logs: {
      title: 'BUKU KAS MCARD (IMMUTABLE LOG):',
      entriesCount: '{count} entri',
      init: '> Sistem diinisialisasi. Menunggu aliran air...',
      flowStart: '> Kran dibuka. Air analog mengalir dari pancuran bambu...',
      flowStop: '> Kran ditutup. Aliran air terhenti.',
      reset: '> Sistem didinginkan. Energi dipulihkan ke 100%, Entropi dinetralkan.',
      milestone: '🎉 [MILESTONE] {count} Tetesan Terverifikasi! Harmoni Gamelan Berbunyi.',
      mcardTick: '[MCard #{count}] Δt: {delta}ms | E: {energy}% | H: {entropy}% | CID: {cid}',
      criticalOverheat: '💥 [CRITICAL ALERT] Sensor Kepanasan! Entropi melampaui kapasitas pengamat. Aliran dihentikan.'
    },
    demon: {
      elderTitle: '--- TETUA DESA / VILLAGE ELDER ---',
      elderRoar: 'Sesepuh: "Dengarkan. Kau dengar gemuruh air itu? Itu adalah Aliran Liar. Untuk menghitungnya, kau harus menjedanya sejenak."',
      elderWarn: 'Sesepuh: "Tapi ingat: Mengamati butuh Energi. Terlalu cepat, mesinmu terbakar. Terlalu lambat, kau tenggelam!"',
      actionTriggered: 'Aksi: Klik Pengamatan (Jeda: {delta}ms)',
      feedbackSound: 'Umpan Balik: *Riak Air* ~ *Denting Gamelan Harmonis*',
      overheatAlert: '*** PERINGATAN KRITIS: Sensor Kepanasan ***',
      elderSurrender: 'Sesepuh: "Kau telah menyerah pada Kekacauan. Sungai meluap."',
      gateCollapse: 'Narasi: Gerbang sensor runtuh di bawah beban panas membara.'
    }
  },

  en: {
    meta: {
      code: 'en',
      name: 'English',
      flag: '🇬🇧'
    },
    header: {
      mainTitle: 'HyperCard Water Clock: Station 01',
      subtitle: '"Counting is an act of observation that requires energy."',
      breadcrumb: 'PROLOGUE OF SPACETIME: CH 01',
      stationBadge: 'STATION 01 (INVENTORY)',
      depthBadge: 'RCA₀ LEVEL 1'
    },
    spigot: {
      banner: '[═══ CONTINUOUS ANALOG BAMBOO SLUICE ═══]',
      reservoirLabel: 'Water Accumulation in Bamboo Sluice:'
    },
    counter: {
      title: 'Counted Droplets (MCard Ledger)',
      cidPrefix: 'CID'
    },
    meters: {
      energyLabel: 'Observer Energy (E)',
      entropyLabel: 'Entropy / Thermal Heat (H)'
    },
    status: {
      laminar: '💧 Laminar Flow (Calm & Optimal — ΔH < 0)',
      turbulent: '⚡ Turbulent Flow (Too Fast! Thermal Friction)',
      overheat: '⚠️ SYSTEM FAILURE: Demon Overheated! Sensor Burnout'
    },
    buttons: {
      startFlow: 'Start Flow',
      stopFlow: 'Stop Flow',
      catchDrop: '💧 Catch Drop',
      reset: 'Cool Down / Reset'
    },
    gasingHint: {
      default: '💡 <strong>GASing Principle</strong>: Turn on the flow, observe the bamboo drop, and click "Catch Drop" in a steady ~1s cadence. Maintain laminar flow without overheating!',
      laminar: '🌟 <strong>Optimal Rhythm!</strong>: Locked in resonance. Minimal energy dissipation, entropy stabilized.',
      fast: '⚠️ <strong>Warning!</strong>: Clicking too fast! By Landauer\'s Principle, rapid discrimination dissipates severe thermal friction.',
      slow: '🌊 <strong>Overflow!</strong>: Droplet detached unmeasured. Maintain focus on the cadence.',
      dead: '🔥 <strong>Sensor Offline!</strong>: Energy depleted. Click "Cool Down / Reset" to recover observational capacity.'
    },
    logs: {
      title: 'MCARD IMMUTABLE LEDGER:',
      entriesCount: '{count} entries',
      init: '> System initialized. Awaiting fluid flow...',
      flowStart: '> Sluice opened. Continuous analog stream flowing...',
      flowStop: '> Sluice closed. Flow paused.',
      reset: '> System cooled down. Energy restored to 100%, entropy cleared.',
      milestone: '🎉 [MILESTONE] {count} Droplets Verified! Harmonic Chime Emitted.',
      mcardTick: '[MCard #{count}] Δt: {delta}ms | E: {energy}% | H: {entropy}% | CID: {cid}',
      criticalOverheat: '💥 [CRITICAL ALERT] Demon Overheated! Entropy exceeds observer threshold. Flow halted.'
    },
    demon: {
      elderTitle: '--- VILLAGE ELDER ---',
      elderRoar: 'Elder: "Listen. Do you hear the roar? That is the Raw Flow. To count it, you must pause it."',
      elderWarn: 'Elder: "Observation costs Energy. Count too fast, and you burn. Count too slow, and you drown."',
      actionTriggered: 'Action: Click Triggered (Delta: {delta}ms)',
      feedbackSound: 'Feedback: *Ripple* ~ *Harmonic Chime*',
      overheatAlert: '*** CRITICAL ALERT: Demon Overheated ***',
      elderSurrender: 'Elder: "You have surrendered to Chaos. The river floods."',
      gateCollapse: 'Narrative: The gate collapses under the weight of the heat.'
    }
  },

  zh: {
    meta: {
      code: 'zh',
      name: '中文 (简体)',
      flag: '🇨🇳'
    },
    header: {
      mainTitle: '超卡水钟：第01工位（竹节滴漏）',
      subtitle: '“计数是一种需要消耗物理能量的观测行为。”',
      breadcrumb: '时空序章：第 01 章',
      stationBadge: '第 01 工位（记忆库存 MCARD）',
      depthBadge: 'RCA₀ 递归可计算（第一级）'
    },
    spigot: {
      banner: '[═══ 连续模拟竹筒流水 ═══]',
      reservoirLabel: '竹节凹槽水流积累：'
    },
    counter: {
      title: '已验证水滴总数（MCard 账本）',
      cidPrefix: '内容哈希 CID'
    },
    meters: {
      energyLabel: '观测者能量储备 (E)',
      entropyLabel: '系统熵增 / 温度 (H)'
    },
    status: {
      laminar: '💧 层流状态（平稳谐振，熵减 ΔH < 0）',
      turbulent: '⚡ 湍流摩擦（点击过快！热耗散加剧）',
      overheat: '⚠️ 系统崩溃：麦克斯韦妖过热！熵增失控'
    },
    buttons: {
      startFlow: '开启流水',
      stopFlow: '暂停流水',
      catchDrop: '💧 捕获水滴',
      reset: '冷却重置'
    },
    gasingHint: {
      default: '💡 <strong>GASing 理念（寓教于乐）</strong>：点击“开启流水”，静心观察竹尖成滴。在水滴饱满时点击“捕获水滴”。保持约1秒一次的平稳节奏，系统将保持清凉高效！',
      laminar: '🌟 <strong>节奏绝佳！</strong>：进入层流谐振状态，以最小能耗锁定水滴，系统熵持续下降！',
      fast: '⚠️ <strong>过载警告！</strong>：点击过频！兰道尔原理生效：高频信息抹除剧烈耗散能量并产生热量。',
      slow: '🌊 <strong>水流溢出！</strong>：水滴未及观测即流失。请专注于周期律动。',
      dead: '🔥 <strong>传感器熔断！</strong>：能量耗尽，熵增过载。请点击“冷却重置”恢复观测能力。'
    },
    logs: {
      title: 'MCARD 不可变账本记录：',
      entriesCount: '{count} 条记录',
      init: '> 系统初始化完毕，等待水流注入...',
      flowStart: '> 竹闸开启，模拟水流持续涌入...',
      flowStop: '> 竹闸关闭，水流暂停。',
      reset: '> 系统完成冷却降温，能量恢复至100%，熵归零。',
      milestone: '🎉【里程碑】{count} 滴水滴验证通过！泛音谐振响起。',
      mcardTick: '[MCard #{count}] 观测间隔: {delta}ms | 能量: {energy}% | 熵: {entropy}% | CID: {cid}',
      criticalOverheat: '💥【紧急警报】传感器过热！系统熵超越观测者极限，水流强行中断。'
    },
    demon: {
      elderTitle: '--- 村落长者 ---',
      elderRoar: '长者：“倾听那轰鸣的水声吧。那是混沌的原始之流。若要计数它，你必须先定格它。”',
      elderWarn: '长者：“但切记：观测需要能耗。过快，系统焚毁；过慢，洪流灭顶！”',
      actionTriggered: '动作：点击观测触发（间隔：{delta}毫秒）',
      feedbackSound: '反馈：*水波微漾* ~ *磬乐谐振*',
      overheatAlert: '*** 紧急警报：麦克斯韦妖过热 ***',
      elderSurrender: '长者：“你已向混乱屈服，江河吞没了防线。”',
      gateCollapse: '叙事：观测闸门在炽热的过载能量下崩塌。'
    }
  }
};

let currentLocale = 'id';
const listeners = new Set();

/**
 * Retrieve a nested translation key using dot notation
 * Example: t('header.mainTitle') or t('logs.milestone', { count: 10 })
 */
export function t(key, params = {}, lang = currentLocale) {
  const dict = locales[lang] || locales.en || locales.id;
  const parts = key.split('.');
  let val = dict;

  for (const part of parts) {
    if (val && typeof val === 'object' && part in val) {
      val = val[part];
    } else {
      // Fallback to English if key missing in target lang
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
  let val = locales.en;
  for (const part of parts) {
    if (val && typeof val === 'object' && part in val) {
      val = val[part];
    } else {
      return key;
    }
  }
  return val;
}

export function setLocale(lang) {
  if (locales[lang]) {
    currentLocale = lang;
    for (const listener of listeners) {
      try {
        listener(currentLocale);
      } catch (e) {
        console.error('Error in i18n listener:', e);
      }
    }
  }
  return currentLocale;
}

export function getLocale() {
  return currentLocale;
}

export function getAvailableLocales() {
  return Object.keys(locales).map(k => locales[k].meta);
}

export function onLocaleChange(fn) {
  listeners.add(fn);
  return () => listeners.delete(fn);
}

export const i18n = {
  locales,
  t,
  setLocale,
  getLocale,
  getAvailableLocales,
  onLocaleChange
};

// Expose globally for browser usage when loaded via <script>
if (typeof window !== 'undefined') {
  window.WaterClockI18n = i18n;
}

export default i18n;
