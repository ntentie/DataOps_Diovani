import pandas as pd

print("✅ Le pipeline s'exécute correctement !")
df = pd.DataFrame({"Test": ["DataOps", "GitHub Actions"]})
df.to_csv("output.csv", index=False)
