class Solution:
    """
    :type  csv: {String[]}
    :rtype: string
    """
    def my_data_process(self, array):
        # create dictionary
        res = dict()
        # separate firt row - keys
        for key in array[0].split(","):
            res[key] = dict()
        # delete extra keys
        del res['FirstName']
        del res['LastName']
        del res['UserName']
        del res['Coffee Quantity']
        # separate array by common
        arr = [[el for el in row.split(",")] for row in array]
        # iterating step
        j = 0
        # check values
        for key in res.keys():
            if j == 1:
                j += 3
            elif j == 8:
                j += 1
            for i in range (1, len(array)):
                # res[key] is key arr[i][j] is value
                if arr[i][j] in res[key]:
                    res[key][arr[i][j]] += 1
                else:
                    res[key][arr[i][j]] = 1
            j += 1
        return str(res).replace(", ", ",").replace(": ", ":").replace("'", '"')
        
# sol = Solution()
# csv = ["Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At", "Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon", "Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon", "Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon", "Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning", "Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon"]
# print (sol.my_data_process(csv))
