/**
 * MCard Stack: The Topographic Cell Wall
 * Chapter: 02 - The Meaning of Shape
 * 
 * Powered by i18n Standard (Indonesian, Pure Sanskrit, English, Traditional Chinese)
 * "Space is not empty; boundaries define meaning, ownership, and sovereignty."
 */

import { i18n, t, setLocale } from './i18n.js';

class TopographicCellWall {
  constructor(options = {}) {
    this.locale = options.locale || 'id';
    setLocale(this.locale);

    this.vertices = [];
    this.isClosed = false;
    this.protectedTokens = 100;
    this.shearPressure = 150; // External shear Pa when unshielded
    this.leakRate = 10;       // Tokens leaking per cycle when boundary is open

    console.log(t('demon.elderTitle'));
    console.log(t('demon.elderRoar'));
    console.log(t('demon.elderWarn'));
    console.log("--------------------------------------------------------------------------------");
  }

  /**
   * Add a boundary vertex anchor
   * @param {number} x
   * @param {number} y
   */
  addVertex(x, y) {
    if (this.isClosed) {
      this.isClosed = false; // Modifying vertices breaks closed seal
    }
    const vertex = { x: Math.round(x), y: Math.round(y) };
    this.vertices.push(vertex);

    const metrics = this.computeMetrics();
    console.log(` > ${t('logs.vertexAdded', { index: this.vertices.length, x: vertex.x, y: vertex.y })}`);
    console.log(`   ${t('canvas.perimeterLabel', { length: metrics.perimeter })} | ${t('canvas.areaLabel', { area: metrics.area })}`);
    return vertex;
  }

  /**
   * Close the perimeter loop, asserting Gauss-Bonnet 2pi theorem
   */
  closeLoop() {
    if (this.vertices.length < 3) {
      console.log(`!! ${t('gasingHint.breach').replace(/<[^>]+>/g, '')} !!`);
      return false;
    }

    this.isClosed = true;
    this.shearPressure = 0;
    this.leakRate = 0;
    const metrics = this.computeMetrics();

    console.log(`\n🎉 ${t('logs.closed', { area: metrics.area })}`);
    console.log(`   Gauss-Bonnet Angle Sum : ${metrics.angleSum.toFixed(1)}° (Ideal: 360° / 2π)`);
    console.log(`   Angular Defect         : ${metrics.defect.toFixed(2)}°`);
    console.log(`   Isoperimetric Ratio Q  : ${metrics.q.toFixed(3)} (Max: 1.000)`);
    console.log(`   Status                 : ${t('status.enclosed')}`);
    console.log(`   Protected Tokens       : ${this.protectedTokens} / 100 preserved`);
    return true;
  }

  /**
   * Calculate polygon perimeter, area, and exterior turning angles
   */
  computeMetrics() {
    const n = this.vertices.length;
    if (n < 2) {
      return { perimeter: 0, area: 0, q: 0, angleSum: 0, defect: 360 };
    }

    // 1. Perimeter length L
    let perimeter = 0;
    for (let i = 0; i < n; i++) {
      if (i < n - 1 || this.isClosed) {
        const next = this.vertices[(i + 1) % n];
        const dx = next.x - this.vertices[i].x;
        const dy = next.y - this.vertices[i].y;
        perimeter += Math.sqrt(dx * dx + dy * dy);
      }
    }

    // 2. Shoelace Area A
    let area = 0;
    if (n >= 3) {
      for (let i = 0; i < n; i++) {
        const next = this.vertices[(i + 1) % n];
        area += this.vertices[i].x * next.y - next.x * this.vertices[i].y;
      }
      area = Math.abs(area) / 2;
    }

    // 3. Isoperimetric quotient Q = 4 * pi * A / L^2
    const q = (perimeter > 0 && area > 0) ? Math.min(1.0, (4 * Math.PI * area) / (perimeter * perimeter)) : 0;

    // 4. Exterior angle turns sum for simple polygon (Gauss-Bonnet planar equivalent)
    let angleSum = 0;
    if (n >= 3 && this.isClosed) {
      for (let i = 0; i < n; i++) {
        const prev = this.vertices[(i - 1 + n) % n];
        const curr = this.vertices[i];
        const next = this.vertices[(i + 1) % n];

        const v1 = { x: curr.x - prev.x, y: curr.y - prev.y };
        const v2 = { x: next.x - curr.x, y: next.y - curr.y };

        const dot = v1.x * v2.x + v1.y * v2.y;
        const det = v1.x * v2.y - v1.y * v2.x;
        let turning = Math.atan2(det, dot) * (180 / Math.PI);
        angleSum += turning;
      }
      angleSum = Math.abs(angleSum);
    }
    const defect = this.isClosed ? Math.abs(360 - angleSum) : 360;

    return {
      perimeter: Math.round(perimeter),
      area: Math.round(area),
      q,
      angleSum,
      defect
    };
  }

  /**
   * Simulate a pulse of external thermal shear
   */
  tickShear() {
    if (!this.isClosed) {
      this.protectedTokens = Math.max(0, this.protectedTokens - this.leakRate);
      console.log(` > [SHEAR PULSE] Perimeter open! ${this.leakRate} tokens lost to void. Vault: ${this.protectedTokens}`);
      if (this.protectedTokens === 0) {
        console.log(`\n${t('demon.breachAlert')}`);
        console.log(` > ${t('status.critical')}`);
      }
    } else {
      console.log(` > [SHEAR PULSE] Deflected by 2π Gauss-Bonnet membrane! Vault intact: ${this.protectedTokens} tokens.`);
    }
  }

  /**
   * Reset canvas to pure Kenotic empty void
   */
  reset() {
    this.vertices = [];
    this.isClosed = false;
    this.protectedTokens = 100;
    this.shearPressure = 150;
    console.log(`\n${t('logs.reset')}`);
  }
}

// CLI Execution Simulation
const isMain = process.argv[1] && process.argv[1].endsWith('cell_wall.js');
if (isMain) {
  let cliLang = process.argv[2] || 'id';
  if (cliLang === 'sa-bali' || cliLang === 'sanskrit' || cliLang === 'bali') cliLang = 'sa';
  console.log(`[i18n] Running Topographic Cell Wall simulation with locale: '${cliLang}' (Supported: 'id', 'sa', 'en', 'zh-TW')\n`);
  
  const cell = new TopographicCellWall({ locale: cliLang });

  // 1. Initial State: Unprotected Tokens in the Void
  console.log("--- 1. HOSTILE VOID EXPOSURE ---");
  cell.tickShear();

  // 2. Placing Regular Hexagonal Boundary Nodes
  console.log("\n--- 2. DEPLOYING CELL WALL NODES ---");
  const cx = 200, cy = 200, r = 100;
  for (let i = 0; i < 6; i++) {
    const angle = (i * 60) * (Math.PI / 180);
    const x = cx + r * Math.cos(angle);
    const y = cy + r * Math.sin(angle);
    cell.addVertex(x, y);
  }

  // 3. Closing Perimeter Loop (Gauss-Bonnet 2pi Theorem)
  console.log("\n--- 3. SEALING CELLULAR MEMBRANE (2π CLOSURE) ---");
  cell.closeLoop();

  // 4. Testing External Thermal Shear Against Closed Sanctuary
  console.log("\n--- 4. DEFLECTING EXTERNAL THERMAL SHEAR ---");
  cell.tickShear();
  cell.tickShear();
  console.log("--------------------------------------------------------------------------------\n");
}

export default TopographicCellWall;
export { TopographicCellWall, i18n };
