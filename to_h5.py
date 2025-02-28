import pandas as pd

# Sample DataFrame (Replace with your actual data)
df = pd.read_csv("cleaned_data.csv")

# Save to HDF5 file
h5_filename = "data.h5"
key_name = "df"

df.to_hdf(h5_filename, key=key_name, mode="w")

# Read back the data to check its content
df_loaded = pd.read_hdf(h5_filename, key=key_name)

# Display the stored data
print("\nContents of the HDF5 file:")
print(df_loaded)

# Show all keys stored in the HDF5 file
with pd.HDFStore(h5_filename) as store:
    print("\nKeys in the HDF5 file:", store.keys())
