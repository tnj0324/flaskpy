import pandas as pd

df = pd.DataFrame([
  ["0001", "John", "Engineer"],
  ["0002", "Lily", "Sales"]],
  columns=['id', 'name', 'job'])

# CSV ファイル (employee.csv) として出力
df.to_csv("utf8.csv")
