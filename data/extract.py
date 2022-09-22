import pandas as pd

# change these addresses and file names
src_address = "C:\\Users\\Andrea\\Documents\\ETF\\Theatre Sound\\tdoa\\data\\main_dataset\\flight-dataset\\csv-data\\const1\\const1-trial1-tdoa2.csv"
dst_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial1-tdoa2-extracted.xlsx"

# read data from the csv file
read_data = pd.read_csv(src_address)
#print(read_data.info())

# delete all rows where ground truth position is not provided
# read_data = read_data[read_data["pose_x"].notna()]
# print(read_data.info())

# extract only needed columns
read_data = read_data[["idA", "idB", "tdoa_meas", "t_tdoa", "pose_x", "pose_y", "pose_z", "t_pose"]]
read_data["idA"] = pd.to_numeric(read_data["idA"], downcast='integer')
read_data["idB"] = pd.to_numeric(read_data["idB"], downcast='integer')
#print(read_data.info())
#print(read_data)

# write into a new excel file
read_data.to_excel(dst_address, index=False)
