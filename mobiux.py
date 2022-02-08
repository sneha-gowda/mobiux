import datetime 
"""Reading csv file and loading it to list"""

def loadData(filepath):
    data =  []
    col = []
    checkcol = False
    with open(filepath) as f:
        for val in f.readlines():
            val = val.split(',')
            if checkcol is False:
                col = val
                checkcol = True
            else:
                formater="%Y-%m-%d"
                date=datetime.datetime.strptime(val[0], formater).date()# converting string to date
                month=date.month#addign an extra coloumn to improve search operation
                val[-1]=int(val[-1])
                val[-2]=int(val[-2])
                val[-3]=int(val[-3])
                val[0]=date
                val.append(month)
                data.append(val)
    return data,col
"""end to reading file"""



parlorData,coloumns = loadData('data.csv')
print(type(parlorData[0][0]),parlorData[0][-1])

# print("************************")
# print("Coloumns\n",*coloumns)
# print("************************");

# print("\n************************")
# print("Total number Sales =",len(parlorData))
# print("************************");
year_total_sales=len(parlorData)
year_total_items_sold=0
year_total_revenue=0

def binarySearchStart(key):
    low=0
    high=len(parlorData)-1
    while(low<=high):
        mid=(low+high)//2
        if(mid==0):
            return 0
        if(parlorData[mid][-1]==key and parlorData[mid-1][-1]!=key):
            return mid
        elif(parlorData[mid][-1]>=key):
            high=mid-1
        else:
            low=mid+1
    return None
def binarySearchEnd(key):
    low=0
    high=len(parlorData)-1
    while(low<=high):
        mid=(low+high)//2
        if(mid==len(parlorData)-1):
            return mid
        if(parlorData[mid][-1]==key and parlorData[mid+1][-1]!=key):
            return mid
        elif(parlorData[mid][-1]>key):
            high=mid-1
        else:
            low=mid+1
    return None

months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",  "December" ]

for index, month in enumerate(months):
    startIndxe=binarySearchStart(index+1)
    endIndex=binarySearchEnd(index+1)
    if(startIndxe==None or endIndex==NoneTypegit )
    month_total_numberOf_sales=endIndex-startIndxe+1
    month_total_items_sold=0
    month_total_money_made=0
    most_popular_item=None
    mpi_count=0
    most_revenue_item=None
    mri_count=0
    items_count_dic={}
    item_price_dic={}
    for i in range(startIndxe,endIndex+1):
        month_total_items_sold+=parlorData[i][-3]
        month_total_money_made+=parlorData[i][-2]
        if(parlorData[i][1] in items_count_dic):
            items_count_dic[parlorData[i][1]]+=parlorData[i][-3]
        else:
            items_count_dic[parlorData[i][1]]=parlorData[i][-3]
            item_price_dic[parlorData[i][1]]=parlorData[i][2]
    for i in items_count_dic:
        if(items_count_dic[i]>mpi_count):
            most_popular_item=i
            mpi_count=items_count_dic[i]
        if(item_price_dic[i]*items_count_dic[i]>mri_count):
            mri_count=item_price_dic[i]*items_count_dic[i]
            most_revenue_item=i
    min_purchase_quantity=float("inf")
    max_purchase_quantity=0
    count=0
    
    for i in range(startIndxe,endIndex+1):
        if(parlorData[i][1]==most_popular_item):
            min_purchase_quantity=min(min_purchase_quantity,parlorData[i][-3])
            max_purchase_quantity=max(min_purchase_quantity,parlorData[i][-3])
            count+=1
    avg_purchase_quantity=mpi_count/count
    print("***************************")
    print("Month ",month)
    print("Number Of Sales",month_total_numberOf_sales)
    print("Total number of items sold",month_total_items_sold)
    print("Money made by sale",month_total_money_made)
    print("Most popular item",most_popular_item)
    print("Items generating most revenue",most_revenue_item)
    print("The min, max and average number of qunatity of most popular item",)
    print("\t Minimum =",min_purchase_quantity)
    print("\t Maximum =",max_purchase_quantity)
    print("\t Average =",avg_purchase_quantity)
    print("***************************")
    year_total_items_sold+=month_total_items_sold
    year_total_revenue+=month_total_money_made
    year_total_sales+=month_total_numberOf_sales
print("********************************")
print("Complete Year details")
print("\t Total items sold =",year_total_items_sold)
print("\t Total number of sales =",year_total_sales)
print("\t Total revenue made =",year_total_revenue)


