import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

                                       #scripping data by use attribute of web_page


#use request to fetch the url
result=requests.get("https://wuzzuf.net/search/jobs/?q=front+end+devolopment&a=hpb")
#save page content
src = result.content
#create soup object to parse
soup = BeautifulSoup(src,"lxml")

#lists that stored deta
job_titles=[]
location_names=[]
company_names=[]
job_times=[]
links=[]

#find the element containing info we need
job_title=soup.find_all("h2",{"class":"css-m604qf"})
location_name=soup.find_all("span",{"class":"css-5wys0k"})
company_name=soup.find_all("a",{"class":"css-17s97q8"})
job_time=soup.find_all("span",{"class":"css-1ve4b75 eoyjyou0"})

#loop retern lists to extract needed info into other lists
for i in range (len(job_title)):
    job_titles.append(job_title[i].text.strip())
    links.append(job_title[i].find("a").attrs['href'].strip())
    location_names.append(location_name[i].text.strip())
    company_names.append(company_name[i].text.strip())
    job_times.append(job_time[i].text.strip())

#to calculat the city that contain max number of jobs
maxcount =0
for i in range (len(location_names)):
    count=0
    j=i+1
    for j in range (len(location_names)):
        if location_names[i]==location_names[j]:
            count +=1
    if count >maxcount:
        maxcount = count
        value = location_names[i]
print (value)
print (maxcount)


#save all data that we need to view
file_list=[job_titles,location_names,company_names,job_times,links]
exported=zip_longest(*file_list)
#create csv file and fill it with values
with open("D:\محاضرات الفرقة الرابعة الترم الثانى/jobs.csv","w",newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title","location name","company name","job times","job links"])
    wr.writerows(exported)




#explain zip_longest
# x=[1,2,3]
# y=["a","b","c"]
# z=[x,y]
# zip_longest(*z) == [[1,2,3],["a","b","c"]] == [1,a][2,b][3,c]






# for link in links:
#     request1=requests.get(link)
#     src1=request1.content
#     soup1 =BeautifulSoup(src1,"lxml")
#     salary=soup1.find_all("div",{"class": "css-rcl8e5"})
#     salarys.append(salary.text.strip())
# print(salarys)