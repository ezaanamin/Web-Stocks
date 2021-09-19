from django.shortcuts import render
from .models import data1
from .form import stocks
from pandas_datareader import data
from bokeh.plotting import figure,output_file,show
import datetime
from bokeh.embed import components
from bokeh.resources import CDN
from bs4 import BeautifulSoup
import requests
data11=[]
def increase(c,v):
    if c>v:
        value='High'
    elif c<v:
        value='Low'
    else:
        value='equal'
    return value


def mainpage(request):
    m=data1.cursor()
    d=m.execute('SELECT * FROM stocks.main')
    ss = m.fetchall()
    form=stocks(request.GET or None )
    if form.is_valid():
        form.save()
        form=stocks()
    context={
        'form':form,
        'm':m,
        'd':d,
        'ss':ss,
    }
    try:
        name=request.GET['Symbol']
        for row in ss:
            data11.append(row[0])
        if name in data11:
            start=datetime.datetime(2020,1,1)
            end=datetime.datetime(2021,1,1)
            d=data.DataReader(name=name,data_source='yahoo',start=start,end=end)
            d["Status"]=[increase(c,v) for c,v in zip(d.Close,d.Open)]
            d['Middle']=(d.Open+d.Close)/2
            d['Height']=abs(d.Close-d.Open)
            hours_12=12*60*60*1000
            p=figure(x_axis_type="datetime",width=1000,height=300)
            p.title=str(name)+"Stocks through January 2020 through September 2021"
            p.grid.grid_line_alpha=0.3
            p.rect(d.index[d.Status=="High"],d.Middle[d.Status=="High"]
            ,hours_12,d.Height[d.Status=="High"],fill_color="#483D8B",line_color="Black")
            p.rect(d.index[d.Status=="Low"],d.Middle[d.Status=="Low"]
            ,hours_12,d.Height[d.Status=="Low"],fill_color="#8B0000",line_color="Blue")
            p.segment(d.index,d.High,d.index,d.Low)
            script,div=components(p)
            context={
            'script':script,
            'div':div,
            'name':name
            }
    
            return render(request,'stocksmarket/graph3.html',context)
        else:
            return render(request,'stocksmarket/error.html',context)
    except:
        return render(request,'stocksmarket/form.html',context)
    return render(request,'stocksmarket/graph3.html',context)


def homepage(request):
    m=data1.cursor()
    d=m.execute('SELECT * FROM stocks.main')
    ss = m.fetchall()
    context={
        'm':m,
        'd':d,
        'ss':ss,
    }
    return render(request,'stocksmarket/main4.html',context)

    
def home(request):
    r=requests.get("https://www.investopedia.com/articles/investing/082614/how-stock-market-works.asp")
    a=r.content
    b=BeautifulSoup(a,"html.parser")
    Title1=b.find("h2",{"class":"comp mntl-sc-block finance-sc-block-heading mntl-sc-block-heading"})
    par1=b.find("p",{"class":"comp mntl-sc-block finance-sc-block-html mntl-sc-block-html"})
    Title2=b.find("h2",{"id":"mntl-sc-block_1-0-33"})
    par2=b.find("p",{"id":"mntl-sc-block_1-0-34"})
    Title3=b.find("h2",{"id":"mntl-sc-block_1-0-44"})
    par3=b.find("p",{"id":"mntl-sc-block_1-0-45"})
    par11=b.find("p",{"id":"mntl-sc-block_1-0-9"})
    par22=b.find("p",{"id":"mntl-sc-block_1-0-36"})
    par33=b.find("p",{"id":"mntl-sc-block_1-0-47"})
    con={
        "Title1":Title1.text,
        "par1":par1.text,
        "Title2":Title2.text,
        "par2":par2.text,
        "Title3":Title3.text,
        "par3":par3.text,
        "par11":par11.text,
        "par22":par22.text,
        "par33":par33.text
    }
    return render(request,'stocksmarket/main5.html',con)



       



    


