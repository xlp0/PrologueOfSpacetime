/**
 * HyperCard Stack: The Water Clock
 * Chapter: 01 - The Value of Counting
 * 
 * "Counting is an act of observation that requires energy."
 */

class MaxwellsDemon {
  constructor() {
    this.energy = 100;
    this.entropy = 0;
    this.ticks = 0;
    this.lastTickTime = Date.now();
    this.isOverheated = false;

    console.log("--- VILLAGE ELDER ---");
    console.log("Elder: \"Listen. Do you hear the roar? That is the Raw Flow. To count it, you must pause it.\"");
    console.log("Elder: \"But be warned: Observation costs Energy. Count too fast, and you burn. Count too slow, and you drown.\"");
    console.log("---------------------");
  }

  /**
   * The Tick: The fundamental unit of time.
   * Represents the user manually clicking to capture a drop.
   */
  tick() {
    if (this.isOverheated) {
      console.log("!! SYSTEM FAILURE: Demon Overheated. Entropy Exceeds Information. !!");
      return;
    }

    const now = Date.now();
    const delta = now - this.lastTickTime;

    // Narrative Logic: Determine Thermodynamic Cost based on speed
    let cost = 5; // Base cost
    let entropyGenerated = 1;

    if (delta < 200) {
      console.log("[!] Too Fast! Friction generates Heat.");
      cost = 20;
      entropyGenerated = 15;
    } else if (delta > 2000) {
      console.log("... Too Slow. The pattern washes away ...");
      entropyGenerated = 5;
    }

    // Apply State Changes ( The Monadic Bind )
    // We are 'binding' the current state to the new state through the 'tick' transformation.
    this.energy -= cost;
    this.entropy += entropyGenerated;
    this.ticks += 1;
    this.lastTickTime = now;

    // Visual Feedback ( The Polynomial Lens Output )
    this.renderState(delta);

    // Check Failure Mode
    if (this.energy <= 0 || this.entropy > 50) {
      this.isOverheated = true;
      console.log("\n*** CRITICAL ALERT ***");
      console.log("Elder: \"You have surrendered to Chaos. The river floods.\"");
      console.log("Narrative: The gate collapses under the weight of the heat.");
    }
  }

  renderState(delta) {
    console.log(`\n[Tick #${this.ticks}]`);
    console.log(` > Action: Click Triggered (Delta: ${delta}ms)`);
    console.log(` > Feedback: *Ripple* ~ *Harmonic Chime*`);
    console.log(` > State Monad: { Energy: ${this.energy}% | Entropy: ${this.entropy}% }`);

    if (this.energy > 80 && this.entropy < 10) {
      console.log(" > Status: Flow is Laminar (Optimal)");
    } else {
      console.log(" > Status: Flow is Turbulent (Warning)");
    }
  }
}

// Simulation of User Interaction aka "Vibe Coding"
if (require.main === module) {
  const demon = new MaxwellsDemon();

  // Simulate a "Good Rhythm"
  setTimeout(() => demon.tick(), 500);
  setTimeout(() => demon.tick(), 1100);

  // Simulate "Panic/Chaos" (Clicking too fast)
  setTimeout(() => demon.tick(), 1200);
  setTimeout(() => demon.tick(), 1250);
  setTimeout(() => demon.tick(), 1300);
  setTimeout(() => demon.tick(), 1350);
}

module.exports = MaxwellsDemon;
