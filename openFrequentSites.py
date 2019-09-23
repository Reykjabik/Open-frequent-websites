'''
As long as you have a URL, the webbrowser module lets users cut out the step of
opening the browser and directing themselves to a website. Other programs could
use this functionality to do the following:

AIM: Open several sites that you regularly check.
'''

import webbrowser

most_common_sites = ['https://www.duolingo.com/',
                     'https://www.meneame.net/',
                     'https://outlook.live.com/mail/inbox',
                     'https://foro.cazadividendos.com/',
                     'https://www.datacamp.com/home',
                     'https://app.dataquest.io/dashboard'
                    ]

for i in range(len(most_common_sites)):
    webbrowser.open_new_tab(most_common_sites[i])
