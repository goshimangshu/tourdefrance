import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os
import datetime
os.system('cls')
cont1='y'
while(cont1=='y' or cont1=='n'):
    print("|----------------------------------|")
    print(u"\u001b[1;33m|            Main Menu             |")
    print(u"\u001b[0m|----------------------------------|")
    print("|1. Read the csv file              |")
    print("|2. Data Manipulation              |")
    print("|3. Data Analysis                  |")
    print("|4. Data Visualisation             |")
    print("|5. Data Export into csv           |")
    print("|6. Exit the program               |")
    print("|----------------------------------|")
    choice=int(input("Enter your choice  :"))
    def read():
        csv1=input("Enter the csv file name  :")
        global df
        df=pd.read_csv(csv1)
        df["Date"]= pd.to_datetime(df["Date"])
        df['Winner_Country'].astype(str)
    if (choice==1):
        read()    
        print("----------------------------------------------")
    
        print("Your csv data has been imported successfully ")
        print("----------------------------------------------")
        print("Do you want to view your csv data [y/n]")
        x=input()
        if (x=='y' or x=='Y'):
            print(u"\u001b[1;34mThe content of csv is :")
            print(u"\u001b[0m")
            print(df)
        
        elif x=='n' or x=='N':
            print()
        else:
            print("Error")
            print("Please provide valid input")
        
    elif (choice==2):
        print("|---------------------------------------|")
        print(u"\u001b[1;33m|           DATA MANIPILATION           |")
        print(u"\u001b[0m|---------------------------------------|")
        print("|1. Insert Rows                         |")
        print("|2. Delete Rows                         |")
        print("|3. Delete Columns                      |")
        print("|4. Update Information                  |")
        print("|5. Add another DataFrame file          |")
        print("|6. Sort data                           |")
        print("|---------------------------------------|")
        m=int(input("Enter a choice  :"))
        if (m==1):
            insert=input("Do you want to insert your data in specific row or in the end position[S/E]:-")
            if (insert=="S" or insert=="s"):
                read()
                pos=int(input("Enter the position of new record"))
                Stage=int(input("Enter the Stage-"))
                Date=input("Enter the Date(YYYY-DD-MM) -")
                Distance=int(input("Enter the Distance -"))
                Origin=input("Enter the Origin -")
                Destination=input("Enter the Destination -")
                Type=input("Enter the Type -")
                Winner=input("Enter the Name of the Winner -")
                Winner_Country=input("Enter the Winner Country -")
                stages_TDF={"Stage":[Stage],"Date":[Date],"Distance":[Distance],"Origin":[Origin],"Destination":[Destination],"Type":[Type],"Winner":[Winner],"Winner_Country":[Winner_Country]}
                df2=pd.DataFrame(stages_TDF,index=[pos-1.5])
                df=df.append(df2, ignore_index=False)  
                df = df.sort_index().reset_index(drop=True)                   
                print("Your data has been successfully added at the specific Position")
                print("The details of the inserted row:")
                print(df.loc[pos-1])
                
            if (insert=="E" or insert=="e"):
                read()
                Stage=int(input("Enter the Stage-"))
                Date=input("Enter the Date(YYYY-DD-MM) -")
                Distance=int(input("Enter the Distance -"))
                Origin=input("Enter the Origin -")
                Destination=input("Enter the Destination -")
                Type=input("Enter the Type -")
                Winner=input("Enter the Name of the Winner -")
                Winner_Country=input("Enter the Winner Country -")
                l=len(df.index)
                stages_TDF={"Stage":[Stage],"Date":[Date],"Distance":[Distance],"Origin":[Origin],"Destination":[Destination],"Type":[Type],"Winner":[Winner],"Winner_Country":[Winner_Country]}
                df2=pd.DataFrame(stages_TDF)
                df=df.append(df2, ignore_index=True, sort= False)                     
                print("Your data has been successfully added in the End Position")
                print("The details of the inserted row:")
                print(df.loc[l])
                
        
        elif (m==2):
            read()
            print("Enter the position-")
            pos=int(input())
            print("are you sure you want to delete this row [y/n]")
            d=input()
            if (d=='y' or d=='Y'):
                z=df.drop(index=pos-1)
                print("----------------------------------------------")
                print(u"\u001b[1;32mYour csv data has been modified successfully ",u"\u001b[0m")
                print("----------------------------------------------")

                print("Do you want to view your csv data [y/n]")
                x=input()           
                if (x=='y' or x=='Y'):
                    print(u"\u001b[1;34mThe content of csv is :")
                    print(u"\u001b[0m")
                    print(z)
                elif (x=='n' or x=='N'):
                    print()
            elif (d=='n' or d=='N'):
                print()
            else:
                print(u"\u001b[1;31mError")
                print(u"\u001b[0m")
                print("Please provide valid input")
        elif (m==3):
            read()
            print(df.columns)
            print("Enter the name of the column-")
            c=input()
            print("are you sure you want to delete this column [y/n]")
            d=input()
            if (d=='y' or d=='Y'):
                df.drop(columns=[c], inplace=True)
                print("The given data has Deleted successfully")
            
                print("Do you want to view your csv data [y/n]")
                x=input()
                if (x=='y' or x=='Y'):
                    print(u"\u001b[1;34mThe content of csv is :")
                    print(u"\u001b[0m")
                    print(df)
                elif (x=='n' or x=='N'):
                    print()
                else:
                    print(u"\u001b[1;31mError")
                    print(u"\u001b[0m")
                    print("Please provide valid input") 
            elif (d=='n' or d=='N'):
                print()
            else:
                print(u"\u001b[1;31mError")
                print(u"\u001b[0m")
                print("Please provide valid input")
                
        elif (m==4):
            read()
            print("Since date is the only unique column")
            print("Enter the Date which you want to update-(DD-MM-YYYY)")
            update=input()
            print("Your data with the corresponding Date", update, "is")
            print(df[(df['Date']==update)])
            print("Do you want to update any column[y/n]")
            d=input()
            if (d=='y' or d=='Y'):
                
                Stage=int(input("Enter the Stage-"))
                Date=input("Enter the Date(YYYY-DD-MM) -")
                Distance=int(input("Enter the Distance -"))
                Origin=input("Enter the Origin -")
                Destination=input("Enter the Destination -")
                Type=input("Enter the Type -")
                Winner=input("Enter the Name of the Winner -")
                Winner_Country=input("Enter the Winner Country -")
                stages_TDF=[Stage,Date,Distance,Origin,Destination,Type,Winner,Winner_Country]
                df.loc[df["Date"]==update]=stages_TDF
                print("Your data has been successfully updated")
                print(df[(df['Date']==update)])
            if (d=='n' or d=='N'):
                print()
        elif (m==5):
            read()
            csv2=input("Enter the csv file which you want to add-")
            df2=pd.read_csv(csv2)
            print("This dataFrame file is successfully added")
            print("Do you want to view your csv data? [y/n]")
            x=input()
            if (x=='y' or x=='Y'):
                print(u"\u001b[1;34mThe content of csv is :")
                print(u"\u001b[0m")
                df3=df.append(df2, ignore_index=True)
                print("The new DataFrame is displayed below--")
                print(df3)
            elif (x=='n' or x=='N'):
                print()
            else:
                print(u"\u001b[1;31mError")
                print(u"\u001b20m")
                print("Please provide valid input")
        
        elif (m==6):
            read()
            print("|-------------------------------------------------|")
            print("|                     COLUMNS                     |")
            print("|-------------------------------------------------|")
            print("| Stage                                           |")
            print("| Date                                            |")
            print("| Distance                                        |")
            print("| Origin                                          |")
            print("| Destination                                     |")
            print("| Type                                            |")
            print("| Winner                                          |")
            print("| Winner_Country                                  |")
            print("|-------------------------------------------------|")
            column=input("Enter the column you want to sort-")
            df.sort_values(column, inplace=True)
        
            print("Your Data has been Sorted")
            print("Do You want to view your Sorted Data [y/n]")
            sort=input("Enter your choice    :")
            if (sort=='y' or sort=='Y'):
                print("The content of csv is:")
                print(df)
            elif (sort=='n' or sort=='N'):
                print()
            else:
                print(u"\u001b[1;31mError")
                print(u"\u001b[0m")
                print("Please provide valid input")
        
               
    elif (choice==3):
        print("|---------------------------------------|")
        print(u"\u001b[1;33m|             DATA ANALYSIS             |")
        print(u"\u001b[0m|---------------------------------------|")
        print("|1 Display Top Records                  |")
        print("|2 Display Bottom Records               |")
        print("|3 Display Particular Column/Columns    |")
        print("|4 Display Particular Row/Rows          |")
        print("|---------------------------------------|")
        a=int(input("Enter a choice  :"))
        if (a==1):
            read()
            r=int(input("Enter the no of rows you want to view from the Top-"))
            df=pd.read_csv("stages_TDF.csv")
            print("Top", r,"rows are-")
            print(df.head(r))
    
        elif (a==2):
            read()
            r=int(input("Enter the no of rows you want to view from the Bottom-"))
            df=pd.read_csv("stages_TDF.csv")
            print("Bottom", r,"rows are-")
            print(df.tail(r))
        
        elif (a==3):
             read()
             print("The name of the columns are as follows-")
             print(df.columns)
             print("Enter the column you want to view-")
             a=input()
             print("The values are-")
             print(df[a])
    
        elif (a==4):
              read()
              date=input("Enter the Date for which you want to view the Record(DD-MM-YYYY)-")
              print("The data corresponding to the given date is-")
              print(df[df['Date']==date])
        else:
            print("Error")
            print("Please provide valid input")
    
    elif (choice==4):
       read()
       print("|---------------------------------------|")
       print(u"\u001b[1;33m|          DATA VISUALISATION           |")
       print(u"\u001b[0m|---------------------------------------|")
       print("|1. Draw Line Graph                     |")
       print("|2. Draw bar graph                      |")
       print("|3. Draw Histograph                     |")
       print("|---------------------------------------|")
       v=int(input("Enter choice  :"))
    
       if (v==1):
           print("|---------------------------------------------|")
           print(u"\u001b[1;33m|       LINE GRAPH                            |")
           print(u"\u001b[0m|---------------------------------------------|")
           print("|1. Distance vs Stage                         |")
           print("|2. Distance vs Origin-Destination            |")
           print("|3. Distance vs Country                       |")
           print("|4. No. of winners vs Country                 |")
           print("|5. No. of stages vs Type                     |")
           print("|---------------------------------------------|")
           h=int(input("Enter your choice  :"))
           if (h==1):
               print("Let's filter the data according to YEAR")
               year1=int(input("Enter the year for which you want the graph  :"))
               dist=df["Distance"]
               dist1=dist[df["Date"].dt.year==year1]
               stag=df["Stage"]
               stage1=stag[df["Date"].dt.year==year1]
               plt.plot(stage1,dist1,label="Distance covered in each stage",color='red')
               plt.xlabel("Stage")
               plt.ylabel("Distance")
               plt.grid()
               title="Distance vs Stage"
               plt.title(title,color='black',fontsize=14)
               plt.show()
               
           elif (h==2):
                fig=plt.gcf()
                fig.set_size_inches(20,18,forward=True)
                fig.savefig('figure.png',dpi=100)
                print("Let's filter the data according to YEAR")
                year1=int(input("Enter the year for which you want the graph  :"))
                dist=df["Distance"]
                dist1=list(dist[df["Date"].dt.year==year1])
                o=df["Origin"]
                d=df["Destination"]
                o1=list(o[df["Date"].dt.year==year1])
                d1=list(d[df["Date"].dt.year==year1])
                od1=[i+"-"+j for i,j in zip(o1,d1)]
                plt.plot(od1,dist1,label="Distance between origin and destination",color='red')
                plt.legend(loc="best")
                plt.xlabel("Origin-Destination",fontsize=9)
                plt.ylabel("Distance")
                plt.grid()
                title="Distance vs Winner"
                plt.xticks(rotation=45)
                plt.title(title,color='black',fontsize=14)
                plt.show()
                
           elif (h==3):
                fig=plt.gcf()
                fig.set_size_inches(20,18,forward=True)
                fig.savefig('figure.png',dpi=100)
                print("Let's filter the data according to YEAR")
                year1=int(input("Enter the year for which you want the graph  :"))
                df=df[df["Date"].dt.year==year1]
                df.sort_values("Winner_Country", inplace = True)
                l=df.groupby("Winner_Country")
                m=l.sum()
                df.drop_duplicates(subset="Winner_Country", keep ='first', inplace = True)
                country=df["Winner_Country"]
                country1=list(country)
                distance=list(m["Distance"])
                plt.plot(country1,distance,label="Total distance covered by each Winner Country",color='red')
                plt.legend(loc="best")
                plt.xlabel("Winner Country",fontsize=9)
                plt.ylabel("Distance")
                plt.grid()
                title="Distance vs Winner Country"
                plt.xticks(rotation=45)
                plt.title(title,color='black',fontsize=14)
                plt.show()
                
           elif (h==4):
                fig=plt.gcf()
                fig.set_size_inches(20,18,forward=True)
                fig.savefig('figure.png',dpi=100)
                print("Let's filter the data according to YEAR")
                year1=int(input("Enter the year for which you want the graph  :"))
                df=df[df["Date"].dt.year==year1]
                l=df.groupby("Winner_Country")
                counter=l["Winner_Country"].value_counts(sort=False)
                counter1=list(counter)
                df.sort_values("Winner_Country", inplace = True)
                df.drop_duplicates(subset="Winner_Country", keep ='first', inplace = True)
                country=df["Winner_Country"]
                country1=list(country)
                plt.plot(country1,counter1,label="Number of Winners from Each Country",color='red')
                plt.legend(loc="best")
                plt.xlabel("Winner Country",fontsize=9)
                plt.ylabel("Number of Winners")
                plt.grid()
                title="Number of Winners vs Country"
                plt.xticks(rotation=45)
                plt.title(title,color='black',fontsize=14)
                plt.show()
    
           elif (h==5): 
                fig=plt.gcf()
                fig.set_size_inches(20,18,forward=True)
                fig.savefig('figure.png',dpi=100)
                print("Let's filter the data according to YEAR")
                year1=int(input("Enter the year for which you want the graph  :"))
                df=df[df["Date"].dt.year==year1]
                l=df.groupby("Type")
                counter=l["Type"].value_counts(sort=False)
                counter1=list(counter)
                df.sort_values("Type", inplace = True)
                df.drop_duplicates(subset="Type", keep ='first', inplace = True)
                stype=df["Type"]
                country1=list(stype)
                plt.plot(stype,counter1,label="Number of Stages of each Type",color='red')
                plt.legend(loc="best")
                plt.xlabel("Stage Type",fontsize=9)
                plt.ylabel("Number of Stages")
                plt.grid()
                title="Number of Stages vs Type"
                plt.xticks(rotation=45)
                plt.title(title,color='black',fontsize=14)
                plt.show()
                
            
       elif (v==2):
            print("|--------------------------------------------|")
            print(u"\u001b[1;33m|          BAR GRAPH                         |")
            print(u"\u001b[0m|--------------------------------------------|")
            print("|1. Distance vs Stage                        |")
            print("|2. Distance vs Origin-Destination           |")
            print("|3. Distance vs Country                      |")
            print("|4. No. of winners vs Country                |")
            print("|5. No. of stages vs Type                    |")
            print("|--------------------------------------------|")
            h=int(input("Enter your choice  :"))
            if (h==1):
               print("Let's filter the data according to YEAR")
               year1=int(input("Enter the year for which you want the graph  :"))
               dist=df["Distance"]
               dist1=dist[df["Date"].dt.year==year1]
               stag=df["Stage"]
               stage1=stag[df["Date"].dt.year==year1]
               plt.bar(stage1,dist1,label="Distance covered in each stage",color='red')
               plt.xlabel("Stage")
               plt.ylabel("Distance")
               plt.grid()
               title="Distance vs Stage"
               plt.title(title,color='black',fontsize=14)
               plt.show()
            elif (h==2):
                fig=plt.gcf()
                fig.set_size_inches(20,18,forward=True)
                fig.savefig('figure.png',dpi=100)
                print("Let's filter the data according to YEAR")
                year1=int(input("Enter the year for which you want the graph  :"))
                dist=df["Distance"]
                dist1=list(dist[df["Date"].dt.year==year1])
                o=df["Origin"]
                d=df["Destination"]
                o1=list(o[df["Date"].dt.year==year1])
                d1=list(d[df["Date"].dt.year==year1])
                od1=[i+"-"+j for i,j in zip(o1,d1)]
                plt.bar(od1,dist1,label="Distance between origin and destination",color='red')
                plt.legend(loc="best")
                plt.xlabel("Origin-Destination",fontsize=9)
                plt.ylabel("Distance")
                plt.grid()
                title="Distance vs Winner"
                plt.xticks(rotation=45)
                plt.title(title,color='black',fontsize=14)
                plt.show()
                
            elif (h==3):
                fig=plt.gcf()
                fig.set_size_inches(20,18,forward=True)
                fig.savefig('figure.png',dpi=100)
                print("Let's filter the data according to YEAR")
                year1=int(input("Enter the year for which you want the graph  :"))
                df=df[df["Date"].dt.year==year1]
                df.sort_values("Winner_Country", inplace = True)
                l=df.groupby("Winner_Country")
                m=l.sum()
                df.drop_duplicates(subset="Winner_Country", keep ='first', inplace = True)
                country=df["Winner_Country"]
                country1=list(country)
                distance=list(m["Distance"])
                plt.bar(country1,distance,label="Total distance covered by each Winner Country",color='red')
                plt.legend(loc="best")
                plt.xlabel("Winner Country",fontsize=9)
                plt.ylabel("Distance")
                plt.grid()
                title="Distance vs Winner Country"
                plt.xticks(rotation=45)
                plt.title(title,color='black',fontsize=14)
                plt.show()
                
            elif (h==4):
                fig=plt.gcf()
                fig.set_size_inches(20,18,forward=True)
                fig.savefig('figure.png',dpi=100)
                print("Let's filter the data according to YEAR")
                year1=int(input("Enter the year for which you want the graph  :"))
                df=df[df["Date"].dt.year==year1]
                l=df.groupby("Winner_Country")
                counter=l["Winner_Country"].value_counts(sort=False)
                counter1=list(counter)
                df.sort_values("Winner_Country", inplace = True)
                df.drop_duplicates(subset="Winner_Country", keep ='first', inplace = True)
                country=df["Winner_Country"]
                country1=list(country)
                plt.bar(country1,counter1,label="Number of Winners from Each Country",color='red')
                plt.legend(loc="best")
                plt.xlabel("Winner Country",fontsize=9)
                plt.ylabel("Number of Winners")
                plt.grid()
                title="Number of Winners vs Country"
                plt.xticks(rotation=45)
                plt.title(title,color='black',fontsize=14)
                plt.show()
            
            elif (h==5): 
                fig=plt.gcf()
                fig.set_size_inches(20,18,forward=True)
                fig.savefig('figure.png',dpi=100)
                print("Let's filter the data according to YEAR")
                year1=int(input("Enter the year for which you want the graph  :"))
                df=df[df["Date"].dt.year==year1]
                l=df.groupby("Type")
                counter=l["Type"].value_counts(sort=False)
                counter1=list(counter)
                df.sort_values("Type", inplace = True)
                df.drop_duplicates(subset="Type", keep ='first', inplace = True)
                stype=df["Type"]
                country1=list(stype)
                plt.bar(stype,counter1,label="Number of Stages of each Type",color='red')
                plt.legend(loc="best")
                plt.xlabel("Stage Type",fontsize=9)
                plt.ylabel("Number of Stages")
                plt.grid()
                title="Number of Stages vs Type"
                plt.xticks(rotation=45)
                plt.title(title,color='black',fontsize=14)
                plt.show()
               
               
               
       elif (v==3):
            print("|--------------------------------------------|")
            print(u"\u001b[1;33m|          HISTOGRAPH                        |")
            print(u"\u001b[0m|--------------------------------------------|")
            print("|1. No. of Winners vs Distance(interval-wise)   |")
            print("|-----------------------------------------------|")
            h=int(input("Enter your choice  :"))
            if (h==1):
               print("Let's filter the data according to YEAR")
               year1=int(input("Enter the year for which you want the graph  :"))
               dist=df["Distance"]
               dist1=dist[df["Date"].dt.year==year1]
               plt.hist(dist1,label="No. of winners for each distance category",color='red')
               plt.xlabel("Distance Intervals")
               plt.ylabel("No. of Winners")
               plt.grid()
               title="No. of Winners vs Distance(interval-wise)"
               plt.title(title,color='black',fontsize=14)
               plt.show()
            else:
                print(u"\u001b[1;31mError")
                print(u"\u001b[0m")
                print("Please provide valid input")
    elif (choice==5):
        read()
        print("|--------------------------------------------|")
        print(u"\u001b[1;33m|          DATA EXPORTING                   |")
        print(u"\u001b[0m|--------------------------------------------|")
        print("1. Export without index                      |")
        print("2. Export with index                         |")
        print("|--------------------------------------------|")    
        e=int(input("Enter your choice:-"))
        if (e==1):
            print("Exporting the csv file without index")
            df2=df.to_csv('df', index=False)
            
            print("----------------------------------------------")
            print(u"\u001b[1;32mYour csv data has been exported successfully ",u"\u001b[0m")
            print("----------------------------------------------")
        
        elif (e==2):
            print("Exporting the csv file with index")
            print(df.to_csv('df'))
            print("----------------------------------------------")
            print(u"\u001b[1;32mYour csv data has been exported successfully ",u"\u001b[0m")
            print("----------------------------------------------")
        
        else:
            print(u"\u001b[1;31mError")
            print(u"\u001b[0m")
            print("Please provide valid input")
    elif (choice==6):
        print("THANK YOU")
        sys.exit(0)
cont1=input("Do you want to continue?")
  