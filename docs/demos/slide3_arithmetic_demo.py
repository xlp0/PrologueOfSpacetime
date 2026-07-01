from mcard_utils import MCard

def run_clm_script(script_content: str):
    """
    Simulates the execution of a CLM (Cubical Logic Model) script.
    """
    print(f"--- Executing CLM Script ---")
    print(f"Script: {script_content}")
    
    # 1. Parse (Arithmetic)
    tokens = script_content.split()
    if len(tokens) < 3:
        print("Error: Invalid Syntax.")
        return

    # 2. Logic (Geometry)
    operation = tokens[1]
    val1 = int(tokens[0])
    val2 = int(tokens[2])
    
    result = 0
    if operation == "+":
        result = val1 + val2
    elif operation == "*":
        result = val1 * val2

    # 3. Verification (MCard)
    card = MCard(content=str(result), metadata={"type": "calculation"})
    print(f"Result: {result}")
    print(f"Verified Hash: {card.hash}")
    print(f"--- Execution Complete ---")

if __name__ == "__main__":
    # Demo Script: "5 * 5"
    run_clm_script("5 * 5")
