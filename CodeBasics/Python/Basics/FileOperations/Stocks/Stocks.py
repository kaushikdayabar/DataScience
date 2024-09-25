with open("stocks.csv","r") as f,open("stocksAns.csv","a") as fn:
    next(f)
    fn.write("Company Name,PE Ratio,Price To Book Ratio"+"\n")

    for line in f:
        print(line)
        List1=line.split(",")
        stockName=List1[0]
        Price=float(List1[1])
        EPS=float(List1[2])
        BookValue=float(List1[3])

        PE=Price/EPS
        PBR=Price/BookValue

        fn.write(f"{stockName},{PE},{PBR}\n")
        

    
        
        
        
    
        
