import datetime

class Solution:
    """
    :type  csv: {String}
    :rtype: string[]
    """
    def my_csv_parser(self, csv, sep):
        return [[el for el in row.split(sep)] for row in csv.split("\n") if len(row) > 0]

    def my_data_transform(self, csv):
        arr = self.my_csv_parser(csv, ",")
        for row in range (1, len(arr)):
            arr[row][4] = arr[row][4].split("@")[1]
            arr[row][5] = int(arr[row][5])
            if arr[row][5] < 21:
                arr[row][5] = "1->20"
            elif arr[row][5] < 41:
                arr[row][5] = "21->40"
            elif arr[row][5] < 66:
                arr[row][5] = "41->65"
            elif arr[row][5] < 100:
                arr[row][5] = "66->99"
            time_order = datetime.datetime.strptime(arr[row][9], '%Y-%m-%d %H:%M:%S').time()
            t1 = datetime.time (11, 59)
            t2 = datetime.time (17, 59)
            if time_order < t1:
                arr[row][9] = "morning"
            elif time_order < t2:
                arr[row][9] = "afternoon"
            else:
                arr[row][9] = "evening"
        return [",".join(row) for row in arr]

# sol = Solution()
# csv = "Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At\nMale,Carl,Wilderman,carl,wilderman_carl@yahoo.com,29,Seattle,Safari iPhone,2,2020-03-06 16:37:56\nMale,Marvin,Lind,marvin,marvin_lind@hotmail.com,77,Detroit,Chrome Android,2,2020-03-02 13:55:51\nFemale,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21,Las Vegas,Chrome,1,2020-03-05 17:53:05\nFemale,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,81,Seattle,Chrome,2,2020-03-04 10:33:53\nMale,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,47,Chicago,Chrome Android,1,2020-03-05 15:19:48\n"
# print (sol.my_data_transform(csv))
