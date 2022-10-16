from selenium import webdriver
from getpass import getpass
import pandas as pd
import time

url = "https://clutch.co"

driver = webdriver.Chrome(executable_path='./driver/chromedriver')
driver.get(url)
time.sleep(5)

skipCookiePopup = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyButtonAccept"]')
skipCookiePopup.click()
sdl=["Mobile App Development",
"Software Development",
"Web Development",
"AR/VR",
"Artificial Intelligence",
"Blockchain",
"Web Design",
"User Experience Design",
"Logo Design",
"Graphic Design",
"Design",
"Digital Design",
"Digital Marketing",
"SEO",
"Social Media Marketing",
"Mobile Marketing",
"Content Marketing",
"Search Marketing",
"Advertising",
"Branding",
"Creative",
"Video Production",
"Public Relations",
"Media Planning & Buying",
"Call Centers",
"BPO",
"Accounting",
"Commercial Real Estate",
"HR Services",
"Consulting",
"IT Services",
"Cybersecurity",
"Data Analytics",
"Managed IT Services",
"Cloud Consulting",
"Staff Augmentation"]
domains={}
subdomains=driver.find_elements_by_class_name("sitemap-nav__item")
count=0
n=0
subdomainList=[]
for subdomian in subdomains:
    count+=1
    if count<=6:
        domainName="Development"
        n+=1
        a=str(n)
        xpath="/html/body/main/article/section[2]/div/div[2]/div[1]/nav/a["+a+"]"
        sb=subdomian.find_element_by_xpath(xpath)
        if count==6:
            domains[domainName]=subdomainList
            n=0
            subdomainList=[]

    elif count<=12:
        domainName="Design and Production"
        n+=1
        a=str(n)
        xpath="/html/body/main/article/section[2]/div/div[2]/div[2]/nav/a["+a+"]"
        sb=subdomian.find_element_by_xpath(xpath)
        if count==12:
            domains[domainName]=subdomainList
            n=0
            subdomainList=[]

    elif count<=18:
        domainName="Marketing"
        n+=1
        a=str(n)
        xpath="/html/body/main/article/section[2]/div/div[2]/div[3]/nav/a["+a+"]"
        sb=subdomian.find_element_by_xpath(xpath)
        if count==18:
            domains[domainName]=subdomainList
            domains[domainName]=subdomainList
            n=0
            subdomainList=[]

    elif count<=24:
        domainName="Advertising"
        n+=1
        a=str(n)
        xpath="/html/body/main/article/section[2]/div/div[2]/div[4]/nav/a["+a+"]"
        sb=subdomian.find_element_by_xpath(xpath)
        if count==24:
            domains[domainName]=subdomainList
            n=0
            subdomainList=[]

    elif count<=30:
        domainName="Business Services"
        n+=1
        a=str(n)
        xpath="/html/body/main/article/section[2]/div/div[2]/div[5]/nav/a["+a+"]"
        sb=subdomian.find_element_by_xpath(xpath)
        if count==30:
            domains[domainName]=subdomainList
            n=0
            subdomainList=[]
    else:
        domainName="IT Services"
        n+=1
        a=str(n)
        xpath="/html/body/main/article/section[2]/div/div[2]/div[6]/nav/a["+a+"]"
        sb=subdomian.find_element_by_xpath(xpath)


    domain_url=sb.get_attribute("href")
    name=sdl[count-1]
    item=(name,domain_url)
    subdomainList.append(item)
    

domains[domainName]=subdomainList

Company_List=[]
for DomainTitle in domains:
    for subDomainTitle in domains[DomainTitle]:
        url=subDomainTitle[1]
        driver = webdriver.Chrome(executable_path='./driver/chromedriver')


        driver.get(url)
        time.sleep(5)

        
        web = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyButtonAccept"]')
        web.click()
        
        videos = driver.find_elements_by_class_name('row')
        
        n=0
        for video in videos:
            try:
                n+=1
                a=str(n)
                xpath="/html/body/main/section[1]/div[2]/ul/li["+a+"]/div/div[1]/div[1]/div/h3/a"
                title = video.find_element_by_xpath(xpath).text
                xpath="/html/body/main/section[1]/div[2]/ul/li["+a+"]/div/div[1]/div[1]/div/div[1]/span"
                rating=video.find_element_by_xpath(xpath).text
                xpath="/html/body/main/section[1]/div[2]/ul/li["+a+"]/div/div[1]/div[1]/div/div[1]/a[2]"
                reviews=video.find_element_by_xpath(xpath).text
                xpath="/html/body/main/section[1]/div[2]/ul/li["+a+"]/div/div[1]/div[2]/div[1]/div[2]/div[1]/span"
                minprojectsize=video.find_element_by_xpath(xpath).text
                xpath="/html/body/main/section[1]/div[2]/ul/li["+a+"]/div/div[1]/div[2]/div[1]/div[2]/div[3]/span"
                empoyees=video.find_element_by_xpath(xpath).text
                xpath="/html/body/main/section[1]/div[2]/ul/li["+a+"]/div/div[1]/div[2]/div[1]/div[2]/div[4]/span"
                location=video.find_element_by_xpath(xpath).text
                xpath="/html/body/main/section[1]/div[2]/ul/li["+a+"]/div/div[2]/ul/li[1]/a"
                website=video.find_element_by_xpath(xpath)
                website_url=website.get_attribute("href")


                details={"Company Name":title,
                "Domain":DomainTitle,
                "Sub-Domain":subDomainTitle[0],
                "Rating":rating,
                "Review":reviews,
                "Min Project Size": minprojectsize,
                "Number of Employees": empoyees,
                "Location":location,
                "website":website_url
                }

                Company_List.append(details)
    
            except:
                break

df=pd.DataFrame(Company_List)

df.to_excel("C:\\Users\\JAYESH\\Desktop\\DefaultAssignment.xlsx",index=False)