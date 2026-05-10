import ollama
import pandas as pd
from tqdm import tqdm

def run_pro_test():
    # 1. Load your leads
    df = pd.read_csv('leads.csv')
    pitches = []

    print(f"🚀 AI Agent active. Processing {len(df)} leads...")
    print("-" * 40)

    # 2. The Progress Bar (tqdm)
    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Writing Compliments", unit="row"):
        
        # THIS IS YOUR EXACT PROMPT FROM BEFORE:
        prompt = f"Write a casual, 1-sentence compliment for {row['Company']} regarding their work in {row['Focus']}. Keep it under 15 words. Avoid hype words like 'revolutionary' or 'innovative'. Sound like a real person."

        try:
            response = ollama.chat(
                model='llama3', 
                messages=[{'role': 'user', 'content': prompt}]
            )
            result = response['message']['content'].strip()
            pitches.append(result)
        except Exception:
            # If one row fails, we save "Error" so the whole 100-row run doesn't stop
            pitches.append("Error in generation")

    # 3. Save the final work
    df['AI_Compliment'] = pitches
    df.to_csv('results.csv', index=False)
    
    print("-" * 40)
    print("✨ SUCCESS: Check 'results.csv' for the final file.")

if __name__ == "__main__":
    run_pro_test()