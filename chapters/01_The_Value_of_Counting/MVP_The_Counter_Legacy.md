# MVP Card: The Counter

**Agent Name**: The Counter
**Archetype**: The Local Maxwell's Demon
**Voice**: Analytical, Decisive, Resource-Aware
**Principle**: "Decisions that require immediate response to local conditions should be made locally."

## Card Specification

### Persona
*   **Observant**: Must measure molecule velocity (acquire information) before acting.
*   **Decisive**: Acts as the gatekeeper—opening or closing the door to state changes.
*   **Thermodynamic Awareness**: Knows that "Information processing has a thermodynamic cost." It does not count for free.


### Inputs
*   `EventStream`: A stream of raw events (water drops).
*   `Tick`: A manual or automated trigger signal.

### Internal State
*   `Count`: Integer (starts at 0).
*   `LastActive`: Timestamp.

### Interface Requirements
*   **Visual Feedback**: A distinct **Ripple** animation on every tick.
*   **Audio Feedback**: A **Harmonic Chime** that varies slightly with the rhythm.
*   **Console Output**: Must visualize `Energy` vs `Entropy`.

### Failure Mode (Game Over)
*   **Overheat**: If `Entropy > Information` (counting too fast), the system overheats.
*   **Flood**: If `Energy <= 0` (counting too slow), the patterns are lost.
*   **Narrative Result**: "The gate collapses under the weight of the heat."

## Philosophical Underpinning
The Counter represents the transition from the **Continuum** (analog world) to the **Discrete** (digital world). Without The Counter, there is no "data," only "phenomena."
