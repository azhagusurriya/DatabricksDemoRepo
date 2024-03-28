# Databricks notebook source
print("hey")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "HII"

# COMMAND ----------

# MAGIC %md
# MAGIC # Hello
# MAGIC ## Hiiiii
# MAGIC ### hiya

# COMMAND ----------

# MAGIC %run ../Includes/Setup
# MAGIC

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


