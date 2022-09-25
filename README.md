# web-scraping
Scrape data from tables in Wikipedia, in this example we will scrape tournament results from the Rugby World Cup page: https://en.wikipedia.org/wiki/Rugby_World_Cup

1) SETTING UP THE ENVIRONMENT
In VSCode open up a new terminal. In the top menu, find the Terminal menu and then select New Terminal. Install requirements.txt in a virtual environment:

From Linux terminal:

    python3 -m venv venv 
    source venv/bin/activate 

From Windows powershell

https://www.c-sharpcorner.com/article/steps-to-set-up-a-virtual-environment-for-python-development/
    
    # upgrade pip to its latest version  
    python -m pip install --upgrade pip  

    # install virtualenv  
    pip install virtualenv  

    # create a virtual environment named 'venv', feel free to name it anything you like
    virtualenv venv -p C:\Users\lukem\AppData\Local\Programs\Python\Python36\python.exe 

    # activate the virtual environment 
    .\venv\Scripts\activate
    #if .\activate.ps1 cannot be loaded because running scripts is disabled on system.
        Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

    # check the python version
    python --version
    pip install -r requirements.txt
    # list all packages installed by default
    pip list
    # deactivate the virtual environment
    deactivate

2) CREATE WEB SCRAPING PROJECT (in venv)

    scrapy startproject wikitables
    
    scrapy genspider rugbywc en.wikipedia.org

3) RUN SPIDER (in venv)

    from .\wikitables> scrapy crawl rugbywc

