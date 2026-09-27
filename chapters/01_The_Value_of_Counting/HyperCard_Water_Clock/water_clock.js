/**
 * HyperCard Stack: The Water Clock
 * Chapter: 01 - The Value of Counting
 * 
 * Powered by i18n Standard (Indonesian, English, Chinese)
 * "Counting is an act of observation that requires energy."
 */

import { i18n, t, setLocale } from './i18n.js';

class MaxwellsDemon {
  constructor(options = {}) {
    this.locale = options.locale || 'id';
    setLocale(this.locale);

    this.energy = 100;
    this.entropy = 0;
    this.ticks = 0;
    this.lastTickTime = Date.now();
    this.isOverheated = false;

    console.log(t('demon.elderTitle'));
    console.log(t('demon.elderRoar'));
    console.log(t('demon.elderWarn'));
    console.log("---------------------------------");
  }

  /**
   * The Tick: The fundamental unit of time.
   * Represents the user manually clicking to capture a drop.
   */
  tick() {
    if (this.isOverheated) {
      console.log(`!! ${t('status.overheat')} !!`);
      return;
    }

    const now = Date.now();
    const delta = now - this.lastTickTime;

    // Narrative Logic: Determine Thermodynamic Cost based on speed
    let cost = 5; // Base cost
    let entropyGenerated = 1;

    if (delta < 200) {
      console.log(`[!] ${t('gasingHint.fast').replace(/<[^>]+>/g, '')}`);
      cost = 20;
      entropyGenerated = 15;
    } else if (delta > 2000) {
      console.log(`... ${t('gasingHint.slow').replace(/<[^>]+>/g, '')} ...`);
      entropyGenerated = 5;
    }

    // Apply State Changes ( The Monadic Bind )
    this.energy -= cost;
    this.entropy += entropyGenerated;
    this.ticks += 1;
    this.lastTickTime = now;

    // Visual Feedback ( The Polynomial Lens Output )
    this.renderState(delta);

    // Check Failure Mode
    if (this.energy <= 0 || this.entropy > 50) {
      this.isOverheated = true;
      console.log(`\n${t('demon.overheatAlert')}`);
      console.log(t('demon.elderSurrender'));
      console.log(t('demon.gateCollapse'));
    }
  }

  renderState(delta) {
    console.log(`\n[Tick #${this.ticks}]`);
    console.log(` > ${t('demon.actionTriggered', { delta })}`);
    console.log(` > ${t('demon.feedbackSound')}`);
    console.log(` > State Monad: { Energy: ${this.energy}% | Entropy: ${this.entropy}% }`);

    const statusKey = (this.energy > 80 && this.entropy < 10) ? 'status.laminar' : 'status.turbulent';
    console.log(` > Status: ${t(statusKey)}`);
  }
}

// Simulation of User Interaction aka "Vibe Coding"
const isMain = process.argv[1] && process.argv[1].endsWith('water_clock.js');
if (isMain) {
  const cliLang = process.argv[2] || 'id';
  console.log(`[i18n] Running Maxwell's Demon simulation with locale: '${cliLang}' (Supported: 'id', 'en', 'zh')\n`);
  const demon = new MaxwellsDemon({ locale: cliLang });

  // Simulate a "Good Rhythm" (Laminar Flow)
  setTimeout(() => demon.tick(), 500);
  setTimeout(() => demon.tick(), 1100);

  // Simulate "Panic/Chaos" (Clicking too fast - Turbulent Friction)
  setTimeout(() => demon.tick(), 1200);
  setTimeout(() => demon.tick(), 1250);
  setTimeout(() => demon.tick(), 1300);
  setTimeout(() => demon.tick(), 1350);
}

export default MaxwellsDemon;
export { MaxwellsDemon, i18n };
