# CSE6242-ATL_UBER


-------------

Author          : Zhekun Qi, Yiqiong Xiao, Shuting Lin, Jie Zhou, Xiang Zhong


## DESCRIPTION
-------------

Analyzing and visualizing 12 months' travel time data from Uber in Atlanta in 2019. We render a web service that can visualize adn predict the average travel time. 

## INSTALLATION
-------------
You can access the application directly via the link below:
https://atlantauber.azurewebsites.net/

Or if you decide to run it locally, this application requires [Node.js](https://nodejs.org/).

The package includes dependencies files, you can just start the server.

```sh
$ cd ATL_Uber
$ PORT=3000 node server.js
```

## EXECUTION
-------------

### Step 1  Launch the application
 - Option 1 (recommended)
We deployed our web service on Azure. You can access it directly via the link below:
https://atlantauber.azurewebsites.net/

 - Option 2
You can also run the application locally. After installed all the files, you can input the command below in the terminal.  Then access localhost:3000 using a browser(Chrome is recommended).
```sh 
$ PORT=3000 node server.js
```

### Step 2 Explore the features
Click the get started button and you will see the main project page. Due to the huge amount of data to be loaded, **the image below the slider will show after approximately 15 seconds**. Please be patient. 
 - Click any area on the map and select it as the origin point, the choropleth map would show you the the average travel time from that point to any destination in atlanta.
 - Slide the slider above the map to select the month you want to explore. The refreshing process may cost up to 10 seconds.
 - Put your mouse over certain area, you will see its ID. Then input an origin ID and a destination ID, you will see the approximate distance and the prediction trip time.
